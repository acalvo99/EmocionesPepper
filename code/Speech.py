from sys import stderr

# from matplotlib.pyplot import annotate
from EyeLEDs import LEDsDicts
from Gestures import MovementDicts
from utils import rangeConversion
import pyrubberband as pyrb
import soundfile as sf
import numpy as np
import os
import re
import yaml
import glob
import subprocess

class Speech():
	'''
	Class to generate speech from text and to look for words position in time in audio files using Watson from IBM Cloud

	Methods
	-------
	generateSpeech(text, filename)
		Generates the speech from text for simulation. The file is then saved in the path defined in the class variable audio_path
	
	recognizeWordsInSpeech(words, filename)
		Finds the corresponding movement of a keyword
	
	generateSpeechAndRecognizeWords(text, filename)
		Modify an existing movement to add a rule based movement
	
	getDurations(filename)
		Get the duration of all the audio files given the base name of all files
	'''

	def __init__(self):
		self.__word_occurrence = {}
		self.__storyname = ""




	def __update_word_occurrence(self, word):
		if word in self.__word_occurrence:
			self.__word_occurrence[word] = self.__word_occurrence[word] + 1
		else:
			self.__word_occurrence[word] = 1

	def __selectWord(self, keywords):
		# TODO: keywords can contain duplicated lemmas if the same lemma occurs in a sentence. For those cases, probabilities aren't accurate. 
		keywords_lemmas = [keyword.lemma for keyword in keywords]

		# Choose a random word from all the words in the sentence.
		# Calculate the number of appearances' inverse proportional probability of a word to be choosen
		words_appearance = [self.__word_occurrence[keyword] if keyword in self.__word_occurrence else 0 for keyword in keywords_lemmas]
		if sum(words_appearance) == 0:
			probabilities = [1.0/len(words_appearance) for _ in words_appearance]
		else:
			probabilities =  [1.0-(float(n)/float(sum(words_appearance))) for n in words_appearance]
			sum_probabilities = sum(probabilities)
			if sum_probabilities == 0:
				probabilities = [1.0/len(words_appearance) for _ in words_appearance]
			else:
				probabilities = [x/sum_probabilities for x in probabilities]

		assert sum(probabilities) <= 1.0, "Probabilites to select a keyword doesn't sum 1.0. "

		# Given the probabilities, choose the word
		word_index = np.random.choice(range(0, len(keywords_lemmas)), p = probabilities)

		self.__update_word_occurrence(keywords_lemmas[word_index])
		
		return keywords[word_index]


	def __getDuration(self, key):
		return self.__db[key]

	def __loadDb(self, storyname):

		with open("Download_watson_info/durations/%s_onomatopoeia_ssml.yml" % storyname) as f:
			self.__db = yaml.load(f)

	def selectKeywordFromSentence(self, sentence, word_type):
		'''
		Given an AnnotatedSentence, it returns the selected AnnotatedKeyword decided by occurrences inverse probability. 

		sentence : AnnotatedSentence
			AnnotatedSentence to find keywords

		word_type : str
			A string with value "movement" or "led" indicating if the keywords corresponds to a movement or a led colour. 
		'''


		if word_type == "movement": 
			movements_db = MovementDicts().getDb()
			keywords = movements_db.keys()

		elif word_type == "led":
			led_db = LEDsDicts().getDict()
			keywords = led_db.keys()
		


		annotated_keywords = [keyword for keyword in sentence.keywords if keyword.lemma in keywords]

		print("%s keywords: %s" % (word_type, keywords))
		print("Keywords in sentence: %s" % [word.lemma for word in sentence.keywords])
		print("Annotated keywords: %s" % annotated_keywords)

		if annotated_keywords:
			return self.__selectWord(annotated_keywords)
		else:
			return -1

		
		
		

	# TODO: modify this function
	def modifySpeechWithEmotion(self, input_filename, output_filename, emotion, intensity):
		'''
		Modifies the pitch and speed of an audio according to the compound score

		Parameters
		----------
		input_filename : string
			The path where the audio he audio filefile is

		output_filename : string
			The filename of the wav file

		emotion: string
			The string corresponding to the emotion

		intensity : float
			The intensity value of the emotion

		Returns
		-------

		A tuple with the audio in a numpy.ndarray and the sample rate

		'''
		# TODO: Convert valence and arousal to a single value to perform the range conversion
		# Define max and min pitch [-300, 100] and tempo [0.8-1.2]values for each emotion

		neutral_max_pitch_shift = -5 # Change this
		neutral_min_pitch_shift = 5 # Change this
		neutral_max_tempo = 0.95 # Change this
		neutral_min_tempo = 1.05 # Change this

		calm_max_pitch_shift = -5 # Change this
		calm_min_pitch_shift = 5 # Change this
		calm_max_tempo = 0.95 # Change this
		calm_min_tempo = 1.05 # Change this
		
		happy_max_pitch_shift = 90 # Change this
		happy_min_pitch_shift = 100 # Change this
		happy_max_tempo = 1.10 # Change this
		happy_min_tempo = 1.20 # Change this

		sad_max_pitch_shift = -250 # Change this
		sad_min_pitch_shift = -200 # Change this
		sad_max_tempo = 0.8 # Change this
		sad_min_tempo = 0.95 # Change this

		angry_max_pitch_shift = -150 # Change this
		angry_min_pitch_shift = -95 # Change this
		angry_max_tempo = 0.95 # Change this
		angry_min_tempo = 1.10 # Change this

		fear_max_pitch_shift = -50 # Change this
		fear_min_pitch_shift = -20 # Change this
		fear_max_tempo = 0.95 # Change this
		fear_min_tempo = 1.05 # Change this

		disgust_max_pitch_shift = -150 # Change this
		disgust_min_pitch_shift = -100 # Change this
		disgust_max_tempo = 0.8 # Change this
		disgust_min_tempo = 0.95 # Change this

		surprise_max_pitch_shift =70 # Change this
		surprise_min_pitch_shift = 90 # Change this
		surprise_max_tempo = 0.95 # Change this
		surprise_min_tempo = 1.10 # Change this



		if emotion == "neutral":
			pitch_shift = rangeConversion(0.0, 1.0, neutral_min_pitch_shift, neutral_max_pitch_shift, intensity)
			tempo = rangeConversion(0.0, 1.0, neutral_min_tempo, neutral_max_tempo, intensity)

		elif emotion == "happy":
			pitch_shift = rangeConversion(0.0, 1.0, happy_min_pitch_shift, happy_max_pitch_shift, intensity)
			tempo = rangeConversion(0.0, 1.0, happy_min_tempo, happy_max_tempo, intensity)
		
		elif emotion == "calm":
			pitch_shift = rangeConversion(0.0, 1.0, calm_min_pitch_shift, calm_max_pitch_shift, intensity)
			tempo = rangeConversion(0.0, 1.0, calm_min_tempo, calm_max_tempo, intensity)
		
		elif emotion == "sad":
			pitch_shift = rangeConversion(0.0, 1.0, sad_min_pitch_shift, sad_max_pitch_shift, intensity)
			tempo = rangeConversion(0.0, 1.0, sad_min_tempo, sad_max_tempo, intensity)
		
		elif emotion == "anger":
			pitch_shift = rangeConversion(0.0, 1.0, angry_min_pitch_shift, angry_max_pitch_shift, intensity)
			tempo = rangeConversion(0.0, 1.0, angry_min_tempo, angry_max_tempo, intensity)
		
		elif emotion == "fear":
			pitch_shift = rangeConversion(0.0, 1.0, fear_min_pitch_shift, fear_max_pitch_shift, intensity)
			tempo = rangeConversion(0.0, 1.0, fear_min_tempo, fear_max_tempo, intensity)
		
		elif emotion == "disgust":
			pitch_shift = rangeConversion(0.0, 1.0, disgust_min_pitch_shift, disgust_max_pitch_shift, intensity)
			tempo = rangeConversion(0.0, 1.0, disgust_min_tempo, disgust_max_tempo, intensity)
		
		elif emotion == "surprised":
			pitch_shift = rangeConversion(0.0, 1.0, surprise_min_pitch_shift, surprise_max_pitch_shift, intensity)
			tempo = rangeConversion(0.0, 1.0, surprise_min_tempo, surprise_max_tempo, intensity)
		
	


		with open(os.devnull, 'wb') as devnull:
			subprocess.check_call(["sox", input_filename, output_filename, 'pitch', str(pitch_shift), 'tempo', str(tempo)], stdout=devnull, stderr=subprocess.STDOUT)

		return tempo
		

	def getDuration(self, filename):
		# Get audio duration
		output = subprocess.check_output(['mediainfo', '--Inform=Audio;%Duration/String3%', 'Download_watson_info/modified_audio/%s' % filename])
		# Remove \n
		output = output.rstrip("\n")
		# Split output into hh:mm:ss.msms
		output = output.split(":")
		duration = int(output[0])*3600 + int(output[1])*60 + float(output[2])
		return duration

	def getDurationAndWords(self, text, filename, movement_keywords, led_keywords):
		'''
		Method to load previously generated speech and recognize words in the speech. 

		Parameters
		----------

		text : string
			Text to find

		filename : string
			Name without extension of the audio and yaml files. Both audio and yaml have the same name

		movement_keywords : list
			All the keywords that have a rule based movement

		led_keywords : list
			All the keywords that have a rule based led modification
		
		Returns
		-------

		keywords_in_file : list
			List of lists being each element a word with beginning and end times. Example: confused,1.28,2.9,3.8,6.4;I,6.9,8.2;
		'''

		# Get audio duration
		output = subprocess.check_output(['mediainfo', '--Inform=Audio;%Duration/String3%', 'modified_audio/%s.wav' % filename])
		# Remove \n
		output = output.rstrip("\n")
		# Split output into hh:mm:ss.msms
		output = output.split(":")
		duration = int(output[0])*3600 + int(output[1])*60 + float(output[2])

		# Find words in sentence
		words_in_sentence = [word for word in movement_keywords if re.search(r'\b' + word.lower() + r'\b', text.lower())]
		led_words_in_sentence = [word for word in led_keywords if re.search(r'\b' + word.lower() + r'\b', text.lower())]
		# print("All led words in sentence: %s" % str(led_words_in_sentence))

		if words_in_sentence:
			# Load words times
			a = "../downloaded_times/%s.yml" % (filename)
			with open(a) as f:
				dict_output = yaml.load(f)

			output = ""
			for found_word in dict_output["results"][0]["keywords_result"]:
				output += str(found_word)
				for occurrence in dict_output["results"][0]["keywords_result"][str(found_word)]:
					output += "," + str(occurrence["start_time"]) + "," + str(occurrence["end_time"])
				output += ";"

			# Convert string in list of lists. [:-1] is to remove the last element generated when doing split with the last ;
			words_in_speech = [w.split(",") for w in output.split(";")[:-1]]
		else:
			words_in_speech = []


		if led_words_in_sentence:
			# Load words times
			a = "../downloaded_times/%s.yml" % (filename)
			with open(a) as f:
				dict_output = yaml.load(f)

			output = ""
			for found_word in dict_output["results"][0]["keywords_result"]:
				if found_word in led_words_in_sentence:
					output += str(found_word)
					for occurrence in dict_output["results"][0]["keywords_result"][str(found_word)]:
						output += "," + str(occurrence["start_time"]) + "," + str(occurrence["end_time"])
					output += ";"

			# Convert string in list of lists. [:-1] is to remove the last element generated when doing split with the last ;
			led_words_in_speech = [w.split(",") for w in output.split(";")[:-1]]
		else:
			led_words_in_speech = []

			# words_in_speech = speech.recognizeWordsInSpeech(rb.keywords, filename)

		return duration, words_in_speech, words_in_sentence, led_words_in_speech, led_words_in_sentence

	def modifyPitch(self, audio, sr, steps):
		'''
		Modifies the pitch of an audio using rubberband

		Parameters
		----------

		audio : numpy.ndarray
			A one or two-dimensional (frames x channels) numpy array.

		sr : int
			The sample rate of the audio file

		steps : float
			The number of semitones to low or rise. 
			steps > 0 raises "steps" semitones
			steps < 0 lowen "steps" semitones
		'''
		return pyrb.pitch_shift(audio, sr, n_steps=steps)

	def modifySpeed(self, audio, sr, gain):
		'''
		Modifies the speed of an audio using rubberband

		Parameters
		----------

		audio : numpy.ndarray
			A one or two-dimensional (frames x channels) numpy array.

		sr : int
			The sample rate of the audio file

		gain : float
			The speed gain to be applied, gain > 1 to speed up and gain < 1 to slow down. 
			If current duration is 10s, with a 0.1 gain, the new duration will be 100s (*10)
			If current duration is 10s, with a 2 gain, the new duration will be 5s (/2)

		'''

		return pyrb.time_stretch(audio, sr, gain)

	def save(self, path, filename, audio, sr):
		'''
		Save the audio in a numpy.ndarray to wav file

		Parameters
		----------
		
		path : str
			The path to save the file

		filename : str
			The filename to save

		audio : numpy.ndarray
			numpy.ndarray containing the audio
		
		sr : int
			The sample rate of the audio file
		'''
		full_path = path + filename 
		sf.write(full_path, audio, sr)

	def getDurations(self, storyname):
		'''
		Get the duration of all the audio files given the base name of all files

		Parameters
		----------
		storyname : str
			The name of the story. It is the substring that all the audio files of the selected story contain. 

		Returns
		-------

		A list with the time of all the files. The order is not guaranteed
		'''

		durations = []
		for file in glob.glob("Download_watson_info/audio/"+storyname+"*"):
			# Get audio duration
			# cmd_sh = 'mediainfo --Inform="Audio;%Duration/String3%" ' + file
			output = subprocess.check_output(['mediainfo', '--Inform=Audio;%Duration/String3%', file])
			# output = os.popen(cmd_sh).read()
			# Remove \n
			output = output.rstrip("\n")
			# Split output into hh:mm:ss.msms
			output = output.split(":")
			duration = int(output[0])*3600 + int(output[1])*60 + float(output[2])
			durations.append(duration)
		return durations


	# def getKeywordFromText(self, text, keywords_to_find, keywords_in_sentence):

	# 	# Find words in sentence
	# 	# print(keywords_in_sentence)
	# 	found_words = [word.lemma for word in keywords_in_sentence if re.search(r'\b' + word.lemma.lower() + r'\b', text.lower()) and word.lemma.lower() in keywords_to_find]

	# 	if found_words:
	# 		selected_keyword = self.__selectWord(found_words)
	# 		self.__update_word_occurrence(selected_keyword)

	# 		all_lemmas = [word.lemma for word in keywords_in_sentence]
	# 		keyword_index = all_lemmas.index(selected_keyword)
			
	# 		time_index = random.choice(range(len(keywords_in_sentence[keyword_index].start_times)))
	# 		start_time = keywords_in_sentence[keyword_index].start_times[time_index]
	# 		end_time = keywords_in_sentence[keyword_index].end_times[time_index]

	# 		return selected_keyword, start_time, end_time
	# 	else:
	# 		return -1, -1, -1

	def getKeywordFromText(self, annotatedSentence):

		# Find words in sentence
		# print(keywords_in_sentence)

		text = annotatedSentence.text
		keywords_in_sentence = annotatedSentence.keywords

		# found_words = [word.lemma for word in keywords_in_sentence if re.search(r'\b' + word.lemma.lower() + r'\b', text.lower())]
		# if found_words:
		
		selected_keyword, start_time, end_time = self.__selectWord(annotatedSentence)
		print("Start time type: ", type(start_time))

		# self.__update_word_occurrence(selected_keyword)

		# all_lemmas = [word.lemma for word in keywords_in_sentence]
		# keyword_index = all_lemmas.index(selected_keyword)
		
		# time_index = random.choice(range(len(keywords_in_sentence[keyword_index].start_times)))
		# start_time = keywords_in_sentence[keyword_index].start_times[time_index]
		# end_time = keywords_in_sentence[keyword_index].end_times[time_index]

		return selected_keyword, start_time, end_time
		# else:
		# 	return -1, -1, -1



	def __loadAudio(self, storyname, i):
		
		if self.__storyname != storyname:
			self.__loadDb(storyname)
			self.__storyname = storyname

		return self.__getDuration("sentence_%d" % i)

	def getSentenceDuration(self, storyname, sentence_key):
		filename, duration = self.__loadAudio(storyname, sentence_key)
		return filename, duration