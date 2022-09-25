from textblob import TextBlob
from utils import rangeConversion
class SentimentAnalyzer():
	'''
	Class to get information about text sentiment

	Methods
	-------

	getEmotion(text, gain = 1.0)
		Method to extract the emotion and intensity of a text
	'''

	def getEmotion(self, text, gain = 1.0):
		'''
		Method to extract the emotion and intensity of a text

		Parameters
		----------
		text : str
			The text to be analyzed

		gain : float
			The value of gain to apply to the intensity

		Return
		------
		emotion : str
			The name of the emotion
		intensity : float
			The intensity of the emotion
		'''
		# TODO: add support for emotions
		text = text.replace("?", "")
		text = text.replace("!", "")
		blb = TextBlob(text)
		return "emotion", map(lambda x: x * gain, [sentence.sentiment.polarity for sentence in blb.sentences])


class EmotionByBodyLanguage():

	def __init__(self):

		self.__HEAD_PITCH = 1
		self.__HIP_PITCH = 15

		# self.__HIP_PITCH_MIN = -0.44 
		# self.__HIP_PITCH_MAX = 0.03
		# self.__HEAD_PITCH_MIN = 0.44
		# self.__HEAD_PITCH_MAX = -0.44

		# self.__MAX_PROPORION = 1.2
		# self.__MIN_PROPORTION = 0.8


		self.__emotionBL = {
			"happy" : {"HIP_PITCH_MIN" : 0.0, "HIP_PITCH_MAX" : 0.03, "HEAD_PITCH_MIN" : 0.0, "HEAD_PITCH_MAX" : -0.34}, # "HEAD_PITCH_MAX" : -0.44  
			"sad" : {"HIP_PITCH_MIN" : -0.44, "HIP_PITCH_MAX" : 0.0, "HEAD_PITCH_MIN" : 0.44, "HEAD_PITCH_MAX" : 0.0},
			"anger" : {"HIP_PITCH_MIN" : 0.0, "HIP_PITCH_MAX" : 0.0, "HEAD_PITCH_MIN" : 0.0, "HEAD_PITCH_MAX" : -0.34}, # "HEAD_PITCH_MAX" : -0.44
			"fear" : {"HIP_PITCH_MIN" : -0.22, "HIP_PITCH_MAX" : 0.0, "HEAD_PITCH_MIN" : 0.22, "HEAD_PITCH_MAX" : 0.0},
			"surprised" : {"HIP_PITCH_MIN" : 0.0, "HIP_PITCH_MAX" : 0.0, "HEAD_PITCH_MIN" : 0.0, "HEAD_PITCH_MAX" : 0.22},
			"disgust" : {"HIP_PITCH_MIN" : -0.44, "HIP_PITCH_MAX" : 0.0, "HEAD_PITCH_MIN" : 0.44, "HEAD_PITCH_MAX" : 0.0},
			"neutral" : {"HIP_PITCH_MIN" : 0.0, "HIP_PITCH_MAX" : 0.0, "HEAD_PITCH_MIN" : 0.0, "HEAD_PITCH_MAX" : 0.0},
			"calm" : {"HIP_PITCH_MIN" : 0.0, "HIP_PITCH_MAX" : 0.0, "HEAD_PITCH_MIN" : 0.0, "HEAD_PITCH_MAX" : 0.0}
		}

	def modifyBodyLanguageByEmotion(self, movement, emotion, intensity):
		
		movement_times, movement_keys, movement_values = movement

		head_pitch_min = self.__emotionBL[emotion]["HEAD_PITCH_MIN"]
		head_pitch_max = self.__emotionBL[emotion]["HEAD_PITCH_MAX"]
		hip_pitch_min = self.__emotionBL[emotion]["HIP_PITCH_MIN"]
		hip_pitch_max = self.__emotionBL[emotion]["HIP_PITCH_MAX"]

		headp = rangeConversion(0.0, 1.0, head_pitch_min, head_pitch_max, intensity)
		movement_keys[self.__HEAD_PITCH] = [headp for _ in movement_keys[self.__HEAD_PITCH]]

		hipp = rangeConversion(0.0, 1.0, hip_pitch_min, hip_pitch_max, intensity)
		movement_keys[self.__HIP_PITCH] = [hipp for _ in movement_keys[self.__HIP_PITCH]]

		return [movement_times, movement_keys, movement_values]


class Emotion():
	def __init__(self):

		self.__INTENSITY_MAX = 1.0
		self.__INTENSITY_MIN = 0.0

		self.__pitchValues = {
			"happy" : [10, 25], # 1 
			"sad" : [-10, -20], # 5
			"anger" : [-10, 0], # 4
			"fear" : [10, 20], # 3
			"surprised" : [15, 30], # 2.0
			"disgust" : [-10, -30], # 6
			"neutral" : [-5, 5],
			"calm" : [-5, 5]
		}

		self.__speedValues = {
			"happy" : [0, 10], # 1 
			"sad" : [0, -20], # 5
			"anger" : [5, 10], # 4
			"fear" : [-10, -30], # 3
			"surprised" : [0, 10], # 2.0
			"disgust" : [-10, -20], # 6
			"neutral" : [-5, 5],
			"calm" : [-5, 5]
		}

	def __pitchFromEmotion(self, emotion, intensity):
		
		min_pitch, max_pitch = self.__pitchValues[emotion]
		return rangeConversion(self.__INTENSITY_MIN, self.__INTENSITY_MAX, min_pitch, max_pitch, intensity)

	def __speedFromEmotion(self, emotion, intensity):
		
		min_speed, max_speed = self.__speedValues[emotion]
		return rangeConversion(self.__INTENSITY_MIN, self.__INTENSITY_MAX, min_speed, max_speed, intensity)

	def voiceParametersFromEmotion(self, emotion, intensity):
		return self.__pitchFromEmotion(emotion, intensity), self.__speedFromEmotion(emotion, intensity)
	