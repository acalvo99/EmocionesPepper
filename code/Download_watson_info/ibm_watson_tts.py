import subprocess
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


class MySynthesizeCallback(SynthesizeCallback):

	'''
	Callback to save IBM Watson's TTS response into audio file. 
	'''
	def __init__(self):
		SynthesizeCallback.__init__(self)
		self.filename = ""

	def on_error(self, error):
		print('Error received: {}'.format(error))

	def on_timing_information(self, timing_information):
		print(timing_information)

	def on_audio_stream(self, audio_stream):
		'''
		Callback for audio stream. It saves the stream in a file with the name in self.filename
		'''
		assert self.filename!="", "You have to set the filename before calling TextToSpeech.getSpeech()"

		# print("Audio_stream: ", type(audio_stream))
		with open('Download_watson_info/audio/%s' % self.filename, 'ab') as audio_file:
			audio_file.write(audio_stream)

	def set_filename(self, filename):
		'''
		Set the filename of the audio stream destination file

		filename : str
			The name of the file
		'''
		self.filename = filename


class TextToSpeech():
	'''
	Converts text to speech using IBM Watson services

	Methods
	-------

	getSpeech(data, filename)
			Given a string containing the text, it converts to speech and save in the file filename
	'''

	def __init__(self):
		# APIKEY unai.zabalac@ehu.eus
		# authenticator = IAMAuthenticator('qcrNt-cYDGhOP207DYvBN82FL4AIYtIsvWGQqMZXcCz4')
		# self.text_to_speech = TextToSpeechV1(authenticator=authenticator)
		# self.text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/b15f31b2-6490-45f8-afe1-831d7e0a5155')

		# rsait.robotics@gmail.com
		authenticator = IAMAuthenticator('HjQPRMAnsfG0Zn6QQRYuBzrWGTjCH__gT3W_n2rlm9CN')
		self.text_to_speech = TextToSpeechV1(authenticator=authenticator)
		self.text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/8a2d47a9-591c-4abf-9dd1-16cc68c95469')

		self.save_file_callback = MySynthesizeCallback()


	def getDuration(self, filename, path="Download_watson_info/audio/"):
		# Get audio duration
		output = subprocess.check_output(['mediainfo', '--Inform=Audio;%Duration/String3%', '%s%s' % (path, filename)]).decode("utf-8")
		# Remove \n
		output = output.rstrip("\n")
		# Split output into hh:mm:ss.msms
		output = output.split(":")
		duration = int(output[0])*3600 + int(output[1])*60 + float(output[2])
		return duration


	def getSpeechWebsocket(self, data, filename):
		'''
		Given a string containing SSML, it converts to speech and save in the file filename

		Parameters
		----------
		data : str
				A string containing the text
		filename : str
				Destination audio file name
		'''
		
		# WARNING: Some voice parameter options are deprecated and will be removed on 31 March 2023
		self.save_file_callback.set_filename(filename)
		self.text_to_speech.synthesize_using_websocket(
			data,
			self.save_file_callback,
			accept='audio/wav',
			voice='en-US_OliviaV3Voice')
			# voice='en-US_AllisonV3Voice')


if __name__ == "__main__":
	from code.Gestures import MovementDicts
	from code.EyeLEDs import LEDsDicts
	from code.AnnotatedStoryReader import AnnotatedStory
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("--story",type=str, default='ColorMonster', help="The name of the story to be processed")
	args = parser.parse_args()
	story = args.story

	# Save keywords together with the story and get them
	rbdb = MovementDicts()
	ledDict = LEDsDicts()

	movement_keywords = list(rbdb.getDb())
	led_keywords = list(ledDict.getDict())
	movement_keywords.extend(led_keywords)
	all_keywords = movement_keywords

	asr = AnnotatedStory(story, all_keywords)

	# Generate SSML
	ssml = asr.saveAsSSML()

	tts = TextToSpeech()

	durations = []
	filenames = []
	for i, sentence in enumerate(ssml):
		sentence = sentence.decode('UTF-8')
		filename = "%s_%d.wav" % (story, i)
		print("Processing file %s..." % filename)
		# print("SSML Sentence: %s" % sentence)
		# Uncomment this line to call Watson. Comment to use alreade downloaded audio files and don't waste Watson minutes. 
		tts.getSpeechWebsocket(sentence, filename)

		duration = tts.getDuration(filename)
		durations.append(duration)
		filenames.append(filename)
		print("Done")

	# Add new information to AnnotatedStory and save as JSON
	asr.setSentencesDurations(durations=durations)
	asr.setSentencesAudioFilenames(filenames=filenames)
	asr.saveAsJSON()