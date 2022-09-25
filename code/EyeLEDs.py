import random
from RuleBasedMovements import Lemmatizer


class PepperLEDs():
	'''
	Class to control the color of the LEDs on Pepper

	Parameters
	----------

	session : Naoqi Session
		The qi session object
	led_dict : dict
		Dictionary containing the corresponding color for each keyword. Keyword : color

	Methods
	-------
	setProportion(proportion = 1.0)
		Sets the proportion of the compound score
	
	earsOff()
		Turn the ears LEDs off
	
	eyesOff()
		Turn the eyes LEDs off

	eyesOn()
		Turn the eyes LEDs on
	
	fade(color)
		Changes the color of the eyes and chest given a color name

	setColor(color)
		Set the color of the eyes and chest given a color name. "Off" color is also accepted

	findColor(keyword)
		Given a keyword, finds the corresponding color

	getWordPosition(keyword)
		Method to find the exact time when a keyword appears
	'''

	def __init__(self, session):
		self.led_service = session.service("ALLeds")
		
		__dict_loader = LEDsDicts()
		self.__led_dict = __dict_loader.getDict()
		self.proportion = 1.0
		self.used_movements = {}

		names = ["FaceLeds", "ChestLeds"]
		self.led_service.createGroup("EyesAndChest",names)
		# Switch the new group on
		self.led_service.on("EyesAndChest")
		self.__earsOff()

	def setProportion(self, proportion = 1.0):
		'''
		Sets the proportion of the compound score

		Parameters
		----------

		proportion : float
			The gain obtained from the compound score
		'''
		self.proportion = proportion

	def __earsOff(self):
		'''
		Turn the ears LEDs off
		'''
		name = "EarLeds"
		self.led_service.off(name)

	def eyesOff(self):
		'''
		Turn pepper's eyes LEDs off
		'''
		name = "EyesAndChest"
		self.led_service.off(name)
	def eyesOn(self):
		'''
		Turn pepper's eyes LEDs on
		'''
		name = "EyesAndChest"
		self.led_service.on(name)

	def fade(self, r, g, b):
		'''
		Changes the color of the eyes and chest given a color name

		Parameters
		----------
		color : str
			The name of the color to fade to. Color must be one of the following values: white, red, green, blue, yellow, magenta, cyan
		
		'''
		
		name = "EyesAndChest"
		duration = 1.0
		self.led_service.fadeRGB(name, r, g, b, duration)

	def __setColor(self, r, g, b):
		'''
		Changes the color of the eyes and chest given a color name. "Off" color is also accepted
		
		Parameters
		----------
		color : str
			The name of the color. Accepted colors: white, red, green, blue, yellow, magenta, cyan, off
		'''
		self.fade(r, g, b)
	
	def __findColor(self, keyword):
		'''
		Given a keyword, finds the corresponding color

		Parameters
		----------
		keyword : str
			The keyword to find
		'''
		color = self.__led_dict.get(keyword, -1)
		assert(color != -1), 'Color for keyword "%s" does not exist.' % keyword
		return color[0], color[1], color[2]

	def setLEDByEmotion(self, keyword):
		'''
		Finds the corresponding eye color to a keyword.
		Parameters
		----------
		keyword : string
			The keyword to find in movements database
		Returns
		-------
		movement : list
			List of lists containing the joint names, keys and times of the movement if exists, else -1
		'''
		
		print("LED Keyword: %s" % keyword)
		r, g, b = self.__findColor(keyword)
		self.__setColor(r, g, b)
		# print("MOVEMENT: %d", movement)
		# assert(movement != -1), 'Movement for keyword "%s" does not exist.' % keyword
		# return random.choice(movement)()


class LEDsDicts():
	'''
	Class containing dictionaries with word-color correspondence

	Methods
	-------

	getDict()
		Returns the default dictionary
	'''

	def __init__(self):
		
		self.__led_emotions = {
				"neutral" : (1.0, 1.0, 1.0),
				"calm" : (1.0, 1.0, 1.0),
				"happy" : (1.0, 1.0, 0.0), 
				"sad" : (0.0, 0.0, 1.0), 
				"surprised" : (0.4, 0.7, 1.0), 
				"fear" : (0.0, 1.0, 0.0),
				"disgust" : (0.7, 0.4, 1.0), # Change ro 
				"anger" : (1.0, 0.0, 0.0)}

	def getDict(self):
		return self.__led_emotions
