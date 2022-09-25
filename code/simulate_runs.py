from cv2 import mean
# from utils import exponential_elena, exponential_porp, rangeConversion
from RuleBasedMovements import RuleBasedKeywordsMovement
from Speech import Speech
from Sentiment import SentimentAnalyzer
import argparse
import numpy as np

from Gestures import GlobalGestures, MovementDicts
from EyeLEDs import LEDsDicts
# from pydub.playback import play
from utils import rangeConversion
import csv
from GANMovements import RunGANMovement

MAX_PROPORION = 1.2
MIN_PROPORTION = 0.8

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--ip",type=str, default='192.168.1.12', help="Robot IP")
	parser.add_argument("--e", type=int, default=1000, help="Number of epochs of the model")
	parser.add_argument("--um", type=int, default=4, help="Number of poses that composes a Unit of Movement")
	parser.add_argument("--times", type=float, default=0.8, help="Time between poses")
	parser.add_argument("--mocap", type=str, default='openpose', help="Used motion capturing system")
	args = parser.parse_args()

	nao_ip = args.ip
	epoch = args.e
	time_interval = args.times
	um = args.um
	
	n_joints =14
	count = 0
	global_gest = GlobalGestures()
	audio_path = '../downloaded_audio/'
	models_path = "/home/bee/robotak/rsait-crss/python/gan/generation/models/openpose/2020-10-01/openpose_n_epochs_%d_batchSize_32_um_%d/" % (epoch, um)
	simulation = False

	filename = "new_text"
	# filename = "ColorMonster"

	f = open("../text/%s.txt" % filename)
	data = f.read()

	splitData = data.split(".")
	splitData = splitData[:-1]
	
	sa = SentimentAnalyzer()
	compound_score = sa.getPolarity(data, gain = 1.0)
	
	# #New text
	# compound_score = [0.0, -0.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.7, 0.5, 0.0, 0.5, 0.5]
	# # color monster
	# compound_score = [0.0, -0.3, 0.0, -0.2, 0.0, 0.1, 0.0, 0.4, 0.3, 0.4, 0.4, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, -0.5, -0.5, -0.7, -0.7, -0.1, 0.0, 0.0, -0.3, 0.3, -0.2, -0.4, -0.5, -0.6, 0.0]

	md = MovementDicts()
	ledd = LEDsDicts()
	keywords_movements = md.getDict(filename)
	keyword_LEDs = ledd.getDict()

	rb = RuleBasedKeywordsMovement(keywords_movements)
	speech = Speech(audio_path)
	durations = speech.getDurations(filename)


	durations = np.array(durations)

	print(durations)
	print("Audio duration: %f" % sum(durations))
	print("Mean: %f" % np.mean(durations))
	print("Min: %f" % np.min(durations))
	print("Max: %f" % np.max(durations))
	print("Standard Deviation: %f" % np.std(durations))
	print("Median: %s" % np.median(durations))
	
	# max_duration = max(durations) * MAX_PROPORION
	# min_duration = min(durations) * MIN_PROPORTION

	# runGAN = RunGANMovement(n_joints, count, global_gest, models_path, simulation, time_interval) #, tts

	# reportFile = open('GAN_probability_report_exp_Elena_4.5_duration.csv', 'w')
	# csvWriter = csv.writer(reportFile)
	# header = ['Sentence_id', 'DoGAN probability', 'Sentence Duration', 'Do GAN']
	# csvWriter.writerow(header)
	
	# rows = []
	# row = []

	# for _ in range(100):
	# 	for i, t in enumerate(splitData):
	# 		compound_score[i] = 1.0
	# 		row.append(i)
	# 		# Modify the audio files according to the compound score
	# 		file = "%s_%i.wav" % (filename, i)
	# 		# print("Compound score %.2f" % compound_score[i])

	# 		# Convert from compound score to proportion
	# 		proportion = rangeConversion(-1.0, 1.0, MIN_PROPORTION, MAX_PROPORION, compound_score[i])
	# 		rb.setProportion(proportion)
	# 		# runGAN.setProportion(proportion)
	# 		# pleds.setProportion(proportion)
	# 		# Get the duration of the speech and the words with their times in the sentence 
	# 		duration, words_in_speech, words_in_sentence, led_words_in_speech, led_words_in_sentence = speech.getDurationAndWords(t, "%s_%d" %(filename, i), keywords_movements.keys(), keyword_LEDs.keys())
	# 		rb.setKeywords(words_in_sentence)


	# 		movement_duration = 0.0

	# 		# Movement Keyword
	# 		if len(words_in_speech):
	# 			# Choose a random word from all the words in the sentence.
	# 			words_appearance = [rb.used_movements[w[0]] if w[0] in rb.used_movements else 0 for w in words_in_speech]
	# 			if sum(words_appearance) == 0:
	# 				probabilities = [1.0/len(words_appearance) for _ in words_appearance]
	# 			else:
	# 				probabilities =  [1.0-(float(n)/float(sum(words_appearance))) for n in words_appearance]
	# 				sum_probabilities = sum(probabilities)
	# 				if sum_probabilities == 0:
	# 					probabilities = [1.0/len(words_appearance) for _ in words_appearance]
	# 				else:
	# 					probabilities = [x/sum_probabilities for x in probabilities]

	# 			assert sum(probabilities) <= 1.0
	# 			word_index = np.random.choice(range(0, len(words_in_speech)), p = probabilities)
	# 			word = words_in_speech[word_index]
	# 			movement, movement_start, movement_end, movement_duration = rb.getWordPosition(word, duration, time_interval)

	# 			if movement:
	# 				# print("Selected word: %s. Start: %f. End: %f" % (str(word), movement_start, movement_end))

	# 				# If selected movement is longer than the sentence, skip movement modification. 
	# 				if movement_duration < duration:
	# 					runGAN.names, runGAN.keys, runGAN.times = rb.modifyMovement((runGAN.names, runGAN.keys, runGAN.times), movement, movement_start, movement_end, duration, movement_duration, time_interval)
	# 					if word[0] in rb.used_movements:
	# 						rb.used_movements[word[0]] = rb.used_movements[word[0]] + 1
	# 					else:
	# 						rb.used_movements[word[0]] = 1

	# 		# else: 
	# 		# 	print("No word selected for movement. All word's movements take longer than speech duration")


	# 		# Generate the GAN movements
	# 		# runGAN.generateGANMovements(epoch, time_interval, um, duration)

	# 		# Randomly select if the movement is done alone or combined with GAN generated movements
	# 		# Calculate the probability of doing both, GAN + RB movement proportional to speech length
	# 		# pGAN = rangeConversion(min_duration, max_duration, 0.2, 1.0, durations[i])
	# 		# pGAN = exponential_porp(0.99, durations[i], 5.8848, 1.1656)
	# 		pGAN = exponential_elena(durations[i] - movement_duration, 4.5)
	# 		# print(pGAN)

	# 		# In case there is not any rule based movement, increase the probability of generating GAN movements
	# 		# pGain = False
	# 		# if not len(words_in_speech):
	# 		# 	pGAN = min(1.0, pGAN*1.1)
	# 		# 	pGain = True

	# 		doGANMovement = np.random.choice([False, True], p=[1.0-pGAN, pGAN])
			
	# 		row.append(pGAN)
	# 		row.append("%.3f" % duration)
	# 		row.append(doGANMovement)

	# 		csvWriter.writerow(row)
	# 		rows.append(row)
	# 		row = []

	
	# gtAndTrue = 0
	# gtAndFalse = 0
	# ltAndTrue = 0
	# ltAndFalse = 0
	# for row in rows:
	# 	if row[1] >= 0.5 and row[3]:
	# 		gtAndTrue = gtAndTrue + 1
	# 	elif row[1] >= 0.5 and not row[3]:
	# 		gtAndFalse = gtAndFalse + 1
	# 	elif row[1] < 0.5 and row[3]:
	# 		ltAndTrue = ltAndTrue + 1
	# 	elif row[1] < 0.5 and not row[3]:
	# 		ltAndFalse = ltAndFalse + 1

	# print("Greater and True: %d.\nGreater and False: %d.\nLower and True: %d.\nLower and False: %d" % (gtAndTrue, gtAndFalse, ltAndTrue, ltAndFalse))
	
	# reportFile.close()