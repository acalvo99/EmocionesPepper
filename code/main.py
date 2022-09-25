from pydub import AudioSegment
from pydub.playback import play
from RuleBasedMovements import RuleBasedKeywordsMovement
from GANMovements import RunGANMovement
from Speech import Speech
from Sentiment import EmotionByBodyLanguage
from Gestures import MovementDicts
from Gestures import GlobalGestures, MovementDicts
from EyeLEDs import PepperLEDs, LEDsDicts
from utils import sendFileToNao, trimMovement
from utils import readcsv

import argparse
import threading
import qi

import math

import face_emotion as face
#import speechEmotion 

import csv
import pandas as pd
import subprocess

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--ip",type=str, default='127.0.0.1', help="Robot IP")
	parser.add_argument("--e", type=int, default=1000, help="Number of epochs of the model")
	parser.add_argument("--um", type=int, default=4, help="Number of poses that composes a Unit of Movement")
	parser.add_argument("--times", type=float, default=0.8, help="Time between poses")
	parser.add_argument("--mocap", type=str, default='openpose', help="Used motion capturing system")
	parser.add_argument("--storyname", type=str, default="ColorMonster", help="Name of the story")
	args = parser.parse_args()

	nao_ip = args.ip
	epoch = args.e
	time_interval = args.times
	um = args.um
	
	n_joints =14
	global_gest = GlobalGestures()
	audio_path = 'Download_watson_info/audio/'
	models_path = "models/openpose/2020-10-01/openpose_n_epochs_%d_batchSize_32_um_%d/" % (epoch, um)
	storyname = args.storyname
	simulation = False

	if nao_ip=="127.0.0.1":
		simulation = True

	# Start app session
	connection_url = "tcp://" + nao_ip + ":42197"
	app = qi.Application(["PepperGestures", "--qi-url=" + connection_url])
	app.start()
	session = app.session
	motion = session.service("ALMotion")
	memory = session.service("ALMemory")
	aup = session.service("ALAudioPlayer")
	motion.wakeUp()

	# Initalize modules
	speech = Speech()
	beatGen = RunGANMovement(n_joints, global_gest, models_path, simulation, time_interval)
	beatGen.loadGenModel(epoch)
	rb = RuleBasedKeywordsMovement()
	pleds = PepperLEDs(session)
	ledDict = LEDsDicts()
	rbdb = MovementDicts()
	blemo = EmotionByBodyLanguage()

	
	# Save keywords together with the story and get them
	movement_keywords = rbdb.getDb().keys()
	#led_keywords = ledDict.getDict().keys()

	# TODO: Get the emotion from emonet and audio
	filename = '/home/bee/TFM-MAL/pepper_expression/emotions_data.csv'
	dataframe = pd.read_csv(filename)
	index = 47
		
	emotion_emonet, valence_emonet, arousal_emonet = face.predict_emotion(dataframe,index)
	#print("Face Emotion:", emotion_emonet)
	#print("Face Valence:", valence_emonet)
	#print("Face Arousal:", arousal_emonet)
	
	process = subprocess.Popen(args=["python", "speechEmotion.py"],
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE
                           )

	stdout, stderr = process.communicate()
	stdout = stdout.split("\n")
	#print(stdout)

	emotion_audio = stdout[23]
	#print(emotion_audio)
	valence_audio = float(stdout[24])
	#print(valence_audio)
	arousal_audio = float(stdout[25])
	#print(arousal_audio)
	#emotion_audio, valence_audio, arousal_audio = speechEmotion.predict_emotion(dataframe,index)
	#print("Speech Emotion:", emotion_audio)
	#print("Speech Valence:", valence_audio)
	#print("Speech Arousal:", arousal_audio)

	# TODO: Combine both emotion systems
	# combined_valence, combined_arousal = combine(valence_emonet, valence_audio, arousal_emonet, arousal_audio)
	# emotion, intensity = getEmotionAndIntensity(combined_valence, combined_arousal)

	valence = 0.7*valence_emonet + 0.3*valence_audio
	arousal = 0.7*arousal_emonet + 0.3*arousal_audio

	if emotion_emonet==emotion_audio or (emotion_audio=="angry" and emotion_emonet=="anger") or (emotion_audio=="ps" and emotion_emonet=="surprised"):
		emotion = emotion_emonet

	else:
		#ditancia euclidea
		d_face = math.sqrt((valence - arousal)**2 + (valence_emonet - arousal_emonet)**2)
		d_speech = math.sqrt((valence - arousal)**2 + (valence_audio - arousal_audio)**2)
		#print(d_face)
		#print(d_speech)
		if d_face<d_speech:
			emotion = emotion_emonet
		else:
			emotion = emotion_audio
			if emotion=="angry":
				emotion="anger"
			elif emotion=="ps":
				emotion="surprised"

	print("Predicted Emotion:", emotion)
	print("Predicted Valence:", valence)
	print("Predicted Arousal:", arousal)

	intensity = math.sqrt(valence**2 + arousal**2)
	#print("Intensity:", intensity)

	# TODO: Read the story and extract the sentences related to the selected emotion
	story = readcsv("text/csv/%s.csv" % storyname)
	#print(story)
	story = [row for row in story if row[2] == emotion]
	# sentences = filterSentenceByEmotion(sentences, emotion)
	#print(story)


	for i, t in enumerate(story):

		# TODO Conseguir en el orden original la posicion de la frase
		# file_index = getFileIndex()
		file_index = int(t[0])
		#print(file_index)

		# sentence = "sentence_%d" % i

		# Find keywords in text
		# selected_keyword = -1
		# selected_led_keyword = -1
		# if story_dict[sentence].keywords_in_sentence.keywords:
		# if t.keywords:
		# 	selected_keyword = speech.selectKeywordFromSentence(t, "movement")
			# selected_led_keyword = speech.selectKeywordFromSentence(t, "led")

		
		# Generate beat movements
		gan_movement = beatGen.generateGANMovements(time_interval, um, 15.0)
		
		# Add emotion to body language
		final_movement = blemo.modifyBodyLanguageByEmotion(gan_movement, emotion, intensity)

		# Modify speed and pitch (modify the function)
		proportion = speech.modifySpeechWithEmotion("Download_watson_info/audio/%s_%d.wav" % (storyname, file_index), "Download_watson_info/modified_audio/%s_%d.wav" % (storyname, file_index), emotion, intensity)

		# Modify movements tempo
		#print(proportion)
		final_movement[2] = [map(lambda x: x * (2.0-float(proportion)), time) for time in final_movement[2]]
		
		# Set LED color
		pleds.setLEDByEmotion(emotion)
		
		# Remove movevements longer than speech duration
		# TODO: trim movement to fit audio duration

		duration = speech.getDuration("%s_%d.wav" % (storyname, file_index))
		final_movement = trimMovement(final_movement, duration)

		thMotion = False
		if [None for x in gan_movement if x]:
			thMotion = threading.Thread(target=motion.angleInterpolation, args=(final_movement[0], final_movement[1], final_movement[2], True, ))

		if not simulation:
			
			# Upload audio to Pepper
			sendFileToNao(nao_ip = nao_ip, orig_audio_path = 'Download_watson_info/audio/', dest_audio_path="storyteller/", file_name = t.audio_filename)
			fileId = aup.loadFile("/home/nao/storyteller/%s_%d.wav" % (storyname, i))
			thPlay = threading.Thread(target=aup.play, args=(fileId,))

		else:
			# print("Emotion: %s. Intensity: %.2f" % (emotion, intensity))
			sound = AudioSegment.from_mp3("Download_watson_info/modified_audio/%s_%d.wav" % (storyname, file_index))

			thPlay = threading.Thread(target=play, args=(sound,))
		
		if thMotion:
			thMotion.start()
			thPlay.start()
			thMotion.join()
			thPlay.join()
		else: 
			thPlay.start()
			thPlay.join()

		beatGen.emptyKeysAndTimes()
		print("********************************************************************")

	posture = global_gest.getMotion("InitPosture")
	motion.angleInterpolation(posture[0], posture[1], posture[2], True, _async=False)