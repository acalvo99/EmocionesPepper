from platform import processor
import random
# import stanza
# import stanfordnlp
from RuleBasedMovements import Lemmatizer


class MovementDicts():

	def __init__(self):
		
		self.__movements = {"separate": [RuleBasedMovements.separate_1, RuleBasedMovements.separate_2],
							"crying": [RuleBasedMovements.cry_1, RuleBasedMovements.cry_2],
							"hidden": [RuleBasedMovements.hide_1, RuleBasedMovements.fearful_1, RuleBasedMovements.hide_1],
							"courage": [RuleBasedMovements.courage],
							"head": [RuleBasedMovements.body_talk_13],
							"mouth": [RuleBasedMovements.body_talk_13],
							"think": [RuleBasedMovements.touch_head_4, RuleBasedMovements.scratch_head_1],
							"no": [RuleBasedMovements.angry_3, RuleBasedMovements.no_1, RuleBasedMovements.no_2, RuleBasedMovements.no_3, RuleBasedMovements.no_8, RuleBasedMovements.no_9],
							"not": [RuleBasedMovements.angry_3, RuleBasedMovements.no_1, RuleBasedMovements.no_2, RuleBasedMovements.no_3, RuleBasedMovements.no_8, RuleBasedMovements.no_9],
							#   "knocking the door" : [RuleBasedMovements.angry_4],
							"knock knock": [RuleBasedMovements.angry_4],
							"tired": [RuleBasedMovements.bored_1],
							"scared": [RuleBasedMovements.fearful_1],
							"sweating": [RuleBasedMovements.relieved_1],
							#   "kiss" : [RuleBasedMovements.kisses_1],
							"I": [RuleBasedMovements.me_1, RuleBasedMovements.me_2],
							"strong deception": [RuleBasedMovements.strong_deception],
							"closed my eyes": [RuleBasedMovements.close_eyes],
							"open my eyes": [RuleBasedMovements.open_eyes],
							"celebrate": [RuleBasedMovements.applause],
							"rejected": [RuleBasedMovements.rejected],
							"confused": [RuleBasedMovements.confused],
							"Hello": [RuleBasedMovements.Hey_3, RuleBasedMovements.Hey_4],
							"energy": [RuleBasedMovements.ShowMuscles_1, RuleBasedMovements.ShowMuscles_4],
							"listen": [RuleBasedMovements.Listen_1],
							"me": [RuleBasedMovements.Me_1, RuleBasedMovements.Me_8],
							"not understand": [RuleBasedMovements.IDontKnow_4, RuleBasedMovements.No_8],
							"plenty": [RuleBasedMovements.Plenty_1],
							"spheres": [RuleBasedMovements.Sphere_1],
							"come": [RuleBasedMovements.ComeOn_],
							"I": [RuleBasedMovements.me_1, RuleBasedMovements.me_2],
							"hide": [RuleBasedMovements.hide_1, RuleBasedMovements.fearful_1, RuleBasedMovements.hide_1],
							"cry": [RuleBasedMovements.cry_1, RuleBasedMovements.cry_2, RuleBasedMovements.CryMotionCorrected],
							"tear": [RuleBasedMovements.cry_1, RuleBasedMovements.cry_2, RuleBasedMovements.CryMotionCorrected],
							"child" : [RuleBasedMovements.BabyMotion],
							"dance" : [RuleBasedMovements.DanceAgMotion],
							"beg" : [RuleBasedMovements.BegMotion],
							"large" : [RuleBasedMovements.BigAgMotion],
							"grand" : [RuleBasedMovements.BigAgMotion],
							"big" : [RuleBasedMovements.BigAgMotion],
							"giant" : [RuleBasedMovements.BigAgMotion],
							"ago" : [RuleBasedMovements.AgoMotion],
							"remember" : [RuleBasedMovements.RememberMotion],
							"shout" : [RuleBasedMovements.ShoutMotion],
							"run" : [RuleBasedMovements.RunMotion],
							"heard" : [RuleBasedMovements.ListenAgMotion]
							}

		# self.__nlp = stanfordnlp.PipeLine(lang="en", processors="tokenize,lemma")

		self.__lemmatizeMovementKeywords()

	def __lemmatizeMovementKeywords(self):
		lemmatizer = Lemmatizer()
		for keyword in list(self.__movements):
			self.__movements[lemmatizer.lemmatize(
				keyword)] = self.__movements.pop(keyword)

	# def __lemmatize(self, keyword):
	# 	doc = self.__nlp(keyword)
	# 	lemma = doc.sentences[0].words[0].lemma
	# 	return lemma

	# def __getWordInfo(self, keyword, filename):

	# 	# Load words times
	# 	a = "../downloaded_times/%s.yml" % (filename)
	# 	with open(a) as f:
	# 		dict_output = yaml.load(f)

	# 	output = ""
	# 	for found_word in dict_output["results"][0]["keywords_result"]:
	# 		if found_word == keyword:
	# 			output += str(found_word)
	# 			for occurrence in dict_output["results"][0]["keywords_result"][str(found_word)]:
	# 				output += "," + str(occurrence["start_time"]) + "," + str(occurrence["end_time"])
	# 			output += ";"
	# 			break

	# 	# Convert string in list of lists. [:-1] is to remove the last element generated when doing split with the last ;
	# 	word_info = [w.split(",") for w in output.split(";")[:-1]]

	# 	print("Word info: %s" % word_info)
	# 	return word_info

	def getMovement(self, keyword):
		# print("Keyword: %s" % keyword)
		movement = self.__movements.get(keyword, -1)
		# TODO: instead of random movement, implement occurrence inverse proportional
		if movement != -1:
			return random.choice(movement)()
		else:
			return -1

	def getDb(self):
		return self.__movements


class GlobalGestures():

	def __init__(self):
		self.initializeGlobalGestures()

	def getMotion(self, motion):
		if motion == "InitPostureArms":
			names = self.namesInitPostureArms
			keys = self.keysInitPostureArms
			times = self.timesInitPostureArms
		elif motion == "InitPosture":
			names = self.namesInitPosture
			keys = self.keysInitPosture
			times = self.timesInitPosture
		elif motion == "InitPosture17":
			names = self.namesInitPosture17
			keys = self.keysInitPosture17
			times = self.timesInitPosture17
		return [names, keys, times]

	def initializeGlobalGestures(self):
		self.initializeInitPostureArms()
		self.initializeInitPosture()
		self.initPosture17()

	def initializeInitPostureArms(self):
		self.namesInitPostureArms = list()
		self.timesInitPostureArms = list()
		self.keysInitPostureArms = list()

		self.namesInitPostureArms.append("LElbowRoll")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([-0.52002])

		self.namesInitPostureArms.append("LElbowYaw")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([-1.22718])

		self.namesInitPostureArms.append("LHand")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([0.584359])

		self.namesInitPostureArms.append("LShoulderPitch")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([1.55852])

		self.namesInitPostureArms.append("LShoulderRoll")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([0.145728])

		self.namesInitPostureArms.append("LWristYaw")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([0.0352399])

		self.namesInitPostureArms.append("RElbowRoll")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([0.529223])

		self.namesInitPostureArms.append("RElbowYaw")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([1.22412])

		self.namesInitPostureArms.append("RHand")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([0.608084])

		self.namesInitPostureArms.append("RShoulderPitch")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([1.55546])

		self.namesInitPostureArms.append("RShoulderRoll")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([-0.141126])

		self.namesInitPostureArms.append("RWristYaw")
		self.timesInitPostureArms.append([1.56])
		self.keysInitPostureArms.append([0.0229681])

	def initializeInitPosture(self):
		self.namesInitPosture = list()
		self.timesInitPosture = list()
		self.keysInitPosture = list()

		self.namesInitPosture.append("HeadPitch")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([-0.268447])

		self.namesInitPosture.append("HeadYaw")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([0.0276117])

		self.namesInitPosture.append("LElbowRoll")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([-0.521554])

		self.namesInitPosture.append("LElbowYaw")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([-1.23179])

		self.namesInitPosture.append("LHand")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([0.586995])

		self.namesInitPosture.append("LShoulderPitch")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([1.55392])

		self.namesInitPosture.append("LShoulderRoll")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([0.148796])

		self.namesInitPosture.append("LWristYaw")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([0.0214341])

		self.namesInitPosture.append("RElbowRoll")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([0.529223])

		self.namesInitPosture.append("RElbowYaw")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([1.21798])

		self.namesInitPosture.append("RHand")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([0.594903])

		self.namesInitPosture.append("RShoulderPitch")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([1.56313])

		self.namesInitPosture.append("RShoulderRoll")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([-0.147262])

		self.namesInitPosture.append("RWristYaw")
		self.timesInitPosture.append([0.96])
		self.keysInitPosture.append([0.053648])

	def initPosture17(self):
		self.namesInitPosture17 = list()
		self.timesInitPosture17 = list()
		self.keysInitPosture17 = list()

		self.namesInitPosture17.append("HeadPitch")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([-0.262569])

		self.namesInitPosture17.append("HeadYaw")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([0.0303817])

		self.namesInitPosture17.append("HipPitch")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([-0.00315644])

		self.namesInitPosture17.append("HipRoll")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([-0.00124297])

		self.namesInitPosture17.append("KneePitch")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([-0.00663467])

		self.namesInitPosture17.append("LElbowRoll")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([-0.530135])

		self.namesInitPosture17.append("LElbowYaw")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([-1.22458])

		self.namesInitPosture17.append("LHand")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([0.584231])

		self.namesInitPosture17.append("LShoulderPitch")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([1.54812])

		self.namesInitPosture17.append("LShoulderRoll")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([0.157489])

		self.namesInitPosture17.append("LWristYaw")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([0.0189414])

		self.namesInitPosture17.append("RElbowRoll")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([0.537722])

		self.namesInitPosture17.append("RElbowYaw")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([1.20863])

		self.namesInitPosture17.append("RHand")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([0.591992])

		self.namesInitPosture17.append("RShoulderPitch")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([1.56049])

		self.namesInitPosture17.append("RShoulderRoll")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([-0.157033])

		self.namesInitPosture17.append("RWristYaw")
		self.timesInitPosture17.append([0.0])
		self.keysInitPosture17.append([0.0624451])


class RuleBasedMovements():

	@staticmethod
	def separate_1():
		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.96, 1.96, 2.96])
		keys.append([-1.08734, -0.71733, -0.520108])

		names.append("LElbowYaw")
		times.append([0.96, 1.96, 2.96])
		keys.append([-0.446804, -0.446804, -1.213])

		names.append("LHand")
		times.append([0.96, 1.96])
		keys.append([0.6, 0.6])

		names.append("LShoulderPitch")
		times.append([0.96, 1.96, 2.96])
		keys.append([0.720821, 0.720821, 1.55509])

		names.append("LShoulderRoll")
		times.append([0.96, 1.96, 2.96])
		keys.append([0.141372, 0.486947, 0.136136])

		names.append("LWristYaw")
		times.append([0.96, 1.96, 2.96])
		keys.append([1.52367, 1.52367, 0.0122173])

		names.append("RElbowRoll")
		times.append([0.96, 1.96, 2.96])
		keys.append([1.08734, 0.71733, 0.520108])

		names.append("RElbowYaw")
		times.append([0.96, 1.96, 2.96])
		keys.append([0.446804, 0.446804, 1.213])

		names.append("RHand")
		times.append([0.96, 1.96])
		keys.append([0.6, 0.6])

		names.append("RShoulderPitch")
		times.append([0.96, 1.96, 2.96])
		keys.append([0.720821, 0.720821, 1.55509])

		names.append("RShoulderRoll")
		times.append([0.96, 1.96, 2.96])
		keys.append([0.141372, -0.486947, -0.136136])

		names.append("RWristYaw")
		times.append([0.96, 1.96, 2.96])
		keys.append([-1.52367, -1.52367, -0.0122173])

		return [names, keys, times]

	@staticmethod
	def separate_2():
		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.96, 1.96, 2.96])
		keys.append([-1.08734, -0.0760117, -0.520108])

		names.append("LElbowYaw")
		times.append([0.96, 1.96, 2.96])
		keys.append([-0.446804, -0.446804, -1.213])

		names.append("LHand")
		times.append([0.96, 1.96])
		keys.append([0.6, 0.6])

		names.append("LShoulderPitch")
		times.append([0.96, 1.96, 2.96])
		keys.append([0.720821, 0.720821, 1.55509])

		names.append("LShoulderRoll")
		times.append([0.96, 1.96, 2.96])
		keys.append([0.141372, 0.141372, 0.136136])

		names.append("LWristYaw")
		times.append([0.96, 1.96, 2.96])
		keys.append([1.52367, 1.52367, 0.0122173])

		names.append("RElbowRoll")
		times.append([0.96, 1.96, 2.96])
		keys.append([1.08734, 0.0760117, 0.520108])

		names.append("RElbowYaw")
		times.append([0.96, 1.96, 2.96])
		keys.append([0.446804, 0.446804, 1.213])

		names.append("RHand")
		times.append([0.96, 1.96])
		keys.append([0.6, 0.6])

		names.append("RShoulderPitch")
		times.append([0.96, 1.96, 2.96])
		keys.append([0.720821, 0.720821, 1.55509])

		names.append("RShoulderRoll")
		times.append([0.96, 1.96, 2.96])
		keys.append([0.141372, 0.141372, -0.136136])

		names.append("RWristYaw")
		times.append([0.96, 1.96, 2.96])
		keys.append([-1.52367, -1.52367, -0.0122173])

		return [names, keys, times]

	@staticmethod
	def cry_1():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([0.445059, 0.445059, 0.445059,
					 0.445059, 0.445059, -0.139626])

		names.append("LElbowRoll")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([-1.14145, -1.14145, -1.14145, -
					 1.14145, -1.14145, -0.523599])

		names.append("LElbowYaw")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([-0.895354, -0.895354, -0.895354, -
					 0.895354, -0.895354, -1.25664])

		names.append("LHand")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([0.02, 0.02, 0.02, 0.02, 0.02, 0.59])

		names.append("LShoulderPitch")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([-0.020944, -0.020944, -0.020944, -
					 0.020944, -0.020944, 1.56381])

		names.append("LShoulderRoll")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([0.00872665, 0.00872665, 0.00872665,
					 0.00872665, 0.00872665, 0.123918])

		names.append("LWristYaw")
		times.append([0.96, 1.36, 1.68, 2, 2.32])
		keys.append([-0.00174533, -1.0472, 0, -1.0472, 0])

		names.append("RElbowRoll")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([1.14145, 1.14145, 1.14145, 1.14145, 1.14145, 0.523599])

		names.append("RElbowYaw")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([0.895354, 0.895354, 0.895354,
					 0.895354, 0.895354, 1.25664])

		names.append("RHand")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([0.02, 0.02, 0.02, 0.02, 0.02, 0.59])

		names.append("RShoulderPitch")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([-0.020944, -0.020944, -0.020944, -
					 0.020944, -0.020944, 1.56381])

		names.append("RShoulderRoll")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([-0.00872665, -0.00872665, -0.00872665, -
					 0.00872665, -0.00872665, -0.123918])

		names.append("RWristYaw")
		times.append([0.96, 1.36, 1.68, 2, 2.32])
		keys.append([0.00174533, 1.0472, 0, 1.0472, 0])

		return [names, keys, times]
	
	@staticmethod
	def cry_2():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([0.445059, 0.445059, 0.445059,
					 0.445059, 0.445059, -0.139626])

		names.append("HeadYaw")
		times.append([0.96, 1.36, 1.68, 2, 2.32])
		keys.append([-0.176278, -0.176278, -0.176278, -0.176278, -0.176278])

		names.append("LElbowRoll")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([-0.523599, -0.523599, -0.523599, -
					 0.523599, -0.523599, -0.523599])

		names.append("LElbowYaw")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([-1.25664, -1.25664, -1.25664, -
					 1.25664, -1.25664, -1.25664])

		names.append("LHand")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([0.58, 0.58, 0.58, 0.58, 0.58, 0.59])

		names.append("LShoulderPitch")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([1.56381, 1.56381, 1.56381, 1.56381, 1.56381, 1.56381])

		names.append("LShoulderRoll")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([0.125664, 0.125664, 0.125664,
					 0.125664, 0.125664, 0.123918])

		names.append("LWristYaw")
		times.append([0.96, 1.36, 1.68, 2, 2.32])
		keys.append([0, 0, 0, 0, 0])

		names.append("RElbowRoll")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([1.14145, 1.14145, 1.14145, 1.14145, 1.14145, 0.523599])

		names.append("RElbowYaw")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([0.895354, 0.895354, 0.895354,
					 0.895354, 0.895354, 1.25664])

		names.append("RHand")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([0.02, 0.02, 0.02, 0.02, 0.02, 0.59])

		names.append("RShoulderPitch")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([-0.020944, -0.020944, -0.020944, -
					 0.020944, -0.020944, 1.56381])

		names.append("RShoulderRoll")
		times.append([0.96, 1.36, 1.68, 2, 2.32, 2.96])
		keys.append([-0.00872665, -0.00872665, -0.00872665, -
					 0.00872665, -0.00872665, -0.123918])

		names.append("RWristYaw")
		times.append([0.96, 1.36, 1.68, 2, 2.32])
		keys.append([0.00174533, 1.0472, 0.00174533, 1.0472, 0.00174533])

		return [names, keys, times]

	@staticmethod
	def hide():
		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.96, 1.56, 2.36])
		keys.append([-1.56207, -1.56207, -0.539307])

		names.append("LElbowYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([-1.01578, -1.01578, -1.24617])

		names.append("LHand")
		times.append([0.96, 1.56, 2.36])
		keys.append([0.98, 0.98, 0.62])

		names.append("LShoulderPitch")
		times.append([0.96, 1.56, 2.36])
		keys.append([-0.0191986, -0.0191986, 1.61268])

		names.append("LWristYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([-1.44164, -1.44164, -0.0349066])

		names.append("RElbowRoll")
		times.append([0.96, 1.56, 2.36])
		keys.append([1.56207, 1.56207, 0.539307])

		names.append("RElbowYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([1.01578, 1.01578, 1.24617])

		names.append("RHand")
		times.append([0.96, 1.56, 2.36])
		keys.append([0.98, 0.98, 0.62])

		names.append("RShoulderPitch")
		times.append([0.96, 1.56, 2.36])
		keys.append([-0.0191986, -0.0191986, 1.61268])

		names.append("RWristYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([1.44164, 1.44164, 0.0349066])

		return [names, keys, times]

	@staticmethod
	def courage():
		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.96, 1.36, 1.76, 2.36])
		keys.append([-1.24442, -1.01404, -1.24442, -0.516617])

		names.append("LElbowYaw")
		times.append([0.96, 1.36, 1.76, 2.36])
		keys.append([-1.7017, -1.7017, -1.7017, -1.1781])

		names.append("LHand")
		times.append([0.96, 1.36, 1.76, 2.36])
		keys.append([0.02, 0.02, 0.02, 0.61])

		names.append("LShoulderRoll")
		times.append([0.96, 1.36, 1.76, 2.36])
		keys.append([0.319395, 0.319395, 0.319395, 0.162316])

		names.append("LWristYaw")
		times.append([0.96, 1.36, 1.76, 2.36])
		keys.append([-1.3282, -1.3282, -1.3282, -0.010472])

		names.append("RElbowRoll")
		times.append([0.96, 1.36, 1.76, 2.36])
		keys.append([1.24442, 1.01404, 1.24442, 0.516617])

		names.append("RElbowYaw")
		times.append([0.96, 1.36, 1.76, 2.36])
		keys.append([1.7017, 1.7017, 1.7017, 1.1781])

		names.append("RHand")
		times.append([0.96, 1.36, 1.76, 2.36])
		keys.append([0.02, 0.02, 0.02, 0.61])

		names.append("RShoulderRoll")
		times.append([0.96, 1.36, 1.76, 2.36])
		keys.append([-0.319395, -0.319395, -0.319395, -0.162316])

		names.append("RWristYaw")
		times.append([0.96, 1.36, 1.76, 2.36])
		keys.append([1.3282, 1.3282, 1.3282, 0.010472])

		return [names, keys, times]

	@staticmethod
	def body_talk_13():
		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([1.32, 1.96])
		keys.append([-0.397265, -0.314428])

		names.append("LElbowYaw")
		times.append([1.32, 1.96])
		keys.append([-0.678069, -0.68574])

		names.append("LHand")
		times.append([1.32, 1.96])
		keys.append([0.181818, 0.1836])

		names.append("LShoulderPitch")
		times.append([1.32, 1.96])
		keys.append([1.38056, 1.40664])

		names.append("LShoulderRoll")
		times.append([1.32, 1.96])
		keys.append([0.246933, 0.220854])

		names.append("LWristYaw")
		times.append([1.32, 1.96])
		keys.append([0, -0.01078])

		names.append("RElbowRoll")
		times.append([0.64, 1.24, 1.88])
		keys.append([0.729548, 1.55552, 1.54462])

		names.append("RElbowYaw")
		times.append([0.64, 1.24, 1.88])
		keys.append([1.63014, 1.10444, 1.02451])

		names.append("RHand")
		times.append([0.64, 1.24, 1.88])
		keys.append([0.84, 0.86, 0.77])

		names.append("RShoulderPitch")
		times.append([1.24, 1.88])
		keys.append([0.270025, 0.158825])

		names.append("RShoulderRoll")
		times.append([1.24, 1.88])
		keys.append([-0.2102, -0.179519])

		names.append("RWristYaw")
		times.append([0.64, 1.24, 1.88])
		keys.append([1.028, 1.13446, 1.13358])

		return [names, keys, times]
	
	@staticmethod
	def angry_3():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.28, 2.28])
		keys.append([-0.118772, -0.0802851])

		names.append("HeadYaw")
		times.append([0.68, 1.28, 2.28])
		keys.append([0.260054, -0.312414, -0.364774])

		names.append("HipPitch")
		times.append([1.16])
		# keys.append([-1.34714e-05])
		keys.append([0.0])

		names.append("HipRoll")
		times.append([1.16])
		# keys.append([-3.8576e-07])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([1.16])
		keys.append([-0.0698259])

		names.append("LElbowRoll")
		times.append([0.6, 1.2, 2.2])
		keys.append([-0.875873, -0.249582, -0.166535])

		names.append("LElbowYaw")
		times.append([0.6, 1.2, 2.2])
		keys.append([-0.79587, -2.08167, -2.08413])

		names.append("LHand")
		times.append([1.2, 2.2])
		keys.append([0.630909, 0.649189])

		names.append("LShoulderPitch")
		times.append([0.6, 1.2, 2.2])
		keys.append([1.28852, 1.66895, 1.74803])

		names.append("LShoulderRoll")
		times.append([0.6, 1.2, 2.2])
		keys.append([0.10821, 0.33437, 0.295484])

		names.append("LWristYaw")
		times.append([1.2, 2.2])
		keys.append([1.028, 1.01733])

		names.append("RElbowRoll")
		times.append([0.52, 1.12, 2.12])
		keys.append([0.42496, 0.564555, 0.553489])

		names.append("RElbowYaw")
		times.append([0.52, 1.12, 2.12])
		keys.append([1.58765, 1.21795, 1.24123])

		names.append("RHand")
		times.append([1.12, 2.12])
		keys.append([0.20548, 0.205067])

		names.append("RShoulderPitch")
		times.append([0.52, 1.12, 2.12])
		keys.append([1.68898, 1.53558, 1.54438])

		names.append("RShoulderRoll")
		times.append([0.52, 1.12, 2.12])
		keys.append([-0.099752, -0.136136, -0.136136])

		names.append("RWristYaw")
		times.append([1.12, 2.12])
		keys.append([0.0889301, 0.0906904])

		return [names, keys, times]

	@staticmethod
	def angry_4():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.6, 1.12, 1.84, 2.64])
		keys.append([-0.223402, -0.48233, -0.595845, -0.523599])

		names.append("HeadYaw")
		times.append([1.12, 1.84, 2.64])
		# keys.append([0.0536481, 0.052114, -7.60054e-07])
		keys.append([0.0536481, 0.052114, 0.0])

		names.append("HipPitch")
		times.append([1, 1.48, 2.52])
		# keys.append([0.150098, 0.150098, 9.56892e-07])
		keys.append([0.150098, 0.150098, 0.0])

		names.append("HipRoll")
		times.append([1.48, 2.52])
		# keys.append([-3.8576e-07, -8.226e-07])
		keys.append([0.0, 0.0])

		names.append("KneePitch")
		times.append([1, 1.48, 2.52])
		keys.append([-0.188496, -0.188496, -0.069809])

		names.append("LElbowRoll")
		times.append([0.52, 1.04, 1.28, 1.52, 1.76, 2, 2.56])
		keys.append([-0.657989, -1.5539, -0.952573, -
					 1.53396, -0.952573, -1.53396, -0.523457])

		names.append("LElbowYaw")
		times.append([0.52, 1.04, 1.28, 1.52, 1.76, 2, 2.56])
		keys.append([-1.51669, -1.40324, -1.2898, -
					 1.36485, -1.36485, -1.44164, -1.2217])

		names.append("LHand")
		times.append([1.04, 2.56])
		keys.append([0.121456, 0])

		names.append("LShoulderPitch")
		times.append([0.52, 1.04, 1.28, 1.52, 1.76, 2, 2.56])
		keys.append([0.467748, -0.10282, -0.101286, -
					 0.015382, -0.101286, -0.015382, 1.65851])

		names.append("LShoulderRoll")
		times.append([1.04, 1.28, 1.52, 1.76, 2, 2.56])
		keys.append([0.233874, 0.164061, 0.178024,
					 0.178024, 0.205949, 0.119999])

		names.append("LWristYaw")
		times.append([0.52, 1.04, 2.56])
		# keys.append([-0.26529, -0.340591, -6.49975e-07])
		keys.append([-0.26529, -0.340591, 0.0])

		names.append("RElbowRoll")
		times.append([0.44, 0.96, 1.2, 1.44, 1.68, 1.92, 2.48])
		keys.append([0.715585, 0.329852, 0.335988,
					 0.33292, 0.335988, 0.33292, 0.523457])

		names.append("RElbowYaw")
		times.append([0.44, 0.96, 1.2, 1.44, 1.68, 1.92, 2.48])
		keys.append([1.85878, 2.06165, 2.05858,
					 2.05704, 2.05858, 2.05704, 1.2217])

		names.append("RHand")
		times.append([0.96, 2.48])
		keys.append([0.0105719, 0])

		names.append("RShoulderPitch")
		times.append([0.96, 1.2, 1.44, 1.68, 1.92, 2.48])
		keys.append([1.83778, 1.83317, 1.77181, 1.83317, 1.77181, 1.65851])

		names.append("RShoulderRoll")
		times.append([0.96, 1.2, 1.44, 1.68, 1.92, 2.48])
		keys.append([-0.154976, -0.14884, -0.144238, -
					 0.14884, -0.144238, -0.119999])

		names.append("RWristYaw")
		times.append([0.96, 2.48])
		# keys.append([0.31903, 8.10213e-07])
		keys.append([0.31903, 0.0])

		return [names, keys, times]

	@staticmethod
	def bored_1():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1, 1.56, 1.96, 3.32])
		# keys.append([-0.509636, -0.303687, 0.345577, 0.37671])
		keys.append([-0.509636, -0.303687, 0.345577, 0.0])

		names.append("HeadYaw")
		times.append([1.56, 1.96, 3.32])
		keys.append([0, 0, 0])

		names.append("HipPitch")
		# times.append([0.88, 1.84])
		# keys.append([-0.0603725, -0.331613])
		times.append([0.88, 1.84, 3.32])
		keys.append([-0.0603725, -0.331613, 0.0])

		names.append("HipRoll")
		times.append([0.88])
		# keys.append([-6.76661e-07])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([0.88, 1.84])
		keys.append([-0.0504119, 0.122173])

		names.append("LElbowRoll")
		times.append([0.92, 1.48, 1.88, 2.48, 3.24])
		keys.append([-1.11003, -1.04022, -0.00872665, -0.164061, -0.0942478])

		names.append("LElbowYaw")
		times.append([0.92, 1.48, 1.88, 3.24])
		keys.append([-1.17635, -1.44164, -1.3226, -1.2898])

		names.append("LHand")
		times.append([0.92, 1.48, 1.88, 2.48, 3.24])
		keys.append([0.29, 0.34, 0.66144, 0.84, 0.75])

		names.append("LShoulderPitch")
		times.append([0.92, 1.88, 2.48, 3.24])
		keys.append([0.893609, 1.54636, 1.46084, 1.46084])

		names.append("LShoulderRoll")
		times.append([0.92, 1.88, 3.24])
		keys.append([0.460767, 0.0645772, 0.0506146])

		names.append("LWristYaw")
		times.append([1.48, 1.88, 3.24])
		keys.append([-1.06116, -0.696386, -0.630064])

		names.append("RElbowRoll")
		times.append([0.88, 1.44, 1.84, 2.44, 3.2])
		keys.append([1.11003, 1.04022, 0.00872665, 0.164061, 0.0942478])

		names.append("RElbowYaw")
		times.append([0.88, 1.44, 1.84, 3.2])
		keys.append([1.17635, 1.44164, 1.3226, 1.2898])

		names.append("RHand")
		times.append([0.88, 1.44, 1.84, 2.44, 3.2])
		keys.append([0.29, 0.34, 0.66144, 0.84, 0.75])

		names.append("RShoulderPitch")
		times.append([0.88, 1.84, 2.44, 3.2])
		keys.append([0.893609, 1.54636, 1.46084, 1.46084])

		names.append("RShoulderRoll")
		times.append([0.88, 1.84, 3.2])
		keys.append([-0.460767, -0.0645772, -0.0506146])

		names.append("RWristYaw")
		times.append([1.44, 1.84, 3.2])
		keys.append([1.06116, 0.696386, 0.630064])

		return [names, keys, times]

	@staticmethod
	def fearful_1():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.8, 1.36, 1.96])
		keys.append([0.0349066, 0.296942, 0.296942])

		names.append("HeadYaw")
		times.append([1.36, 1.96])
		keys.append([-0.665798, -0.665798])

		names.append("HipPitch")
		times.append([1.24])
		keys.append([0.0785398])

		names.append("HipRoll")
		times.append([1.24])
		keys.append([-0.0942478])

		names.append("KneePitch")
		times.append([1.24])
		keys.append([-0.0610865])

		names.append("LElbowRoll")
		times.append([0.4, 0.72, 1.28])
		keys.append([-0.757473, -1.09607, -1.19555])

		names.append("LElbowYaw")
		times.append([0.72, 1.28])
		keys.append([-0.0245859, 0.151844])

		names.append("LHand")
		times.append([0.72, 1.28])
		keys.append([0.545455, 0.522571])

		names.append("LShoulderPitch")
		times.append([0.72, 1.28])
		keys.append([-0.301942, -0.560251])

		names.append("LShoulderRoll")
		times.append([0.4, 0.72, 1.28])
		keys.append([0.488692, 0.0506146, 0.105804])

		names.append("LWristYaw")
		times.append([0.72, 1.28])
		keys.append([0.319395, 0.397935])

		names.append("RElbowRoll")
		times.append([0.64, 1.2])
		keys.append([0.827286, 1.31161])

		names.append("RElbowYaw")
		times.append([0.64, 1.2])
		keys.append([0.898881, 1.2514])

		names.append("RHand")
		times.append([0.64, 1.2])
		keys.append([0.745455, 0.713478])

		names.append("RShoulderPitch")
		times.append([0.64, 1.2])
		keys.append([0.696479, 0.791585])

		names.append("RShoulderRoll")
		times.append([0.64, 1.2])
		keys.append([-0.277507, -0.263545])

		names.append("RWristYaw")
		times.append([0.64, 1.2])
		keys.append([-0.506145, -0.504728])

		return [names, keys, times]
	
	@staticmethod
	def ask_for_attention_2():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.4, 1.04, 1.84, 2.28])
		keys.append([0.13894, -0.327396, -0.49767, -0.216948])

		names.append("HeadYaw")
		times.append([0.4, 1.04, 1.84, 2.28])
		keys.append([-0.135034, -0.351328, -0.415757, -0.418823])

		names.append("HipPitch")
		times.append([1.28])
		# keys.append([-3.67339e-09])
		keys.append([0.0])

		names.append("HipRoll")
		times.append([1.28])
		# keys.append([4.07479e-15])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([1.28])
		keys.append([-0.06981])

		names.append("LElbowRoll")
		times.append([0.64, 1.28, 2.28])
		keys.append([-1.28085, -0.561403, -0.566003])

		names.append("LElbowYaw")
		times.append([0.64, 1.28, 2.28])
		keys.append([-0.909316, -1.2898, -1.17635])

		names.append("LHand")
		times.append([1.28])
		keys.append([0.238207])

		names.append("LShoulderPitch")
		times.append([0.64, 1.28, 2.28])
		keys.append([1.45211, 1.52015, 1.52015])

		names.append("LShoulderRoll")
		times.append([0.64, 1.28, 2.28])
		keys.append([0.395731, 0.148756, 0.159494])

		names.append("LWristYaw")
		times.append([1.28])
		keys.append([0.147222])

		names.append("RElbowRoll")
		times.append([0.64, 1.28, 1.84, 2.28, 2.68])
		keys.append([1.15208, 0.667332, 0.938849, 0.395814, 0.785451])

		names.append("RElbowYaw")
		times.append([0.64, 1.28, 1.84, 2.28, 2.68])
		keys.append([1.09523, 0.647306, 0.386526, 0.343573, 0.299088])

		names.append("RHand")
		times.append([1.28])
		keys.append([0.853478])

		names.append("RShoulderPitch")
		times.append([0.64, 1.28, 1.84, 2.28, 2.68])
		keys.append([1.62608, -1.08756, -1.09063, -1.28392, -1.27625])

		names.append("RShoulderRoll")
		times.append([0.64, 1.28, 1.84, 2.28, 2.68])
		keys.append([-0.681137, -0.981802, -0.444902, -0.951122, -0.397349])

		names.append("RWristYaw")
		times.append([1.28])
		keys.append([-0.312978])

		return [names, keys, times]

	@staticmethod
	def relieved_1():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.4, 2.28])
		keys.append([0.306146, 0.24632])

		names.append("HeadYaw")
		times.append([1.4, 2.28])
		keys.append([-0.624379, 0.0183661])

		names.append("HipPitch")
		times.append([1.28])
		keys.append([0.000247308])

		names.append("HipRoll")
		times.append([1.28])
		# keys.append([7.19482e-19])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([1.28])
		keys.append([-0.0696179])

		names.append("LElbowRoll")
		times.append([1.32, 2.2])
		keys.append([-0.437147, -0.42641])

		names.append("LElbowYaw")
		times.append([1.32, 2.2])
		keys.append([-1.17635, -1.31161])

		names.append("LHand")
		times.append([2.2])
		keys.append([0.110572])

		names.append("LShoulderPitch")
		times.append([1.32, 2.2])
		keys.append([1.38516, 1.52322])

		names.append("LShoulderRoll")
		times.append([1.32, 2.2])
		keys.append([0.10821, 0.105804])

		names.append("LWristYaw")
		times.append([2.2])
		keys.append([-0.179519])

		names.append("RElbowRoll")
		times.append([0.56, 1.24, 2.12, 2.76, 2.92])
		keys.append([0.671952, 1.38678, 1.56207, 1.0821, 0.921534])

		names.append("RElbowYaw")
		times.append([1.24, 2.12, 2.76])
		keys.append([-0.378736, 0.190241, 1.20428])

		names.append("RHand")
		times.append([1.24, 2.12, 2.76])
		keys.append([0.585455, 0.327273, 0.585455])

		names.append("RShoulderPitch")
		times.append([1.24, 2.12, 2.92])
		keys.append([-0.820305, -0.548033, 1.94081])

		names.append("RShoulderRoll")
		times.append([0.56, 1.24, 2.12, 2.92])
		keys.append([-0.233874, -0.029188, -0.610865, -0.284489])

		names.append("RWristYaw")
		times.append([1.24, 2.12, 2.76])
		keys.append([-0.366519, -0.383972, 0.413643])

		return [names, keys, times]

	@staticmethod
	def hey_1():
		names = list()
		times = list()
		keys = list()

		names.append("HipPitch")
		times.append([1.2, 3.24])
		# keys.append([-3.84404e-09, -0.0595632])
		keys.append([0.0, -0.0595632])

		names.append("HipRoll")
		times.append([1.2, 3.24])
		# keys.append([4.51721e-32, -6.54135e-07])
		keys.append([0.0, 0.0])

		names.append("KneePitch")
		times.append([1.2, 3.24])
		keys.append([-0.06981, -0.0495208])

		names.append("LElbowRoll")
		times.append([0.68, 1.24, 2])
		keys.append([-0.599753, -0.516916, -0.523053])

		names.append("LElbowYaw")
		times.append([0.68, 1.24, 2])
		keys.append([-0.940383, -1.15514, -1.14594])

		names.append("LHand")
		times.append([1.24])
		keys.append([0.262571])

		names.append("LShoulderPitch")
		times.append([0.68, 1.24, 2])
		keys.append([1.43425, 1.49561, 1.50174])

		names.append("LShoulderRoll")
		times.append([0.68, 1.24, 2])
		keys.append([0.10427, 0.182504, 0.167164])

		names.append("LWristYaw")
		times.append([1.24])
		keys.append([-0.754769])

		names.append("RElbowRoll")
		times.append([0.6, 1.16, 1.48, 1.92, 2.36, 2.72, 3.2])
		keys.append([1.22348, 0.366519, 0.314159,
					 0.92351, 0.345191, 1.33692, 0.522443])

		names.append("RElbowYaw")
		times.append([0.6, 1.16, 1.92, 2.36, 2.72, 3.2])
		keys.append([0.0750492, 0.776162, 0.536858,
					 0.747017, 1.55509, 1.22296])

		names.append("RHand")
		times.append([0.6, 1.16, 2.72, 3.2])
		keys.append([0.84, 0.890909, 0.34, 0])

		names.append("RShoulderPitch")
		times.append([1.16, 1.92, 2.36, 2.72, 3.2])
		keys.append([-1.22869, -1.17654, -1.25664, 0.837758, 1.56615])

		names.append("RShoulderRoll")
		times.append([0.6, 1.16, 1.92, 2.36, 3.2])
		keys.append([-0.729548, -0.767945, -0.345191, -0.680678, -0.130382])

		names.append("RWristYaw")
		times.append([0.6, 1.16, 2.72, 3.2])
		# keys.append([-0.464258, -0.541052, 0.762709, 7.67468e-07])
		keys.append([-0.464258, -0.541052, 0.762709, 0.0])

		return [names, keys, times]

	@staticmethod
	def hey_3():
		names = list()
		times = list()
		keys = list()

		names.append("HipPitch")
		times.append([1.56])
		keys.append([-0.0599238])

		names.append("HipRoll")
		times.append([1.56])
		# keys.append([5.14422e-07])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([1.56])
		keys.append([-0.0499168])

		names.append("LElbowRoll")
		times.append([0.68, 1.6, 2])
		keys.append([-0.560251, -0.768491, -0.76389])

		names.append("LElbowYaw")
		times.append([0.68, 1.6, 2])
		keys.append([-1.44164, -1.38831, -1.38831])

		names.append("LHand")
		times.append([2])
		keys.append([0.162935])

		names.append("LShoulderPitch")
		times.append([1.6, 2])
		keys.append([1.5447, 1.5447])

		names.append("LShoulderRoll")
		times.append([1.6, 2])
		keys.append([0.030638, 0.033706])

		names.append("LWristYaw")
		times.append([2])
		keys.append([-0.239346])

		names.append("RElbowRoll")
		times.append([0.6, 1.12, 1.52, 1.92])
		keys.append([1.44862, 1.01555, 1.56207, 1.01862])

		names.append("RElbowYaw")
		times.append([0.6, 1.12, 1.52, 1.92])
		keys.append([0.947714, 1.88984, 1.22102, 1.89906])

		names.append("RHand")
		times.append([0.6, 1.12, 1.92])
		keys.append([0.9, 0.890909, 0.890933])

		names.append("RShoulderPitch")
		times.append([1.12, 1.52, 1.92])
		keys.append([-0.024502, -0.276078, -0.0291041])

		names.append("RShoulderRoll")
		times.append([0.6, 1.12, 1.52, 1.92])
		keys.append([-0.685914, -0.834538, -0.889762, -0.849878])

		names.append("RWristYaw")
		times.append([0.6, 1.12, 1.92])
		keys.append([-0.994838, -0.349066, -0.345191])

		return [names, keys, times]

	@staticmethod
	def hide_1():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.48, 2.28])
		keys.append([0.172688, -0.255298])

		names.append("HeadYaw")
		times.append([1.48, 2.28])
		keys.append([-0.081344, -0.0429939])

		# *********************** #
		names.append("HipPitch")
		times.append([1.36])
		keys.append([-0.213223])

		names.append("HipRoll")
		times.append([1.36])
		keys.append([-0.00920387])

		names.append("KneePitch")
		times.append([1.36])
		keys.append([0.0762543])

		names.append("LElbowRoll")
		times.append([0.72, 1.4, 2.2])
		keys.append([-0.616101, -1.40674, -1.40674])

		names.append("LElbowYaw")
		times.append([1.4, 2.2])
		keys.append([-0.25622, -0.190241])

		names.append("LHand")
		times.append([2.2])
		keys.append([0.43])

		names.append("LShoulderPitch")
		times.append([1.4, 2.2])
		keys.append([0.0436332, -0.0436332])

		names.append("LShoulderRoll")
		times.append([0.72, 1.4, 2.2])
		keys.append([0.333358, 0.29147, 0.29147])

		names.append("LWristYaw")
		times.append([1.4, 2.2])
		keys.append([-1.32645, -1.32645])

		names.append("RElbowRoll")
		times.append([0.64, 1.32, 2.12])
		keys.append([0.574213, 1.4207, 1.44862])

		names.append("RElbowYaw")
		times.append([1.32, 2.12])
		keys.append([0.269941, 0.269941])

		names.append("RHand")
		times.append([2.12])
		keys.append([0.62])

		names.append("RShoulderPitch")
		times.append([1.32, 2.12])
		keys.append([-0.445059, -0.417134])

		names.append("RShoulderRoll")
		times.append([0.64, 1.32, 2.12])
		keys.append([-0.389208, -0.219911, -0.178024])

		names.append("RWristYaw")
		times.append([1.32, 2.12])
		keys.append([1.16064, 1.16064])

		return [names, keys, times]
	
	@staticmethod
	def kisses_1():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.68, 1.32, 2.08, 2.84])
		keys.append([-0.477728, -0.170928, -0.523747, -0.453786])

		names.append("HeadYaw")
		times.append([0.68, 1.32, 2.08, 2.84])
		keys.append([-0.075208, -0.04913, -0.032256, -0.032256])

		names.append("HipPitch")
		# times.append([1.2])
		# keys.append([-0.213223])
		times.append([1.2, 2.84])
		keys.append([-0.213223, 0.0])

		names.append("HipRoll")
		times.append([1.2])
		keys.append([-0.00920387])

		names.append("KneePitch")
		times.append([1.2])
		keys.append([0.0762543])

		names.append("LElbowRoll")
		times.append([0.6, 1.24, 2, 2.76])
		keys.append([-0.535324, -1.56207, -1.55697, -0.785367])

		names.append("LElbowYaw")
		times.append([0.6, 1.24, 2, 2.76])
		keys.append([-1.93288, -0.909316, -0.947714, -1.77181])

		names.append("LHand")
		times.append([1.24, 2, 2.76])
		keys.append([0.73166, 0.702933, 0.8])

		names.append("LShoulderPitch")
		times.append([0.6, 1.24, 2, 2.76])
		keys.append([0.863599, 0.18675, -0.18675, 0.955639])

		names.append("LShoulderRoll")
		times.append([0.6, 1.24, 2, 2.76])
		keys.append([0.030638, 0.205949, 0.277507, 0.914223])

		names.append("LWristYaw")
		times.append([1.24, 2, 2.76])
		keys.append([-1.19503, -1.12446, -1.53589])

		names.append("RElbowRoll")
		times.append([0.52, 1.16, 1.92, 2.68])
		keys.append([0.527739, 1.55859, 1.5621, 0.716419])

		names.append("RElbowYaw")
		times.append([0.52, 1.16, 1.92, 2.68])
		keys.append([2.0856, 0.986111, 0.872665, 1.94047])

		names.append("RHand")
		times.append([1.16, 1.92, 2.68])
		keys.append([0.789478, 0.758933, 0.909091])

		names.append("RShoulderPitch")
		times.append([0.52, 1.16, 1.92, 2.68])
		keys.append([1.01095, 0.216421, -0.274017, 1.10606])

		names.append("RShoulderRoll")
		times.append([0.52, 1.16, 1.92, 2.68])
		keys.append([-0.17185, -0.219911, -0.319395, -0.849878])

		names.append("RWristYaw")
		times.append([1.16, 1.92, 2.68])
		keys.append([1.00319, 1.16064, 1.39626])

		return [names, keys, times]

	@staticmethod
	def me_1():
		names = list()
		times = list()
		keys = list()

		names.append("HipPitch")
		times.append([1.2, 1.76])
		keys.append([-0.0601011, -0.0600997])

		names.append("HipRoll")
		times.append([1.2, 1.76])
		# keys.append([-7.07461e-07, -5.92168e-07])
		keys.append([0.0, 0.0])

		names.append("KneePitch")
		times.append([1.2, 1.76])
		keys.append([-0.0501103, -0.0501089])

		names.append("LElbowRoll")
		times.append([0.72, 1.24, 1.8])
		keys.append([-0.685914, -1.43466, -1.44862])

		names.append("LElbowYaw")
		times.append([0.72, 1.24, 1.8])
		keys.append([-1.51669, -0.909316, -0.872665])

		names.append("LHand")
		times.append([0.72, 1.24, 1.8])
		keys.append([0.91, 0.8, 0.74])

		names.append("LShoulderPitch")
		times.append([1.24, 1.8])
		keys.append([0.610865, 0.610865])

		names.append("LShoulderRoll")
		times.append([1.24, 1.8])
		keys.append([0.249582, 0.249582])

		names.append("LWristYaw")
		times.append([0.72, 1.24, 1.8])
		keys.append([-0.994838, -0.79587, -0.79587])

		names.append("RElbowRoll")
		times.append([0.68, 1.2, 1.76])
		keys.append([0.588176, 0.522443, 0.47473])

		names.append("RElbowYaw")
		times.append([1.2, 1.76])
		keys.append([1.22296, 1.22296])

		names.append("RHand")
		times.append([0.68, 1.2, 1.76])
		keys.append([0.1, 0.17, 0.1])

		names.append("RShoulderPitch")
		times.append([1.2, 1.76])
		keys.append([1.56614, 1.56614])

		names.append("RShoulderRoll")
		times.append([1.2, 1.76])
		keys.append([-0.130365, -0.130366])

		names.append("RWristYaw")
		times.append([0.68, 1.2, 1.76])
		# keys.append([0.165806, 6.43787e-07, -1.12766e-07])
		keys.append([0.165806, 0.0, 0.0])

		return [names, keys, times]

	@staticmethod
	def me_2():
		names = list()
		times = list()
		keys = list()

		names.append("HipPitch")
		times.append([1.28])
		keys.append([-0.0597217])

		names.append("HipRoll")
		times.append([1.28])
		keys.append([0.0])
		# keys.append([-7.07461e-07])

		names.append("KneePitch")
		times.append([1.28])
		keys.append([-0.0496953])

		names.append("LElbowRoll")
		times.append([0.72, 1.32])
		keys.append([-0.799361, -1.56207])

		names.append("LElbowYaw")
		times.append([0.72, 1.32])
		keys.append([-1.40324, -0.607375])

		names.append("LHand")
		times.append([0.72, 1.32])
		keys.append([0.97, 0.73])

		names.append("LShoulderPitch")
		times.append([1.32])
		keys.append([0.411898])

		names.append("LShoulderRoll")
		times.append([1.32])
		keys.append([0.418879])

		names.append("LWristYaw")
		times.append([0.72, 1.32])
		keys.append([-1.16064, -1.028])

		names.append("RElbowRoll")
		times.append([0.64, 1.24])
		keys.append([0.375246, 0.522442])

		names.append("RElbowYaw")
		times.append([0.64, 1.24])
		keys.append([1.2514, 1.22296])

		names.append("RHand")
		times.append([0.64, 1.24])
		keys.append([0.34, 0])

		names.append("RShoulderPitch")
		times.append([1.24])
		keys.append([1.56615])

		names.append("RShoulderRoll")
		times.append([1.24])
		keys.append([-0.130382])

		names.append("RWristYaw")
		times.append([1.24])
		keys.append([0.0])
		# keys.append([7.38658e-07])

		return [names, keys, times]

	@staticmethod
	def no_1():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.68, 1.96])
		keys.append([-0.324631, -0.523599])

		names.append("HeadYaw")
		times.append([0.68, 1.16, 1.56, 1.96])
		keys.append([-0.260054, 0.260054, 0.10472, 0])

		names.append("HipPitch")
		times.append([1.44])
		# keys.append([7.17332e-09])
		keys.append([0.0])

		names.append("HipRoll")
		times.append([1.44])
		# keys.append([-1.80471e-16])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([1.44])
		keys.append([-0.06981])

		names.append("LElbowRoll")
		times.append([1.48, 1.88])
		keys.append([-0.26611, -0.263807])

		names.append("LElbowYaw")
		times.append([1.48, 1.88])
		keys.append([-1.21808, -1.21804])

		names.append("LHand")
		times.append([1.48, 1.88])
		keys.append([0.178993, 0.181818])

		names.append("LShoulderPitch")
		times.append([1.48, 1.88])
		keys.append([1.56358, 1.5631])

		names.append("LShoulderRoll")
		times.append([1.48, 1.88])
		keys.append([0.177477, 0.177901])

		names.append("LWristYaw")
		times.append([1.48, 1.88])
		keys.append([-0.190278, -0.191986])

		names.append("RElbowRoll")
		times.append([0.4, 0.72, 1.4, 1.8])
		keys.append([0.785398, 1.30725, 1.36136, 1.4328])

		names.append("RElbowYaw")
		times.append([0.4, 0.72, 1.04, 1.4, 1.8])
		keys.append([1.59349, 1.213, 1.32645, 1.74358, 1.78198])

		names.append("RHand")
		times.append([0.72, 1.4, 1.8])
		keys.append([0.51, 0.760022, 0.787273])

		names.append("RShoulderPitch")
		times.append([0.72, 1.4, 1.8])
		keys.append([0.439823, 0.657481, 0.666716])

		names.append("RShoulderRoll")
		times.append([1.4, 1.8])
		keys.append([-0.391181, -0.397349])

		names.append("RWristYaw")
		times.append([0.72, 1.4, 1.8])
		keys.append([-1.22697, -1.028, -0.895354])

		return [names, keys, times]

	@staticmethod
	def no_2():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.12, 1.6])
		keys.append([-0.471239, -0.523599])

		names.append("HeadYaw")
		times.append([0.72, 1.12, 1.6])
		keys.append([-0.329852, 0.185572, 0])

		names.append("HipPitch")
		times.append([1])
		keys.append([-0.0597852])

		names.append("HipRoll")
		times.append([1])
		# keys.append([-7.09139e-07])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([1])
		keys.append([-0.0497649])

		names.append("LElbowRoll")
		times.append([1.04, 1.52])
		keys.append([-0.271475, -0.36505])

		names.append("LElbowYaw")
		times.append([1.04, 1.52])
		keys.append([-1.2119, -1.15361])

		names.append("LHand")
		times.append([1.52])
		keys.append([0.184025])

		names.append("LShoulderPitch")
		times.append([1.04, 1.52])
		keys.append([1.52015, 1.48334])

		names.append("LShoulderRoll")
		times.append([1.04, 1.52])
		keys.append([0.171766, 0.13495])

		names.append("LWristYaw")
		times.append([1.52])
		keys.append([-0.190258])

		names.append("RElbowRoll")
		times.append([0.28, 0.56, 0.96, 1.44])
		keys.append([0.813323, 1.46259, 1.45581, 1.54171])

		names.append("RElbowYaw")
		times.append([0.28, 0.56, 0.96, 1.44])
		keys.append([1.59349, 1.09956, 1.97728, 1.34528])

		names.append("RHand")
		times.append([0.56, 1.44])
		keys.append([0.48, 0.885115])

		names.append("RShoulderPitch")
		times.append([0.56, 0.96, 1.44])
		keys.append([0.752237, 0.883625, 0.799256])

		names.append("RShoulderRoll")
		times.append([0.56, 0.96, 1.44])
		keys.append([-0.418879, -0.30224, -0.276162])

		names.append("RWristYaw")
		times.append([0.56, 0.96, 1.44])
		keys.append([-1.49226, -0.837758, -1.5708])

		return [names, keys, times]

	@staticmethod
	def no_3():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.88, 1.92, 2.32])
		keys.append([-0.272136, -0.010472, -0.13439])

		names.append("HeadYaw")
		times.append([0.88, 1.44, 1.92])
		keys.append([-0.34985, 0.323916, -0.272421])

		names.append("LElbowRoll")
		times.append([0.44, 0.8, 1.36, 1.84, 2.24])
		keys.append([-0.715585, -1.54457, -0.219911, -0.176687, -0.418879])

		names.append("LElbowYaw")
		times.append([0.44, 0.8, 1.36, 1.84, 2.24])
		keys.append([-1.213, -0.581048, -0.398883, -0.439415, -1.2898])

		names.append("LHand")
		times.append([0.8, 1.36, 1.84, 2.24])
		keys.append([0.82, 0.82, 0.9, 0.57])

		names.append("LShoulderPitch")
		times.append([0.8, 1.36, 1.84])
		keys.append([0.112844, 0.673385, 0.839798])

		names.append("LShoulderRoll")
		times.append([0.8, 1.36, 1.84])
		keys.append([0.247341, 0.685914, 0.633462])

		names.append("LWristYaw")
		times.append([0.44, 0.8, 1.36, 1.84, 2.24])
		keys.append([-0.26529, 0.0523599, 0.0523599, 0.0366207, -0.596903])

		names.append("RElbowRoll")
		times.append([0.4, 0.76, 1.32, 1.8, 2.2])
		keys.append([0.644027, 1.40554, 0.219911, 0.212637, 0.418879])

		names.append("RElbowYaw")
		times.append([0.4, 0.76, 1.32, 1.8, 2.2])
		keys.append([1.2898, 0.619969, 0.46476, 0.516359, 1.2898])

		names.append("RHand")
		times.append([0.76, 1.32, 1.8, 2.2])
		keys.append([0.827273, 0.827273, 0.86, 0.57])

		names.append("RShoulderPitch")
		times.append([0.76, 1.32, 1.8])
		keys.append([0.374097, 0.725624, 0.879841])

		names.append("RShoulderRoll")
		times.append([0.76, 1.32, 1.8])
		keys.append([-0.365722, -0.685914, -0.636097])

		names.append("RWristYaw")
		times.append([0.4, 0.76, 1.32, 1.8, 2.2])
		keys.append([0.696386, 0.244346, 0.244346, 0.243058, 0.596903])

		return [names, keys, times]

	@staticmethod
	def no_8():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.52, 1.16, 1.84])
		keys.append([-0.152002, -0.068944, -0.161279])

		names.append("HeadYaw")
		times.append([0.52, 0.96, 1.44, 1.84])
		keys.append([-0.440631, 0.272853, -0.146715, -0.00158487])

		# *********************** #
		names.append("HipPitch")
		times.append([1.52])
		keys.append([-0.213223])

		names.append("HipRoll")
		times.append([1.52])
		keys.append([-0.00920389])

		names.append("KneePitch")
		times.append([1.52])
		keys.append([0.0762569])

		names.append("LElbowRoll")
		times.append([0.6, 1.08, 1.6])
		keys.append([-0.575208, -0.46476, -0.377323])

		names.append("LElbowYaw")
		times.append([0.6, 1.08, 1.6])
		keys.append([-0.900499, -1.00174, -1.1306])

		names.append("LHand")
		times.append([1.6])
		keys.append([0.111663])

		names.append("LShoulderPitch")
		times.append([0.6, 1.08, 1.6])
		keys.append([1.36829, 1.42965, 1.45419])

		names.append("LShoulderRoll")
		times.append([0.6, 1.08, 1.6])
		keys.append([0.015298, 0.05825, 0.06592])

		names.append("LWristYaw")
		times.append([1.6])
		keys.append([-0.196393])

		names.append("RElbowRoll")
		times.append([0.44, 0.92, 1.44])
		keys.append([0.742498, 0.650458, 0.572224])

		names.append("RElbowYaw")
		times.append([0.44, 0.92, 1.44])
		keys.append([0.882007, 1.19801, 1.46646])

		names.append("RHand")
		times.append([1.44])
		keys.append([0.218935])

		names.append("RShoulderPitch")
		times.append([0.44, 0.92, 1.44])
		keys.append([1.50183, 1.54631, 1.57239])

		names.append("RShoulderRoll")
		times.append([0.44, 0.92, 1.44])
		keys.append([-0.00924597, -0.016916, -0.030722])

		names.append("RWristYaw")
		times.append([1.44])
		keys.append([0.030638])

		return [names, keys, times]

	@staticmethod
	def no_9():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.08, 1.44, 1.8])
		keys.append([-0.434587, -0.420624, -0.523599])

		names.append("HeadYaw")
		times.append([0.6, 1.08, 1.8])
		# keys.append([0.233874, -0.260054, -6.49739e-07])
		keys.append([0.233874, -0.260054, 0.0])

		names.append("HipPitch")
		times.append([1.68])
		keys.append([-0.059999])

		names.append("HipRoll")
		times.append([1.68])
		# keys.append([-7.78904e-07])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([1.68])
		keys.append([-0.049999])

		names.append("LElbowRoll")
		times.append([1, 1.72])
		keys.append([-0.42641, -0.477746])

		names.append("LElbowYaw")
		times.append([1, 1.72])
		keys.append([-0.817664, -0.96524])

		names.append("LHand")
		times.append([1, 1.72])
		keys.append([0.5016, 0.5016])

		names.append("LShoulderPitch")
		times.append([1, 1.72])
		keys.append([1.41124, 1.42489])

		names.append("LShoulderRoll")
		times.append([1, 1.72])
		keys.append([0.095066, 0.0729759])

		names.append("LWristYaw")
		times.append([1, 1.72])
		keys.append([-0.021518, -0.0798092])

		names.append("RElbowRoll")
		times.append([0.44, 0.92, 1.64])
		keys.append([1.29329, 1.14806, 1.09607])

		names.append("RElbowYaw")
		times.append([0.44, 0.92, 1.64])
		keys.append([0.79587, 1.76048, 1.85878])

		names.append("RHand")
		times.append([0.44, 0.92, 1.64])
		keys.append([0.69, 0.753998, 0.77])

		names.append("RShoulderPitch")
		times.append([0.92, 1.64])
		keys.append([0.863879, 0.863879])

		names.append("RShoulderRoll")
		times.append([0.44, 0.92, 1.64])
		keys.append([-0.389208, -0.493628, -0.493628])

		names.append("RWristYaw")
		times.append([0.44, 0.92, 1.64])
		keys.append([-1.22697, -1.01758, -1.01758])

		return [names, keys, times]

	@staticmethod
	def touch_head_4():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.04, 1.76, 2.2, 2.96])
		keys.append([-0.57437, -0.387222, -0.0482076, -0.318192])

		names.append("HeadYaw")
		times.append([1.04, 1.76, 2.2, 2.96])
		keys.append([-0.358999, -0.319114, -0.271559, -0.023052])

		names.append("HipPitch")
		times.append([1.64])
		# keys.append([-1.28319e-08])
		keys.append([0.0])

		names.append("HipRoll")
		times.append([1.64])
		# keys.append([4.59828e-14])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([1.64])
		keys.append([-0.06981])

		names.append("LElbowRoll")
		times.append([0.52, 0.88, 1.6, 2.04, 2.8])
		keys.append([-0.729548, -1.18114, -1.18159, -1.40674, -0.481634])

		names.append("LElbowYaw")
		times.append([0.52, 0.88, 1.6, 2.04, 2.48, 2.8])
		keys.append([-1.09956, -0.37127, -0.89283, -
					 0.994838, -1.44164, -1.17355])

		names.append("LHand")
		times.append([0.88, 1.6, 2.8])
		keys.append([0.28148, 0.82, 0.3])

		names.append("LShoulderPitch")
		times.append([0.88, 1.6, 2.04, 2.8])
		keys.append([-0.205598, -0.938987, -0.135034, 1.54163])

		names.append("LShoulderRoll")
		times.append([0.88, 1.6, 2.04, 2.8])
		keys.append([0.421808, 0.361283, 0.233874, 0.093532])

		names.append("LWristYaw")
		times.append([0.88, 1.6, 2.04, 2.8])
		keys.append([-0.43263, -1.0472, -0.895354, 0.0996681])

		names.append("RElbowRoll")
		times.append([0.72, 1.4, 1.8, 2.6])
		keys.append([0.592166, 0.529271, 0.533873, 0.423426])

		names.append("RElbowYaw")
		times.append([0.72, 1.4, 1.8, 2.6])
		keys.append([1.52936, 1.88677, 1.37749, 1.17193])

		names.append("RHand")
		times.append([0.72, 2.6])
		keys.append([0.264389, 0.302])

		names.append("RShoulderPitch")
		times.append([0.72, 1.4, 1.8, 2.6])
		keys.append([1.74113, 1.74113, 1.56165, 1.54325])

		names.append("RShoulderRoll")
		times.append([0.72, 1.4, 1.8, 2.6])
		keys.append([-0.285367, -0.0982179, -0.084412, -0.081344])

		names.append("RWristYaw")
		times.append([0.72, 2.6])
		keys.append([0.328234, 0.184038])

		return [names, keys, times]


	@staticmethod
	def scratch_head_1():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.76, 1.4, 2.72])
		keys.append([-0.228638, 0.178518, 0.219911])

		names.append("HeadYaw")
		times.append([1.4, 2.72])
		keys.append([0.287208, 0.294486])

		names.append("HipPitch")
		times.append([1.28])
		keys.append([-0.0599039])

		names.append("HipRoll")
		times.append([1.28])
		# keys.append([-5.73121e-07])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([1.28])
		keys.append([-0.0499468])

		names.append("LElbowRoll")
		times.append([0.68, 1.32, 2.64])
		keys.append([-0.630064, -0.296966, -0.263545])

		names.append("LElbowYaw")
		times.append([1.32, 2.64])
		keys.append([-1.18738, -1.18609])

		names.append("LHand")
		times.append([0.68, 1.32, 2.64])
		keys.append([0.23, 0.361079, 0.37])

		names.append("LShoulderPitch")
		times.append([1.32, 2.64])
		keys.append([1.51399, 1.51476])

		names.append("LShoulderRoll")
		times.append([1.32, 2.64])
		keys.append([0.117113, 0.111275])

		names.append("LWristYaw")
		times.append([1.32, 2.64])
		# keys.append([-7.12869e-07, -7.12869e-07])
		keys.append([0.0, 0.0])

		names.append("RElbowRoll")
		times.append([0.6, 1.24, 2.56])
		keys.append([0.574213, 1.12554, 1.18159])

		names.append("RElbowYaw")
		times.append([0.6, 1.24, 2.56])
		keys.append([1.36485, 0.883231, 0.834267])

		names.append("RHand")
		times.append([0.6, 1.24, 1.56, 1.8, 2.12, 2.36, 2.56])
		keys.append([0.72, 0.611074, 0.33, 0.65, 0.38, 0.59, 0.64])

		names.append("RShoulderPitch")
		times.append([1.24, 2.56])
		keys.append([-0.417472, -0.467748])

		names.append("RShoulderRoll")
		times.append([0.6, 1.24, 2.56])
		keys.append([-0.136136, -0.27763, -0.29147])

		names.append("RWristYaw")
		times.append([0.6, 1.24, 2.56])
		keys.append([0.928515, 1.10912, 1.12748])

		return [names, keys, times]

	@staticmethod
	def show_muscles_2():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.76, 1.44])
		keys.append([0.0699109, 0.103659])

		names.append("HeadYaw")
		times.append([0.76, 1.44])
		keys.append([-0.553816, -0.65506])

		names.append("HipPitch")
		times.append([1.32])
		# keys.append([1.38185e-06])
		keys.append([0.0])

		names.append("HipRoll")
		times.append([1.32])
		# keys.append([3.56248e-14])
		keys.append([0.0])

		names.append("KneePitch")
		times.append([1.32])
		keys.append([-0.0698085])

		names.append("LElbowRoll")
		times.append([0.68, 1.36])
		keys.append([-0.799172, -1.06302])

		names.append("LElbowYaw")
		times.append([0.68, 1.36])
		keys.append([-1.18122, -1.23798])

		names.append("LHand")
		times.append([0.68, 1.36])
		keys.append([0.3052, 0.2])

		names.append("LShoulderPitch")
		times.append([0.68, 1.36])
		keys.append([1.64901, 1.89291])

		names.append("LShoulderRoll")
		times.append([0.68, 1.36])
		keys.append([0.145688, 0.259204])

		names.append("LWristYaw")
		times.append([0.68, 1.36])
		keys.append([0.217786, 0.256136])

		names.append("RElbowRoll")
		times.append([0.6, 1.28, 1.8, 2])
		keys.append([0.342125, 1.5233, 0.342125, 0.502655])

		names.append("RElbowYaw")
		times.append([0.6, 1.28, 1.8, 2])
		keys.append([2.03865, 2.08567, 2.03865, 1.21649])

		names.append("RHand")
		times.append([0.6, 1.28, 1.8, 2])
		keys.append([0.2, 0, 0.2, 0.6])

		names.append("RShoulderPitch")
		times.append([0.6, 1.28, 1.8, 2])
		keys.append([1.735, 0.866751, 1.735, 1.68075])

		names.append("RShoulderRoll")
		times.append([0.6, 1.28, 1.8])
		keys.append([-0.168782, -0.561486, -0.168782])

		names.append("RWristYaw")
		times.append([0.6, 1.28, 1.8, 2])
		keys.append([1.73645, 1.34834, 1.73645, 0])

		return [names, keys, times]

	@staticmethod
	def show_muscles_4():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.64, 0.88, 1.24, 1.84, 2.4, 2.96])
		keys.append([-0.473126, -0.519146, -0.644934, -
					 0.724701, -0.0628318, -0.348872])

		names.append("HeadYaw")
		times.append([0.64, 0.88, 1.24, 1.84, 2.96])
		keys.append([0.013764, 0.015298, 0.0352401, 0.0475121, -0.00464395])

		names.append("HipPitch")
		times.append([1.12, 1.72, 2.84])
		# keys.append([-0.780162, -0.79006, 1.12516e-07])
		keys.append([-0.780162, -0.79006, 0.0])

		names.append("HipRoll")
		times.append([1.72, 2.84])
		# keys.append([-1.16874e-05, 5.47648e-14])
		keys.append([0.0, 0.0])

		names.append("KneePitch")
		times.append([1.12, 1.72, 2.84])
		keys.append([0.42237, 0.4009, -0.0698099])

		names.append("LElbowRoll")
		times.append([0.52, 0.76, 0.92, 1.12, 1.76, 2.32, 2.88])
		keys.append([-0.466294, -0.375789, -1.36485, -
					 1.25324, -1.33692, -1.15715, -0.483168])

		names.append("LElbowYaw")
		times.append([0.52, 0.76, 1.12, 1.76, 2.88])
		keys.append([-0.564555, -0.570689, -0.259288, -0.250085, -1.17202])

		names.append("LHand")
		times.append([0.52, 0.76, 1.12, 1.76, 2.88])
		keys.append([0.7552, 0.7552, 0, 0.2232, 0.3])

		names.append("LShoulderPitch")
		times.append([0.52, 0.76, 1.12, 1.76, 2.88])
		keys.append([1.18574, 1.20415, 0.991347, 1.0124, 1.53703])

		names.append("LShoulderRoll")
		times.append([0.52, 0.76, 1.12, 1.76, 2.88])
		keys.append([0.868202, 0.908086, 0.496974, 0.446352, 0.130348])

		names.append("LWristYaw")
		times.append([0.52, 0.76, 1.12, 1.76, 2.88])
		keys.append([-0.742498, -0.744032, -1.53864, -1.53864, 0.105804])

		names.append("RElbowRoll")
		times.append([0.44, 0.76, 0.92, 1.12, 1.68, 2.24, 2.8])
		keys.append([0.441834, 0.389678, 1.40324,
					 1.19656, 1.26536, 1.1397, 0.43263])

		names.append("RElbowYaw")
		times.append([0.44, 0.76, 1.12, 1.68, 2.8])
		keys.append([0.075124, 0.078192, 0.194775, 0.168698, 1.16273])

		names.append("RHand")
		times.append([0.44, 0.76, 1.12, 1.68, 2.8])
		keys.append([0.6988, 0.6992, 0, 0.0348, 0.3016])

		names.append("RShoulderPitch")
		times.append([0.44, 0.76, 1.12, 1.68, 2.8])
		keys.append([0.997141, 1.00481, 1.01753, 0.994073, 1.52944])

		names.append("RShoulderRoll")
		times.append([0.44, 0.76, 1.12, 1.68, 2.8])
		keys.append([-0.808459, -0.845275, -0.464844, -0.412688, -0.107422])

		names.append("RWristYaw")
		times.append([0.44, 0.76, 1.12, 1.68, 2.8])
		keys.append([1.10137, 1.10137, 1.58305, 1.56464, 0.177901])

		return [names, keys, times]

	@staticmethod
	def show_muscles_5():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.56, 0.92, 1.28, 1.64, 1.96, 2.64])
		keys.append([-0.51301, -0.649535, -0.531418, -
					 0.634195, -0.146608, -0.350406])

		names.append("HeadYaw")
		times.append([0.56, 0.92, 1.28, 1.64, 2.64])
		keys.append([-0.039926, -0.055266, -0.032256, 0.047596, -0.0245859])

		names.append("HipPitch")
		times.append([1.6, 2.52])
		# keys.append([-0.60912, 1.52383e-06])
		keys.append([-0.60912, 0.0])

		names.append("HipRoll")
		times.append([1.6, 2.52])
		# keys.append([2.35087e-14, -2.04862e-13])
		keys.append([0.0, 0.0])

		names.append("KneePitch")
		times.append([1.6, 2.52])
		keys.append([0.387463, -0.0698083])

		names.append("LElbowRoll")
		times.append([0.48, 0.84, 1.2, 1.56, 1.84, 2.56])
		keys.append([-1.52475, -1.20261, -1.47873, -
					 1.1352, -1.28107, -0.489305])

		names.append("LElbowYaw")
		times.append([0.48, 0.84, 1.2, 1.56, 2.56])
		keys.append([-0.702614, -0.199461, -0.684206, -0.254602, -1.17202])

		names.append("LHand")
		times.append([0.48, 0.84, 1.2, 1.56, 1.84, 2.56])
		keys.append([0.3028, 0, 0.304, 0, 0, 0.3])

		names.append("LShoulderPitch")
		times.append([0.48, 0.84, 1.2, 1.56, 1.84, 2.56])
		keys.append([1.24863, 1.04768, 1.24557, 1.07861, 1.22348, 1.53703])

		names.append("LShoulderRoll")
		times.append([0.48, 0.84, 1.2, 1.56, 2.56])
		keys.append([1.07376, 0.282215, 1.01086, 0.242414, 0.131882])

		names.append("LWristYaw")
		times.append([0.48, 0.84, 1.2, 1.56, 1.84, 2.56])
		keys.append([-0.820732, -1.13213, -0.849878, -
					 1.30693, -1.46782, 0.10427])

		names.append("RElbowRoll")
		times.append([0.44, 0.8, 1.16, 1.52, 1.8, 2.52])
		keys.append([1.54462, 1.12446, 1.50336, 1.20108, 1.31772, 0.43263])

		names.append("RElbowYaw")
		times.append([0.44, 0.8, 1.16, 1.52, 2.52])
		keys.append([0.681054, 0.251533, 0.66418, 0.197927, 1.16273])

		names.append("RHand")
		times.append([0.44, 0.8, 1.16, 1.52, 1.8, 2.52])
		keys.append([0.3048, 0, 0.3048, 0, 0, 0.302])

		names.append("RShoulderPitch")
		times.append([0.44, 0.8, 1.16, 1.52, 1.8, 2.52])
		keys.append([1.2119, 1.07998, 1.20883, 0.993092, 1.22348, 1.52944])

		names.append("RShoulderRoll")
		times.append([0.44, 0.8, 1.16, 1.52, 2.52])
		keys.append([-1.05543, -0.216335, -0.989473, -0.291418, -0.112024])

		names.append("RWristYaw")
		times.append([0.44, 0.8, 1.16, 1.52, 1.8, 2.52])
		keys.append([0.803775, 1.33607, 0.820649, 1.33692, 1.35612, 0.184038])

		return [names, keys, times]

	@staticmethod
	def close_eyes():

		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.96, 1.56, 2.36])
		keys.append([-1.56207, -1.56207, -0.539307])

		names.append("LElbowYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([-1.01578, -1.01578, -1.24617])

		names.append("LHand")
		times.append([0.96, 1.56, 2.36])
		keys.append([0.98, 0.02, 0.62])

		names.append("LShoulderPitch")
		times.append([0.96, 1.56, 2.36])
		keys.append([-0.0191986, -0.0191986, 1.61268])

		names.append("LWristYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([-1.44164, -1.44164, -0.0349066])

		names.append("RElbowRoll")
		times.append([0.96, 1.56, 2.36])
		keys.append([1.56207, 1.56207, 0.539307])

		names.append("RElbowYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([1.01578, 1.01578, 1.24617])

		names.append("RHand")
		times.append([0.96, 1.56, 2.36])
		keys.append([0.98, 0.02, 0.62])

		names.append("RShoulderPitch")
		times.append([0.96, 1.56, 2.36])
		keys.append([-0.0191986, -0.0191986, 1.61268])

		names.append("RWristYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([1.44164, 1.44164, 0.0349066])

		return [names, keys, times]

	@staticmethod
	def open_eyes():

		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.96, 1.56, 2.36])
		keys.append([-1.56207, -1.56207, -0.539307])

		names.append("LElbowYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([-1.01578, -1.01578, -1.24617])

		names.append("LHand")
		times.append([0.96, 1.56, 2.36])
		keys.append([0.02, 0.98, 0.62])

		names.append("LShoulderPitch")
		times.append([0.96, 1.56, 2.36])
		keys.append([-0.0191986, -0.0191986, 1.61268])

		names.append("LWristYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([-1.44164, -1.44164, -0.0349066])

		names.append("RElbowRoll")
		times.append([0.96, 1.56, 2.36])
		keys.append([1.56207, 1.56207, 0.539307])

		names.append("RElbowYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([1.01578, 1.01578, 1.24617])

		names.append("RHand")
		times.append([0.96, 1.56, 2.36])
		keys.append([0.02, 0.98, 0.62])

		names.append("RShoulderPitch")
		times.append([0.96, 1.56, 2.36])
		keys.append([-0.0191986, -0.0191986, 1.61268])

		names.append("RWristYaw")
		times.append([0.96, 1.56, 2.36])
		keys.append([1.44164, 1.44164, 0.0349066])

		return [names, keys, times]

	@staticmethod
	def applause():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.88, 1.24, 1.92, 2.36, 2.92])
		keys.append([-0.0802851, -0.437844, -0.523599, -0.3735, -0.523599])

		names.append("HeadYaw")
		times.append([1.24, 1.92, 2.92])
		# keys.append([0, 0, 8.06428e-07])
		keys.append([0.0, 0.0, 0.0])

		names.append("HipPitch")
		times.append([0.76, 2.8])
		keys.append([-0.00010896, -0.05951])

		names.append("HipRoll")
		times.append([0.76, 2.8])
		# keys.append([-1.0086e-06, -6.46786e-07])
		keys.append([0.0, 0.0])

		names.append("KneePitch")
		times.append([0.76, 2.8])
		keys.append([-0.069927, -0.0494623])

		names.append("LElbowRoll")
		times.append([1.12, 1.48, 1.8, 2.28, 2.84])
		keys.append([-1.38516, -0.994838, -1.37177, -1.16588, -0.52345])

		names.append("LElbowYaw")
		times.append([0.8, 1.12, 1.48, 1.8, 2.28, 2.84])
		keys.append([-1.58825, -0.834267, -1.309, -
					 0.850548, -1.51669, -1.22171])

		names.append("LHand")
		times.append([0.8, 1.12, 1.48, 1.8, 2.84])
		keys.append([0.89, 0.8, 0.93, 0.798435, 0])

		names.append("LShoulderPitch")
		times.append([0.8, 1.12, 1.8, 2.84])
		keys.append([0.762709, 0.337341, 0.339276, 1.56997])

		names.append("LShoulderRoll")
		times.append([1.12, 1.8, 2.84])
		keys.append([0.178024, 0.171035, 0.120074])

		names.append("LWristYaw")
		times.append([1.12, 1.8, 2.28, 2.84])
		# keys.append([-0.296706, -0.296332, -0.630064, -6.35377e-07])
		keys.append([-0.296706, -0.296332, -0.630064, 0.0])

		names.append("RElbowRoll")
		times.append([1.12, 1.48, 1.8, 2.24, 2.8])
		keys.append([1.38678, 1.09956, 1.37693, 1.2514, 0.52345])

		names.append("RElbowYaw")
		times.append([0.76, 1.12, 1.48, 1.8, 2.24, 2.8])
		keys.append([1.71042, 0.79587, 1.36136, 0.815262, 1.59349, 1.22171])

		names.append("RHand")
		times.append([0.76, 1.12, 1.48, 1.8, 2.8])
		keys.append([0.82, 0.763636, 0.87, 0.762275, 0])

		names.append("RShoulderPitch")
		times.append([0.76, 1.12, 1.8, 2.8])
		keys.append([0.733038, 0.301942, 0.304892, 1.56997])

		names.append("RShoulderRoll")
		times.append([1.12, 1.8, 2.8])
		keys.append([-0.164061, -0.158895, -0.120074])

		names.append("RWristYaw")
		times.append([1.12, 1.8, 2.24, 2.8])
		# keys.append([0.279253, 0.278518, 0.630064, -7.57089e-07])
		keys.append([0.279253, 0.278518, 0.630064, 0.0])

		return [names, keys, times]

	@staticmethod
	def rejected():

		names = list()
		times = list()
		keys = list()

		names.append("HeadYaw")
		times.append([0.8, 1.48, 2.36])
		keys.append([-0.610865, 0.610865, 0.0])

		names.append("LElbowRoll")
		times.append([0.8, 1.48, 2.36])
		keys.append([-0.895354, -0.308923, -0.741765])

		names.append("LElbowYaw")
		times.append([0.8, 2.36])
		keys.append([-0.190241, -1.23918])

		names.append("LShoulderPitch")
		times.append([0.8, 1.48, 2.36])
		keys.append([0.436332, 0.701622, 1.58999])

		names.append("LShoulderRoll")
		times.append([0.8, 1.48, 2.36])
		keys.append([-0.0826053, 0.607375, 0.123918])

		names.append("RElbowRoll")
		times.append([0.8, 1.48, 2.36])
		keys.append([0.895354, 0.308923, 0.741765])

		names.append("RElbowYaw")
		times.append([0.8, 2.36])
		keys.append([0.190241, 1.23918])

		names.append("RShoulderPitch")
		times.append([0.8, 1.48, 2.36])
		keys.append([0.699877, 0.701622, 1.58999])

		names.append("RShoulderRoll")
		times.append([0.8, 1.48, 2.36])
		keys.append([-0.00872665, -0.607375, -0.123918])

		return [names, keys, times]

	@staticmethod
	def strong_deception():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.96, 1.56, 1.88, 2.24, 2.8])
		keys.append([0.345577, 0.445059, 0.445059, 0.37671, 0.0])

		names.append("HeadYaw")
		times.append([0.76, 0.96, 1.56, 1.88, 2.8])
		keys.append([0.00349066, -0.389208, 0.392699, 0, 0])

		names.append("HipPitch")
		times.append([0.76, 1.56, 1.88, 2.24])
		keys.append([-0.500909, -0.455531, -0.455531, 0.0])

		names.append("LElbowRoll")
		times.append([0.76, 2.16])
		keys.append([-0.00872665, -0.0942478])

		names.append("LElbowYaw")
		times.append([0.76, 2.16])
		keys.append([-1.3226, -1.2898])

		names.append("LHand")
		times.append([0.76, 2.16])
		keys.append([0.66144, 0.75])

		names.append("LShoulderPitch")
		times.append([0.76, 1.56, 1.88, 2.12, 2.16])
		keys.append([1.54636, 1.23569, 1.23569, 1.2322, 1.23395])

		names.append("LShoulderRoll")
		times.append([0.76, 2.12, 2.16])
		keys.append([0.0645772, 0.0558505, 0.0506146])

		names.append("LWristYaw")
		times.append([0.76, 2.16])
		keys.append([-0.696386, -0.630064])

		names.append("RElbowRoll")
		times.append([1.56, 1.88, 2.12])
		keys.append([0.164061, 0.164061, 0.0942478])

		names.append("RElbowYaw")
		times.append([2.12])
		keys.append([1.2898])

		names.append("RHand")
		times.append([1.56, 1.88, 2.12])
		keys.append([0.84, 0.84, 0.75])

		names.append("RShoulderPitch")
		times.append([1.56, 1.88, 2.12, 2.16])
		keys.append([1.23569, 1.23569, 1.2322, 1.23395])

		names.append("RShoulderRoll")
		times.append([2.12])
		keys.append([-0.0558505])

		names.append("RWristYaw")
		times.append([2.12])
		keys.append([0.630064])

		return [names, keys, times]

	@staticmethod
	def Hey_3():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.72, 1.32, 1.72])
		keys.append([-0.31765, -0.471239, -0.523599])

		names.append("HeadYaw")
		times.append([1.32, 1.72])
		keys.append([0, 0])

		names.append("HipPitch")
		times.append([1.2])
		keys.append([-0.0599238])

		names.append("HipRoll")
		times.append([1.2])
		keys.append([5.14422e-07])

		names.append("KneePitch")
		times.append([1.2])
		keys.append([-0.0499168])

		names.append("LElbowRoll")
		times.append([0.64, 1.24, 1.64])
		keys.append([-0.560251, -0.768491, -0.76389])

		names.append("LElbowYaw")
		times.append([0.64, 1.24, 1.64])
		keys.append([-1.44164, -1.38831, -1.38831])

		names.append("LHand")
		times.append([1.64])
		keys.append([0.162935])

		names.append("LShoulderPitch")
		times.append([1.24, 1.64])
		keys.append([1.5447, 1.5447])

		names.append("LShoulderRoll")
		times.append([1.24, 1.64])
		keys.append([0.030638, 0.033706])

		names.append("LWristYaw")
		times.append([1.64])
		keys.append([-0.239346])

		names.append("RElbowRoll")
		times.append([0.56, 0.92, 1.16, 1.56])
		keys.append([1.44862, 1.01555, 1.56207, 1.01862])

		names.append("RElbowYaw")
		times.append([0.56, 0.92, 1.16, 1.56])
		keys.append([0.947714, 1.88984, 1.22102, 1.89906])

		names.append("RHand")
		times.append([0.56, 0.92, 1.56])
		keys.append([0.9, 0.890909, 0.890933])

		names.append("RShoulderPitch")
		times.append([0.92, 1.16, 1.56])
		keys.append([-0.024502, -0.276078, -0.0291041])

		names.append("RShoulderRoll")
		times.append([0.56, 0.92, 1.16, 1.56])
		keys.append([-0.685914, -0.834538, -0.889762, -0.849878])

		names.append("RWristYaw")
		times.append([0.56, 0.92, 1.56])
		keys.append([-0.994838, -0.349066, -0.345191])

		return [names, keys, times]

	@staticmethod
	def Hey_4():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.72, 1.4, 1.92])
		keys.append([-0.242601, -0.471239, -0.523599])

		names.append("HeadYaw")
		times.append([1.4, 1.92])
		keys.append([0, 0])

		names.append("HipPitch")
		times.append([1.28])
		keys.append([-0.0599063])

		names.append("HipRoll")
		times.append([1.28])
		keys.append([5.14422e-07])

		names.append("KneePitch")
		times.append([1.28])
		keys.append([-0.0498977])

		names.append("LElbowRoll")
		times.append([1.32, 1.72])
		keys.append([-0.414139, -0.366584])

		names.append("LElbowYaw")
		times.append([1.32, 1.72])
		keys.append([-1.25946, -1.34843])

		names.append("LHand")
		times.append([1.32, 1.72])
		keys.append([0.22948, 0.22948])

		names.append("LShoulderPitch")
		times.append([1.32, 1.72])
		keys.append([1.53703, 1.55697])

		names.append("LShoulderRoll")
		times.append([1.32, 1.72])
		keys.append([0.108872, 0.124212])

		names.append("LWristYaw")
		times.append([1.32, 1.72])
		keys.append([-0.366667, -0.417291])

		names.append("RElbowRoll")
		times.append([0.56, 0.96, 1.24, 1.64])
		keys.append([1.0821, 1.39277, 1.22111, 0.986404])

		names.append("RElbowYaw")
		times.append([0.56, 0.96, 1.24, 1.64])
		keys.append([-0.0383972, 0.226893, 1.22256, 2.0856])

		names.append("RHand")
		times.append([0.56, 1.24, 1.64])
		keys.append([0.82, 0.818182, 0.819296])

		names.append("RShoulderPitch")
		times.append([0.56, 1.24, 1.64])
		keys.append([0.0994838, -0.477032, 0.0261199])

		names.append("RShoulderRoll")
		times.append([0.56, 0.96, 1.24, 1.64])
		keys.append([-0.574213, -0.361283, -0.408086, -0.760906])

		names.append("RWristYaw")
		times.append([0.56, 1.24, 1.64])
		keys.append([-0.762709, -0.855211, -0.83914])

		return [names, keys, times]

	@staticmethod
	def Me_1():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.44, 0.76, 1.04])
		keys.append([-0.303687, -0.471239, -0.523599])

		names.append("HeadYaw")
		times.append([0.76, 1.04])
		keys.append([6.33429e-07, 4.69956e-07])

		names.append("HipPitch")
		times.append([0.64, 0.92])
		keys.append([-0.0601011, -0.0600997])

		names.append("HipRoll")
		times.append([0.64, 0.92])
		keys.append([-7.07461e-07, -5.92168e-07])

		names.append("KneePitch")
		times.append([0.64, 0.92])
		keys.append([-0.0501103, -0.0501089])

		names.append("LElbowRoll")
		times.append([0.36, 0.68, 0.96])
		keys.append([-0.685914, -1.43466, -1.44862])

		names.append("LElbowYaw")
		times.append([0.36, 0.68, 0.96])
		keys.append([-1.51669, -0.909316, -0.872665])

		names.append("LHand")
		times.append([0.36, 0.68, 0.96])
		keys.append([0.91, 0.8, 0.74])

		names.append("LShoulderPitch")
		times.append([0.68, 0.96])
		keys.append([0.610865, 0.610865])

		names.append("LShoulderRoll")
		times.append([0.68, 0.96])
		keys.append([0.249582, 0.249582])

		names.append("LWristYaw")
		times.append([0.36, 0.68, 0.96])
		keys.append([-0.994838, -0.79587, -0.79587])

		names.append("RElbowRoll")
		times.append([0.32, 0.64, 0.92])
		keys.append([0.588176, 0.522443, 0.47473])

		names.append("RElbowYaw")
		times.append([0.64, 0.92])
		keys.append([1.22296, 1.22296])

		names.append("RHand")
		times.append([0.32, 0.64, 0.92])
		keys.append([0.1, 0.17, 0.1])

		names.append("RShoulderPitch")
		times.append([0.64, 0.92])
		keys.append([1.56614, 1.56614])

		names.append("RShoulderRoll")
		times.append([0.64, 0.92])
		keys.append([-0.130365, -0.130366])

		names.append("RWristYaw")
		times.append([0.32, 0.64, 0.92])
		keys.append([0.165806, 6.43787e-07, -1.12766e-07])

		return [names, keys, times]

	@staticmethod
	def Me_8():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.6, 0.92, 1.28])
		keys.append([-0.310669, -0.471239, -0.523599])

		names.append("HeadYaw")
		times.append([0.92, 1.28])
		keys.append([0, 0])

		names.append("HipPitch")
		times.append([0.8])
		keys.append([-0.0591122])

		names.append("HipRoll")
		times.append([0.8])
		keys.append([-7.09139e-07])

		names.append("KneePitch")
		times.append([0.8])
		keys.append([-0.0490258])

		names.append("LElbowRoll")
		times.append([0.52, 0.84, 1.2])
		keys.append([-0.757473, -1.32518, -1.40674])

		names.append("LElbowYaw")
		times.append([0.52, 0.84, 1.2])
		keys.append([-1.40324, -0.859847, -0.759218])

		names.append("LHand")
		times.append([0.52, 0.84, 1.2])
		keys.append([0.88, 0.756766, 0.733944])

		names.append("LShoulderPitch")
		times.append([0.84, 1.2])
		keys.append([0.539895, 0.497419])

		names.append("LShoulderRoll")
		times.append([0.84, 1.2])
		keys.append([0.298474, 0.305433])

		names.append("LWristYaw")
		times.append([0.52, 0.84, 1.2])
		keys.append([-1.22697, -0.792763, -0.712356])

		names.append("RElbowRoll")
		times.append([0.48, 0.8, 1.16])
		keys.append([0.544543, 1.27489, 1.40674])

		names.append("RElbowYaw")
		times.append([0.48, 0.8, 1.16])
		keys.append([1.40324, 0.859847, 0.759218])

		names.append("RHand")
		times.append([0.48, 0.8, 1.16])
		keys.append([0.92, 0.781361, 0.755687])

		names.append("RShoulderPitch")
		times.append([0.8, 1.16])
		keys.append([0.539895, 0.497419])

		names.append("RShoulderRoll")
		times.append([0.8, 1.16])
		keys.append([-0.298474, -0.305433])

		names.append("RWristYaw")
		times.append([0.48, 0.8, 1.16])
		keys.append([0.961676, 0.808428, 0.780049])

		return [names, keys, times]

	@staticmethod
	def ShowMuscles_1():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.56, 0.96, 1.36])
		keys.append([0.242601, 0.184961, -0.238424])

		names.append("HeadYaw")
		times.append([0.56, 0.96, 1.36])
		keys.append([-0.503194, -0.47865, -0.0890139])

		names.append("RElbowRoll")
		times.append([0.8, 1.2])
		keys.append([1.06814, 0.388144])

		names.append("RElbowYaw")
		times.append([0.8, 1.2])
		keys.append([1.44164, 1.40324])

		names.append("RHand")
		times.append([0.8, 1.2])
		keys.append([0.03, 0.302])

		names.append("RShoulderPitch")
		times.append([0.8, 1.2])
		keys.append([0.47473, 0.785451])

		names.append("RShoulderRoll")
		times.append([0.8, 1.2])
		keys.append([-0.150098, -0.164061])

		names.append("RWristYaw")
		times.append([0.8, 1.2])
		keys.append([0.851721, 1.32645])

		return [names, keys, times]

	@staticmethod
	def ShowMuscles_4():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.76, 1, 1.36, 1.84, 2.4, 2.96])
		keys.append([-0.473126, -0.519146, -0.644934, -
					 0.724701, -0.0628318, -0.348872])

		names.append("HeadYaw")
		times.append([0.76, 1, 1.36, 1.84, 2.96])
		keys.append([0.013764, 0.015298, 0.0352401, 0.0475121, -0.00464395])

		# names.append("HipPitch")
		# times.append([1.24, 1.72, 2.84])
		# keys.append([-0.780162, -0.79006, 1.12516e-07])

		# names.append("HipRoll")
		# times.append([1.72, 2.84])
		# keys.append([-1.16874e-05, 5.47648e-14])

		# names.append("KneePitch")
		# times.append([1.24, 1.72, 2.84])
		# keys.append([0.42237, 0.4009, -0.0698099])

		names.append("LElbowRoll")
		times.append([0.64, 0.88, 1.04, 1.24, 1.76, 2.32, 2.88])
		keys.append([-0.466294, -0.375789, -1.36485, -
					 1.25324, -1.33692, -1.15715, -0.483168])

		names.append("LElbowYaw")
		times.append([0.64, 0.88, 1.24, 1.76, 2.88])
		keys.append([-0.564555, -0.570689, -0.259288, -0.250085, -1.17202])

		names.append("LHand")
		times.append([0.64, 0.88, 1.24, 1.76, 2.88])
		keys.append([0.7552, 0.7552, 0, 0.2232, 0.3])

		names.append("LShoulderPitch")
		times.append([0.64, 0.88, 1.24, 1.76, 2.88])
		keys.append([1.18574, 1.20415, 0.991347, 1.0124, 1.53703])

		names.append("LShoulderRoll")
		times.append([0.64, 0.88, 1.24, 1.76, 2.88])
		keys.append([0.868202, 0.908086, 0.496974, 0.446352, 0.130348])

		names.append("LWristYaw")
		times.append([0.64, 0.88, 1.24, 1.76, 2.88])
		keys.append([-0.742498, -0.744032, -1.53864, -1.53864, 0.105804])

		names.append("RElbowRoll")
		times.append([0.56, 0.88, 1.04, 1.24, 1.68, 2.24, 2.8])
		keys.append([0.441834, 0.389678, 1.40324,
					 1.19656, 1.26536, 1.1397, 0.43263])

		names.append("RElbowYaw")
		times.append([0.56, 0.88, 1.24, 1.68, 2.8])
		keys.append([0.075124, 0.078192, 0.194775, 0.168698, 1.16273])

		names.append("RHand")
		times.append([0.56, 0.88, 1.24, 1.68, 2.8])
		keys.append([0.6988, 0.6992, 0, 0.0348, 0.3016])

		names.append("RShoulderPitch")
		times.append([0.56, 0.88, 1.24, 1.68, 2.8])
		keys.append([0.997141, 1.00481, 1.01753, 0.994073, 1.52944])

		names.append("RShoulderRoll")
		times.append([0.56, 0.88, 1.24, 1.68, 2.8])
		keys.append([-0.808459, -0.845275, -0.464844, -0.412688, -0.107422])

		names.append("RWristYaw")
		times.append([0.56, 0.88, 1.24, 1.68, 2.8])
		keys.append([1.10137, 1.10137, 1.58305, 1.56464, 0.177901])

		return [names, keys, times]

	@staticmethod
	def Listen_1():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.52, 1.48])
		keys.append([-0.200952, -0.219359])

		names.append("HeadYaw")
		times.append([0.52, 1.48])
		keys.append([-0.00766993, 0.891243])

		names.append("LElbowRoll")
		times.append([0.52, 1.48])
		keys.append([-0.52002, -0.521554])

		names.append("LElbowYaw")
		times.append([0.52, 1.48])
		keys.append([-1.21951, -1.21645])

		names.append("LHand")
		times.append([0.52, 1.48])
		keys.append([0.592267, 0.593146])

		names.append("LShoulderPitch")
		times.append([0.52, 1.48])
		keys.append([1.56773, 1.56926])

		names.append("LShoulderRoll")
		times.append([0.52, 1.48])
		keys.append([0.118117, 0.119651])

		names.append("LWristYaw")
		times.append([0.52, 1.48])
		keys.append([-0.0261199, -0.0153821])

		names.append("RElbowRoll")
		times.append([0.52, 1.48])
		keys.append([0.516952, 1.55852])

		names.append("RElbowYaw")
		times.append([0.52, 1.48])
		keys.append([1.21951, 1.21491])

		names.append("RHand")
		times.append([0.52, 1.48])
		keys.append([0.595782, 0.958699])

		names.append("RShoulderPitch")
		times.append([0.52, 1.48])
		keys.append([1.56773, -0.111981])

		names.append("RShoulderRoll")
		times.append([0.52, 1.48])
		keys.append([-0.115049, -0.199418])

		names.append("RWristYaw")
		times.append([0.52, 1.48])
		keys.append([-0.023052, -0.153442])

		return [names, keys, times]

	@staticmethod
	def ScratchHead_1():
		### Keywords: Head ###
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.72, 1.36, 2.68])
		keys.append([-0.228638, 0.178518, 0.219911])

		names.append("HeadYaw")
		times.append([1.36, 2.68])
		keys.append([0.287208, 0.294486])

		names.append("HipPitch")
		times.append([1.24])
		keys.append([-0.0599039])

		names.append("HipRoll")
		times.append([1.24])
		keys.append([-5.73121e-07])

		names.append("KneePitch")
		times.append([1.24])
		keys.append([-0.0499468])

		names.append("LElbowRoll")
		times.append([0.64, 1.28, 2.6])
		keys.append([-0.630064, -0.296966, -0.263545])

		names.append("LElbowYaw")
		times.append([1.28, 2.6])
		keys.append([-1.18738, -1.18609])

		names.append("LHand")
		times.append([0.64, 1.28, 2.6])
		keys.append([0.23, 0.361079, 0.37])

		names.append("LShoulderPitch")
		times.append([1.28, 2.6])
		keys.append([1.51399, 1.51476])

		names.append("LShoulderRoll")
		times.append([1.28, 2.6])
		keys.append([0.117113, 0.111275])

		names.append("LWristYaw")
		times.append([1.28, 2.6])
		keys.append([-7.12869e-07, -7.12869e-07])

		names.append("RElbowRoll")
		times.append([0.56, 1.2, 2.52])
		keys.append([0.574213, 1.12554, 1.18159])

		names.append("RElbowYaw")
		times.append([0.56, 1.2, 2.52])
		keys.append([1.36485, 0.883231, 0.834267])

		names.append("RHand")
		times.append([0.56, 1.2, 1.52, 1.76, 2.08, 2.32, 2.52])
		keys.append([0.72, 0.611074, 0.33, 0.65, 0.38, 0.59, 0.64])

		names.append("RShoulderPitch")
		times.append([1.2, 2.52])
		keys.append([-0.417472, -0.467748])

		names.append("RShoulderRoll")
		times.append([0.56, 1.2, 2.52])
		keys.append([-0.136136, -0.27763, -0.29147])

		names.append("RWristYaw")
		times.append([0.56, 1.2, 2.52])
		keys.append([0.928515, 1.10912, 1.12748])

		return [names, keys, times]

	@staticmethod
	def IDontKnow_4():
		### Keywords: Not Understand ###

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.48, 0.96, 1.76, 2.12])
		keys.append([-0.0420715, -0.0420715, -0.324631, -0.523599])

		names.append("HeadYaw")
		times.append([0.48, 0.96, 1.4, 2.12])
		keys.append([-0.434165, 0.14262, -0.296706, 0])

		names.append("HipPitch")
		times.append([1.64])
		keys.append([-0.213223])

		names.append("HipRoll")
		times.append([1.64])
		keys.append([-0.00920387])

		names.append("KneePitch")
		times.append([1.64])
		keys.append([0.0762543])

		names.append("LElbowRoll")
		times.append([0.68, 1.68, 2.04])
		keys.append([-0.882007, -0.501576, -0.500042])

		names.append("LElbowYaw")
		times.append([0.68, 1.68, 2.04])
		keys.append([-0.224006, -1.89607, -1.90834])

		names.append("LHand")
		times.append([1.68, 2.04])
		keys.append([0.690569, 0.690933])

		names.append("LShoulderPitch")
		times.append([0.68, 1.68, 2.04])
		keys.append([1.10904, 1.42965, 1.43425])

		names.append("LShoulderRoll")
		times.append([0.68, 1.68, 2.04])
		keys.append([0.162562, 0.25767, 0.282215])

		names.append("LWristYaw")
		times.append([1.68, 2.04])
		keys.append([-0.894364, -0.890118])

		names.append("RElbowRoll")
		times.append([0.64, 1.64, 2])
		keys.append([0.879025, 0.44797, 0.415757])

		names.append("RElbowYaw")
		times.append([0.64, 1.64, 2])
		keys.append([0.777696, 2.08007, 2.0856])

		names.append("RHand")
		times.append([1.64, 2])
		keys.append([0.673842, 0.671296])

		names.append("RShoulderPitch")
		times.append([0.64, 1.64, 2])
		keys.append([1.38985, 1.48189, 1.47575])

		names.append("RShoulderRoll")
		times.append([0.64, 1.64, 2])
		keys.append([-0.138102, -0.260822, -0.288433])

		names.append("RWristYaw")
		times.append([1.64, 2])
		keys.append([0.766959, 0.771436])

		return [names, keys, times]

	@staticmethod
	def No_8():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.44, 1.08, 1.76])
		keys.append([-0.152002, -0.068944, -0.161279])

		names.append("HeadYaw")
		times.append([0.44, 0.88, 1.36, 1.76])
		keys.append([-0.440631, 0.272853, -0.146715, -0.00158487])

		names.append("HipPitch")
		times.append([1.44])
		keys.append([-0.213223])

		names.append("HipRoll")
		times.append([1.44])
		keys.append([-0.00920389])

		names.append("KneePitch")
		times.append([1.44])
		keys.append([0.0762569])

		names.append("LElbowRoll")
		times.append([0.52, 1, 1.52])
		keys.append([-0.575208, -0.46476, -0.377323])

		names.append("LElbowYaw")
		times.append([0.52, 1, 1.52])
		keys.append([-0.900499, -1.00174, -1.1306])

		names.append("LHand")
		times.append([1.52])
		keys.append([0.111663])

		names.append("LShoulderPitch")
		times.append([0.52, 1, 1.52])
		keys.append([1.36829, 1.42965, 1.45419])

		names.append("LShoulderRoll")
		times.append([0.52, 1, 1.52])
		keys.append([0.015298, 0.05825, 0.06592])

		names.append("LWristYaw")
		times.append([1.52])
		keys.append([-0.196393])

		names.append("RElbowRoll")
		times.append([0.36, 0.84, 1.36])
		keys.append([0.742498, 0.650458, 0.572224])

		names.append("RElbowYaw")
		times.append([0.36, 0.84, 1.36])
		keys.append([0.882007, 1.19801, 1.46646])

		names.append("RHand")
		times.append([1.36])
		keys.append([0.218935])

		names.append("RShoulderPitch")
		times.append([0.36, 0.84, 1.36])
		keys.append([1.50183, 1.54631, 1.57239])

		names.append("RShoulderRoll")
		times.append([0.36, 0.84, 1.36])
		keys.append([-0.00924597, -0.016916, -0.030722])

		names.append("RWristYaw")
		times.append([1.36])
		keys.append([0.030638])

		return [names, keys, times]

	@staticmethod
	def Plenty_1():
		### Keywords: Plenty ###

		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.56])
		keys.append([-0.530757])

		names.append("LElbowYaw")
		times.append([0.56])
		keys.append([-1.22258])

		names.append("LHand")
		times.append([0.56])
		keys.append([0.592267])

		names.append("LShoulderPitch")
		times.append([0.56])
		keys.append([1.56926])

		names.append("LShoulderRoll")
		times.append([0.56])
		keys.append([0.125787])

		names.append("LWristYaw")
		times.append([0.56])
		keys.append([-0.0138481])

		names.append("RElbowRoll")
		times.append([0.56])
		keys.append([1.15816])

		names.append("RElbowYaw")
		times.append([0.56])
		keys.append([1.17963])

		names.append("RHand")
		times.append([0.56, 0.76, 0.88, 1, 1.16])
		keys.append([0.594025, 0.02, 0.55, 0.02, 0.55])

		names.append("RShoulderPitch")
		times.append([0.56])
		keys.append([1.04924])

		names.append("RShoulderRoll")
		times.append([0.56])
		keys.append([-0.0736311])

		names.append("RWristYaw")
		times.append([0.56])
		keys.append([1.35295])

		return [names, keys, times]

	@staticmethod
	def Sphere_1():
		### Keywords: Sphere ###

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.52, 1.24, 2.16])
		keys.append([-0.151844, 0.363554, 0.0720971])

		names.append("HeadYaw")
		times.append([0.52, 1.24, 2.16])
		keys.append([0.00613594, 0.00613594, 0.00613595])

		names.append("LElbowRoll")
		times.append([0.52, 1.24, 2.16])
		keys.append([-1.19344, -1.15969, -1.19344])

		names.append("LElbowYaw")
		times.append([0.52, 1.24, 2.16])
		keys.append([-1.27934, -0.918854, -1.27934])

		names.append("LHand")
		times.append([0.52, 1.24, 2.16])
		keys.append([0.543937, 0.485062, 0.543937])

		names.append("LShoulderPitch")
		times.append([0.52, 1.24, 2.16])
		keys.append([1.03544, 0.343612, 1.03544])

		names.append("LShoulderRoll")
		times.append([0.52, 1.24, 2.16])
		keys.append([0.076699, 0.0168738, 0.076699])

		names.append("LWristYaw")
		times.append([0.52, 1.24, 2.16])
		keys.append([-0.29457, 0.394196, -0.29457])

		names.append("RElbowRoll")
		times.append([0.52, 1.24, 2.16])
		keys.append([1.31309, 0.615126, 1.31309])

		names.append("RElbowYaw")
		times.append([0.52, 1.24, 2.16])
		keys.append([1.40206, 0.80534, 1.40206])

		names.append("RHand")
		times.append([0.52, 1.24, 2.16])
		keys.append([0.577329, 0.577329, 0.577329])

		names.append("RShoulderPitch")
		times.append([0.52, 1.24, 2.16])
		keys.append([1.15509, 0.817612, 1.15509])

		names.append("RShoulderRoll")
		times.append([0.52, 1.24, 2.16])
		keys.append([-0.0889709, -0.00872665, -0.088971])

		names.append("RWristYaw")
		times.append([0.52, 1.24, 2.16])
		keys.append([-0.142704, 1.44499, -0.142704])

		return [names, keys, times]

	@staticmethod
	def ComeOn_():
		### Keywords: Come ###

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.92, 1.4, 1.88, 2.24, 3.24])
		keys.append([-0.331998, 0.0296706, -0.370348, -0.413299, -0.523599])

		names.append("HeadYaw")
		times.append([0.92, 1.88, 2.24, 3.24])
		keys.append([-0.039926, -0.039926, -0.04913, 0])

		names.append("LElbowRoll")
		times.append([0.64, 0.84, 1.8, 2.16, 2.48, 3.16])
		keys.append([-1.51402, -1.51402, -1.51402, -
					 1.51402, -1.0821, -0.598219])

		names.append("LElbowYaw")
		times.append([0.64, 0.84, 1.8, 2.16, 2.48, 3.16])
		keys.append([-0.586029, -0.586029, -0.586029, -
					 0.592166, -1.02451, -1.21497])

		names.append("LHand")
		times.append([0.64, 0.84, 1.8, 2.16, 2.48, 3.16])
		keys.append([0.7228, 0.7228, 0.7224, 0.7224, 0.82, 0.234])

		names.append("LShoulderPitch")
		times.append([0.64, 0.84, 1.8, 2.16, 3.16])
		keys.append([1.83769, 1.83769, 1.8423, 1.83923, 1.62753])

		names.append("LShoulderRoll")
		times.append([0.64, 0.84, 1.8, 2.16, 3.16])
		keys.append([0.638103, 0.638103, 0.641169, 0.638103, 0.174835])

		names.append("LWristYaw")
		times.append([0.64, 0.84, 1.8, 2.16, 2.48, 3.16])
		keys.append([0.151824, 0.151824, 0.151824,
					 0.151824, -0.464258, 0.124212])

		names.append("RElbowRoll")
		times.append([0.56, 0.76, 1.24, 1.72, 2.08, 2.4, 3.08])
		keys.append([0.316046, 0.316046, 0.685914,
					 0.921534, 1.23951, 1.45037, 0.444902])

		names.append("RElbowYaw")
		times.append([0.56, 0.76, 1.24, 1.72, 2.08, 2.4, 3.08])
		keys.append([1.04154, 1.04154, 1.31598,
					 1.31598, 1.28085, 1.38056, 1.18574])

		names.append("RHand")
		times.append([0.56, 0.76, 1, 1.24, 1.48, 1.72, 2.08, 3.08])
		keys.append([0.3, 0.3, 0.9, 0.4, 0.8, 0.4008, 0.3, 0.406])

		names.append("RShoulderPitch")
		times.append([0.56, 0.76, 1.72, 2.08, 3.08])
		keys.append([0.0798099, 0.0798099, 0.390954, 0.619779, 1.49262])

		names.append("RShoulderRoll")
		times.append([0.56, 0.76, 1.72, 2.08, 3.08])
		keys.append([-0.11049, -0.11049, -0.116626, -0.219911, -0.112024])

		names.append("RWristYaw")
		times.append([0.56, 0.76, 1.24, 1.72, 2.08, 2.4, 3.08])
		keys.append([1.7794, 1.7794, 1.45037, 1.52542,
					 1.51095, 1.54287, 0.190175])

		return [names, keys, times]

	@staticmethod
	def monster():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1, 1.76, 2.12, 2.52, 2.92])
		keys.append([0.31535, -0.483863, -0.577437, -0.597379, -0.305433])

		names.append("HeadYaw")
		times.append([1, 1.76, 2.12, 2.52, 2.92])
		keys.append([-0.107422, 0.0444441, 0.015298, -0.138102, 0.0663225])

		names.append("HipPitch")
		times.append([1.56, 2.92])
		keys.append([-0.623083, -0.321141])

		names.append("HipRoll")
		times.append([1.56, 2.92])
		keys.append([-0.122173, 0])

		names.append("KneePitch")
		times.append([1.56])
		keys.append([0.20944])

		names.append("LElbowRoll")
		times.append([0.88, 1.64, 2, 2.24, 2.4, 2.92])
		keys.append([-0.870919, -0.828318, -0.739346, -
					 0.715585, -1.52322, -0.5044])

		names.append("LElbowYaw")
		times.append([0.88, 1.64, 2, 2.24, 2.4, 2.92])
		keys.append([0.0750492, -1.63682, -0.6704, -
					 0.977384, 0.121144, -1.26013])

		names.append("LHand")
		times.append([0.88, 1.64, 2, 2.4, 2.92])
		keys.append([0.449091, 0.581818, 0.110208, 0.109844, 0.6])

		names.append("LShoulderPitch")
		times.append([0.88, 1.64, 2, 2.4, 2.92])
		keys.append([0.753151, -0.188724, -1.17202, 0.383972, 1.48702])

		names.append("LShoulderRoll")
		times.append([0.88, 1.64, 2, 2.4, 2.92])
		keys.append([0.460767, 1.00473, 0.888144, 0.0291041, 0.109956])

		names.append("LWristYaw")
		times.append([0.88, 1.64, 2, 2.4, 2.92])
		keys.append([-0.165714, -0.162646, -0.168782, -0.139636, 0.0174533])

		names.append("RElbowRoll")
		times.append([0.72, 1.48, 1.72, 1.84, 2.24, 2.92])
		keys.append([1.16588, 0.517, 0.610865, 1.52177, 1.03703, 0.5044])

		names.append("RElbowYaw")
		times.append([0.72, 1.48, 1.72, 1.85, 2.24, 2.92])
		keys.append([0.322099, 0.481634, 0.575959, -
					 0.323717, 1.11364, 1.26013])

		names.append("RHand")
		times.append([0.72, 1.48, 1.84, 2.24, 2.92])
		keys.append([0.54, 0.618182, 0.219662, 0.217116, 0.6])

		names.append("RShoulderPitch")
		times.append([0.72, 1.48, 1.84, 2.24, 2.92])
		keys.append([1.01708, -0.782298, 0.176453, 1.23645, 1.48702])

		names.append("RShoulderRoll")
		times.append([0.72, 1.48, 1.84, 2.24, 2.92])
		keys.append([-0.547679, -1.13674, -0.046062, -0.24088, -0.109956])

		names.append("RWristYaw")
		times.append([0.72, 1.48, 1.84, 2.24, 2.92])
		keys.append([0.00302603, 0.558505, -0.0445279, -0.0629359, -0.0174533])

		return [names, keys, times]

	@staticmethod
	def confused():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.96, 1.44, 2.24])
		keys.append([0.291345, 0.291344, 0.291344])

		names.append("HeadYaw")
		times.append([0.96, 1.44, 2.24])
		keys.append([0, 0, 0])

		names.append("LElbowRoll")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([-1.56207, -1.56207, -1.56207, -0.527089])

		names.append("LElbowYaw")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([-0.97913, -0.97913, -0.97913, -1.25664])

		names.append("LHand")
		times.append([0.96, 1.44, 1.84, 2.24, 2.64, 3.04, 3.6])
		keys.append([0.75, 0.33, 0.96, 0.33, 0.96, 0.96, 0.61])

		names.append("LShoulderPitch")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([-0.494728, -0.494728, -0.494728, 1.59349])

		names.append("LShoulderRoll")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([0.113446, 0.113446, 0.113446, 0.113446])

		names.append("LWristYaw")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([-0.640536, -0.640536, -0.640536, 0.010472])

		names.append("RElbowRoll")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([1.56207, 1.56207, 1.56207, 0.527089])

		names.append("RElbowYaw")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([1.95302, 1.95302, 1.95302, 1.25664])

		names.append("RHand")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([0.63, 0.63, 0.63, 0.61])

		names.append("RShoulderPitch")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([1.03149, 1.03149, 1.03149, 1.59349])

		names.append("RShoulderRoll")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([-0.5044, -0.5044, -0.5044, 0.113446])

		names.append("RWristYaw")
		times.append([0.96, 1.44, 2.24, 3.6])
		keys.append([0.640536, 0.640536, 0.640536, -0.010472])

		return [names, keys, times]

	# NARROB movements

	@staticmethod
	def AgoMotion():
		names = list()
		times = list()
		keys = list()

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([0.403484, 0.403484, 0.408086, 0.512398, 0.543078, 1.22111, 0.981802, 0.921976, 0.604438, 0.231676, 0.230142])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([-0.127364, -0.127364, -0.12583, 0.16563, 1.67355, 1.82849, 1.84843, 1.65821, -0.257754, -0.415756, -0.415756])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([0.1356, 0.1356, 0.1356, 0.1356, 0.1356, 0.1356, 0.1356, 0.1356, 0.1356, 0.1356, 0.1356])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([1.23184, 1.23338, 1.23184, 0.814596, -0.271476, -0.44175, -0.524586, -0.475498, 0.6704, 1.25025, 1.25025])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([-0.108956, -0.108956, -0.0782759, 0.118076, 0.210116, 0.0659201, 0.0183661, -0.00924587, -0.0614018, -0.151908, -0.096684])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([1.73798, 1.73798, 1.74565, 1.82387, 1.82387, 1.82387, 1.82387, 1.82387, 1.82387, 1.82387, 1.82387])

		return [names, keys, times]

	@staticmethod
	def AngryAgMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([-0.159578, -0.159578, -0.159578, -0.645856, -0.671952, -0.671952, -0.671952, -0.671952, -0.671952,
					 -0.671952, -0.671952, -0.671952, -0.671952, -0.671952, -0.115092, -0.101286, -0.101286])

		names.append("HeadYaw")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[-0.0107799, -0.0107799, -0.0107799, -0.0383921, -0.0506639, -0.0506639, -0.0506639, -0.0521979, -0.0521979,
			 -0.0537319, -0.0521979, -0.0521979, -0.0521979, -0.0521979, -0.01845, -0.0138481, -0.0138481])

		names.append("LElbowRoll")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[-0.415672, -0.415672, -0.415672, -0.414138, -0.414138, -0.561402, -0.635034, -1.09523, -1.11978, -1.0891,
			 -0.791502, -0.383458, -0.865134, -0.8636, -0.8636, -0.8636, -0.8636])

		names.append("LElbowYaw")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[-1.17815, -1.17815, -1.17815, -1.17815, -1.17815, -1.17969, -1.12907, -0.250084, -0.016916, -0.636652,
			 -0.730226, -0.58603, -0.0399261, -0.0399261, -0.042994, -0.042994, -0.04146])

		names.append("LHand")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[0.2952, 0.2952, 0.2952, 0.2952, 0.2952, 0.2952, 0.2948, 0.2952, 0.4768, 0.4768, 0.4764, 0.4764, 0.6136,
			 0.6136, 0.6136, 0.6136, 0.6136])

		names.append("LShoulderPitch")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[1.46033, 1.46033, 1.46033, 1.46033, 1.46339, 1.29772, 0.38039, 0.07359, 0.25767, 0.26534, 1.0937, 1.34067,
			 1.37289, 1.37289, 1.37289, 1.37289, 1.37289])

		names.append("LShoulderRoll")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[0.156426, 0.156426, 0.156426, 0.151824, 0.15029, 0.136484, -0.208666, -0.314159, -0.314159, -0.17952,
			 0.374254, 0.323632, 0.39573, 0.39573, 0.39573, 0.39573, 0.39573])

		names.append("LWristYaw")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([0.11194, 0.11194, 0.11194, 0.11194, 0.11194, 0.113474, -0.104354, -0.507796, -0.656594, -0.806926,
					 -0.782382, -0.605972, -0.829936, -0.83147, -0.83147, -0.829936, -0.829936])

		names.append("RElbowRoll")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[0.414222, 0.414222, 0.414222, 0.406552, 0.398882, 0.487854, 0.817664, 1.09992, 1.09378, 1.07231, 0.987938,
			 0.843742, 0.756304, 0.7471, 0.740964, 0.73943, 0.73943])

		names.append("RElbowYaw")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[1.18267, 1.18267, 1.18267, 1.18267, 1.18267, 1.14125, 0.450954, 0.153358, 0.15796, 0.191708, 0.171766,
			 0.0889301, -0.0061779, -0.0061779, -0.0061779, -0.0061779, -0.0061779])

		names.append("RHand")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948,
			 0.2948, 0.2948, 0.2948, 0.2948])

		names.append("RShoulderPitch")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[1.46655, 1.46655, 1.46655, 1.46808, 1.47575, 1.3515, 0.779314, 0.628982, 0.895898, 0.782382, 0.817664,
			 1.38218, 1.3699, 1.36837, 1.36837, 1.3699, 1.36837])

		names.append("RShoulderRoll")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([-0.0399261, -0.0399261, -0.0399261, -0.0399261, -0.016916, 0.055182, 0.139552, 0.314159, 0.294486,
					 -0.190258, -0.541544, -0.452572, -0.360532, -0.357464, -0.354396, -0.354396, -0.354396])

		names.append("RWristYaw")
		times.append(
			[0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append(
			[0.0843279, 0.0843279, 0.0843279, 0.0843279, 0.0843279, 0.098134, 0.099668, 0.101202, 0.182504, 0.193242,
			 0.194776, 0.170232, 0.162562, 0.162562, 0.162562, 0.162562, 0.162562])


		return [names, keys, times]

	@staticmethod
	def BabyMotion():
		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.8, 1.84])
		keys.append([-0.835988, -0.742414])

		names.append("LElbowYaw")
		times.append([0.8, 1.84])
		keys.append([-1.18276, -1.17202])

		names.append("LHand")
		times.append([0.8, 1.84])
		keys.append([0.9708, 0.9708])

		names.append("LShoulderPitch")
		times.append([0.8, 1.84])
		keys.append([0.812978, 1.62753])

		names.append("LShoulderRoll")
		times.append([0.8, 1.84])
		keys.append([0.0981341, 0.116542])

		names.append("LWristYaw")
		times.append([0.8, 1.84])
		keys.append([0.713267, 0.915757])

		return [names, keys, times]

	@staticmethod
	def BegMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[-0.116626, -0.116626, -0.116626, -0.0752079, 0.139552, 0.383458, 0.511779, 0.511779, 0.511779, 0.458624,
			 -0.067538, -0.0844119, -0.121228, -0.119694])

		names.append("HeadYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[-0.021518, -0.021518, -0.023052, -0.021518, -0.00771189, 0.00609398, 0.0168321, 0.0168321, 0.0168321,
			 0.0122299, 0.00302601, -4.19617e-05, -4.19617e-05, -4.19617e-05])

		names.append("LElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[-0.0367742, -0.0367742, -0.0689881, -0.274544, -1.10904, -1.20568, -1.24403, -1.25017, -1.2425, -1.18114,
			 -0.82525, -0.220854, -0.222388, -0.220854])

		names.append("LElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[-1.1398, -1.1398, -1.14287, -1.14441, -1.14441, -1.03856, -1.04316, -1.04316, -1.07077, -1.06157, -0.99254,
			 -0.99254, -0.99254, -0.99254])

		names.append("LHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[0.9984, 0.9984, 0.9984, 0.9984, 0.9984, 0.998, 0.9984, 0.9984, 0.9984, 0.9984, 0.9984, 0.998, 0.9984,
			 0.9984])

		names.append("LShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[1.41124, 1.41277, 1.4051, 0.812978, 0.282214, 0.392662, 0.435614, 0.435614, 0.44942, 0.58748, 1.58611,
			 1.57077, 1.57077, 1.57077])

		names.append("LShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[0.124212, 0.124212, 0.0966001, -0.199462, -0.181054, -0.314159, -0.314159, -0.314159, -0.274628, 0.029104,
			 0.317496, 0.194776, 0.194776, 0.194776])

		names.append("LWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[-0.236278, -0.236278, -0.513932, -0.760906, -1.3607, -1.21804, -1.11066, -1.09225, -1.20423, -1.18736,
			 -0.658128, -0.641254, -0.641254, -0.641254])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[0.073674, 0.07214, 0.0890141, 0.285366, 1.3607, 1.31621, 1.31315, 1.31008, 1.26406, 1.07538, 0.914306,
			 0.797722, 0.797722, 0.796188])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[1.24557, 1.24557, 1.2379, 1.25937, 1.42044, 1.34681, 1.3146, 1.3146, 1.26091, 1.04921, 0.951038, 0.952572,
			 0.952572, 0.951038])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[0.9996, 0.9996, 0.9996, 0.9996, 0.9996, 0.9996, 0.9996, 0.9996, 0.9996, 0.9996, 0.9996, 0.9996, 0.9996,
			 0.9996])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[1.51257, 1.51257, 1.51257, 0.963394, 0.411154, 0.388144, 0.398882, 0.397348, 0.39428, 0.48632, 1.59847,
			 1.66443, 1.66597, 1.66597])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[-0.130432, -0.130432, -0.11816, 0.076658, 0.308292, 0.314159, 0.314159, 0.314159, 0.314159, 0.0628521,
			 -0.414222, -0.29457, -0.29457, -0.293036])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04])
		keys.append(
			[-0.093616, -0.092082, -0.124296, -0.158044, -0.161112, -0.0782759, -0.0844119, -0.0844119, -0.121228,
			 -0.122762, -0.326784, -0.328318, -0.328318, -0.328318])

		return [names, keys, times]

	@staticmethod
	def BigAgMotion():
		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([-0.34971, -0.351244, -0.381924, -0.360448, -0.27301, -0.153358, -0.282214, -0.182504, -0.136484,
					 -0.0689881, -0.0705221])

		names.append("LElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([-1.32235, -1.32235, -1.32849, -1.32849, -1.31621, -1.31468, -1.31621, -1.24258, -1.24718, -1.24872,
					 -1.24718])

		names.append("LHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([0.304, 0.304, 0.304, 0.304, 0.304, 0.304, 0.304, 0.304, 0.304, 0.304, 0.304])

		names.append("LShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append(
			[1.4726, 1.4726, 1.07683, 0.443284, 0.190174, 0.190174, 0.187106, 0.240796, 1.17807, 1.35448, 1.35448])

		names.append("LShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append(
			[0.05058, 0.032172, 0.139552, 0.589014, 1.06302, 1.18267, 0.972514, 0.467828, -0.0322559, -0.0368581,
			 -0.0368581])

		names.append("LWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append(
			[0.12728, 0.12728, 0.124212, 0.121144, 0.13495, 0.148756, 0.099668, 0.00609398, 0.026036, -0.0874801,
			 -0.0874801])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append(
			[0.211734, 0.213268, 0.314512, 0.293036, 0.326784, 0.319114, 0.40195, 0.37894, 0.30991, 0.259288, 0.260822])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([1.85917, 1.85917, 1.90058, 2.02484, 2.08567, 2.08567, 2.08567, 2.08567, 2.08567, 2.08567, 2.08567])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append(
			[1.53558, 1.53558, 1.27786, 0.673468, 0.63205, 0.622846, 0.619778, 0.719488, 1.30548, 1.50643, 1.50643])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append(
			[0.00609398, 0.00762796, -0.211734, -0.9005, -1.29781, -1.30241, -1.24412, -0.497058, -0.019984, 0.079726,
			 0.079726])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append(
			[0.098134, 0.0966001, 0.102736, 0.113474, 0.113474, 0.113474, 0.113474, 0.115008, 0.113474, 0.108872,
			 0.108872])

		return [names, keys, times]

	@staticmethod
	def CarefulMotion():
		names = list()
		times = list()
		keys = list()
		
		names.append("HeadPitch")
		times.append([1.28, 2.16])
		keys.append([-0.0245859, -0.0245859])

		names.append("HeadYaw")
		times.append([1.28, 2.16])
		keys.append([0.00609404, 0.00609404])

		# names.append("LAnklePitch")
		# times.append([1.28, 2.16])
		# keys.append([-0.411285, -0.104485])

		# names.append("LAnkleRoll")
		# times.append([1.28, 2.16])
		# keys.append([-0.0812816, 0.0092244])

		names.append("LElbowRoll")
		times.append([1, 1.36, 2.16])
		keys.append([-0.368118, -0.368118, -0.326699])

		names.append("LElbowYaw")
		times.append([1, 1.36, 2.16])
		keys.append([0.727074, 0.727074, -0.759372])

		names.append("LHand")
		times.append([1, 1.36, 2.16])
		keys.append([0.392752, 0.0378446, 0.918933])

		# names.append("LHipPitch")
		# times.append([1.28, 2.16])
		# keys.append([-0.191972, 0.0596046])

		# names.append("LHipRoll")
		# times.append([1.28, 2.16])
		# keys.append([0.15014, -0.0324061])

		# names.append("LHipYawPitch")
		# times.append([1.28, 2.16])
		# keys.append([-0.372806, 0.0183645])

		# names.append("LKneePitch")
		# times.append([1.28, 2.16])
		# keys.append([0.966101, 0.0702441])

		names.append("LShoulderPitch")
		times.append([1, 1.36, 2.16])
		keys.append([-0.165714, -0.165714, 1.52613])

		names.append("LShoulderRoll")
		times.append([1, 1.36, 2.16])
		keys.append([0.00762803, 0.00762803, 0.329768])

		names.append("LWristYaw")
		times.append([1, 1.36, 2.16])
		keys.append([-0.740964, -0.760906, -1.02629])

		# names.append("RAnklePitch")
		# times.append([1.28, 2.16])
		# keys.append([-0.38813, -0.0951351])

		# names.append("RAnkleRoll")
		# times.append([1.28, 2.16])
		# keys.append([0.0475937, -0.00302827])

		names.append("RElbowRoll")
		times.append([1, 2.16])
		keys.append([0.368202, 0.291501])

		names.append("RElbowYaw")
		times.append([1, 2.16])
		keys.append([0.469363, 0.77923])

		names.append("RHand")
		times.append([1, 2.16])
		keys.append([0.46, 0.918205])

		# names.append("RHipPitch")
		# times.append([1.28, 2.16])
		# keys.append([-0.148855, 0.0367591])

		# names.append("RHipRoll")
		# times.append([1.28, 2.16])
		# keys.append([-0.0383295, 0.0107584])

		# names.append("RKneePitch")
		# times.append([1.28, 2.16])
		# keys.append([0.892375, 0.0839559])

		names.append("RShoulderPitch")
		times.append([1, 2.16])
		keys.append([1.26713, 1.59274])

		names.append("RShoulderRoll")
		times.append([1, 2.16])
		keys.append([-0.346725, -0.320648])

		names.append("RWristYaw")
		times.append([1, 2.16])
		keys.append([0.819114, 0.967912])


		return [names, keys, times]

	@staticmethod
	def ClapMotion():
		
		names = list()
		times = list()
		keys = list()
		names.append("HeadPitch")
		times.append([1, 3.44])
		keys.append([-0.00771196, -0.00771196])

		names.append("HeadYaw")
		times.append([1, 3.44])
		keys.append([-0.00157596, -0.00157596])

		# names.append("LAnklePitch")
		# times.append([1, 3.44])
		# keys.append([-0.0922134, -0.0922134])

		# names.append("LAnkleRoll")
		# times.append([1, 3.44])
		# keys.append([0.0046224, 0.0046224])

		names.append("LElbowRoll")
		times.append([1, 1.16, 1.36, 1.52, 1.68, 1.84, 2, 2.16, 2.32, 2.48, 2.64, 2.8, 2.96, 3.44])
		keys.append([-0.312894, -1.20253, -1.20253, -1.20253, -1.20253, -1.20253, -1.20253, -1.20253, -1.20253, -1.20253, -1.20253, -1.20253, -1.20253, -0.312894])

		names.append("LElbowYaw")
		times.append([1, 1.16, 1.28, 1.36, 1.44, 1.52, 1.6, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64, 2.72, 2.8, 2.88, 2.96, 3.04, 3.44])
		keys.append([-0.770111, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.770111])

		names.append("LHand")
		times.append([1, 1.16, 1.36, 1.52, 1.68, 1.84, 2, 2.16, 2.32, 2.48, 2.64, 2.8, 2.96, 3.44])
		keys.append([0.916751, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.916751])

		# names.append("LHipPitch")
		# times.append([1, 3.44])
		# keys.append([0.0442645, 0.0442645])

		# names.append("LHipRoll")
		# times.append([1, 3.44])
		# keys.append([-0.0155321, -0.0155321])

		# names.append("LHipYawPitch")
		# times.append([1, 3.44])
		# keys.append([0.00916048, 0.00916048])

		# names.append("LKneePitch")
		# times.append([1, 3.44])
		# keys.append([0.0564382, 0.0564382])

		names.append("LShoulderPitch")
		times.append([1, 1.16, 1.36, 1.52, 1.68, 1.84, 2, 2.16, 2.32, 2.48, 2.64, 2.8, 2.96, 3.44])
		keys.append([1.57231, 0.994838, 0.994838, 0.994838, 0.994838, 0.994838, 0.994838, 0.994838, 0.994838, 0.994838, 0.994838, 0.994838, 0.994838, 1.57231])

		names.append("LShoulderRoll")
		times.append([1, 1.16, 1.36, 1.52, 1.68, 1.84, 2, 2.16, 2.32, 2.48, 2.64, 2.8, 2.96, 3.44])
		keys.append([0.31903, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.31903])

		names.append("LWristYaw")
		times.append([1, 1.16, 1.36, 1.52, 1.68, 1.84, 2, 2.16, 2.32, 2.48, 2.64, 2.8, 2.96, 3.44])
		keys.append([-1.00941, 0.254818, 0.254818, 0.254818, 0.254818, 0.254818, 0.254818, 0.254818, 0.254818, 0.254818, 0.254818, 0.254818, 0.254818, -1.00941])

		# names.append("RAnklePitch")
		# times.append([1, 3.44])
		# keys.append([-0.0889992, -0.0889992])

		# names.append("RAnkleRoll")
		# times.append([1, 3.44])
		# keys.append([-0.00149427, -0.00149427])

		names.append("RElbowRoll")
		times.append([1, 1.16, 1.28, 1.36, 1.44, 1.52, 1.6, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64, 2.72, 2.8, 2.88, 2.96, 3.04, 3.44])
		keys.append([0.308375, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 0.308375])

		names.append("RElbowYaw")
		times.append([1, 1.16, 1.28, 1.36, 1.44, 1.52, 1.6, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64, 2.72, 2.8, 2.88, 2.96, 3.04, 3.44])
		keys.append([0.770025, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.770025])

		names.append("RHand")
		times.append([1, 1.16, 1.36, 1.52, 1.68, 1.84, 2, 2.16, 2.32, 2.48, 2.64, 2.8, 2.96, 3.44])
		keys.append([0.917114, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.945455, 0.917114])

		# names.append("RHipPitch")
		# times.append([1, 3.44])
		# keys.append([0.032157, 0.032157])

		# names.append("RHipRoll")
		# times.append([1, 3.44])
		# keys.append([0.0046224, 0.0046224])

		# names.append("RKneePitch")
		# times.append([1, 3.44])
		# keys.append([0.0624798, 0.0624798])

		names.append("RShoulderPitch")
		times.append([1, 1.16, 1.36, 1.52, 1.68, 1.84, 2, 2.16, 2.32, 2.48, 2.64, 2.8, 2.96, 3.44])
		keys.append([1.57239, 1.09956, 1.09956, 1.09956, 1.09956, 1.09956, 1.09956, 1.09956, 1.09956, 1.09956, 1.09956, 1.09956, 1.09956, 1.57239])

		names.append("RShoulderRoll")
		times.append([1, 1.16, 1.36, 1.52, 1.68, 1.84, 2, 2.16, 2.32, 2.48, 2.64, 2.8, 2.96, 3.44])
		keys.append([-0.309909, -0.0942478, -0.0942478, -0.0942478, -0.0942478, -0.0942478, -0.0942478, -0.0942478, -0.0942478, -0.0942478, -0.0942478, -0.0942478, -0.0942478, -0.309909])

		names.append("RWristYaw")
		times.append([1, 1.16, 1.36, 1.52, 1.68, 1.84, 2, 2.16, 2.32, 2.48, 2.64, 2.8, 2.96, 3.44])
		keys.append([0.989389, 1.22173, 1.22173, 1.22173, 1.22173, 1.22173, 1.22173, 1.22173, 1.22173, 1.22173, 1.22173, 1.22173, 1.22173, 0.989389])



		return [names, keys, times]

	@staticmethod
	def ComeMotion():
		names = list()
		times = list()
		keys = list()
		
		
		names.append("LElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([-0.39573, -0.39573, -0.39573, -0.501576, -0.805308, -1.34988, -0.889678, -0.581344, -1.06149, -1.52936, -0.668782, -0.292952, -0.164096, -0.16563, -0.16563])

		names.append("LElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([-1.25332, -1.25332, -1.25332, -1.25025, -1.24872, -1.24872, -1.25025, -1.25179, -1.25639, -1.26713, -1.26713, -1.26559, -1.26559, -1.26713, -1.26713])

		names.append("LHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948, 0.2948])

		names.append("LShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([1.49561, 1.49714, 1.49561, 1.42351, 1.15659, 1.18881, 1.22869, 1.29772, 1.09984, 1.14586, 1.29772, 1.36062, 1.4864, 1.4864, 1.4864])

		names.append("LShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.15029, 0.15029, 0.15029, -0.046062, -0.247016, -0.242414, -0.230142, -0.231676, -0.314159, -0.308376, -0.254686, -0.0798099, 0.055182, 0.052114, 0.052114])

		names.append("LWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([-1.79329, -1.79329, -1.79329, -1.79636, -1.79636, -1.79942, -1.80096, -1.79482, -1.79636, -1.79329, -1.76414, -1.72733, -1.72886, -1.72886, -1.72886])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.400416, 0.400416, 0.400416, 0.500126, 1.04163, 1.4328, 0.81613, 0.507796, 1.09532, 1.51563, 1.28247, 0.067538, 0.0506639, 0.0521979, 0.0521979])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([1.45726, 1.45726, 1.45726, 1.46493, 1.46493, 1.47567, 1.47567, 1.4726, 1.48334, 1.48947, 1.48334, 1.48487, 1.48487, 1.4864, 1.4864])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([1.47882, 1.47882, 1.47882, 1.40212, 1.14594, 1.14441, 1.26099, 1.24718, 1.05083, 1.05697, 1.30548, 1.41286, 1.41439, 1.41439, 1.41439])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.00149202, 0.00149202, 0.00149202, 0.0613179, 0.0398421, 0.0674541, 0.0919981, 0.10427, 0.0919981, 0.116542, 0.08126, -0.0521979, -0.04146, -0.016916, -0.016916])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([1.62753, 1.62753, 1.62753, 1.62907, 1.6306, 1.63367, 1.65054, 1.64901, 1.65208, 1.65054, 1.64901, 1.48947, 1.48947, 1.49101, 1.49101])



		return [names, keys, times]

	@staticmethod
	def ContinueMotion():
		names = list()
		times = list()
		keys = list()
		names.append("HeadPitch")
		
		times.append([2.84])
		keys.append([-0.0245859])

		names.append("HeadYaw")
		times.append([2.84])
		keys.append([0.00609404])

		# names.append("LAnklePitch")
		# times.append([2.84])
		# keys.append([-0.104485])

		# names.append("LAnkleRoll")
		# times.append([2.84])
		# keys.append([0.0092244])

		names.append("LElbowRoll")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([-1.29312, -1.04308, -0.6335, -0.891212, -1.29312, -1.04308, -0.6335, -0.891212, -0.326699])

		names.append("LElbowYaw")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([-0.311444, -1.01095, -0.671934, -0.0690719, -0.311444, -1.01095, -0.671934, -0.0690719, -0.759372])

		names.append("LHand")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([0.922569, 0.754545, 0.754545, 0.754545, 0.922569, 0.754545, 0.754545, 0.754545, 0.918933])

		# names.append("LHipPitch")
		# times.append([2.84])
		# keys.append([0.0596046])

		# names.append("LHipRoll")
		# times.append([2.84])
		# keys.append([-0.0324061])

		# names.append("LHipYawPitch")
		# times.append([2.84])
		# keys.append([0.0183645])

		# names.append("LKneePitch")
		# times.append([2.84])
		# keys.append([0.0702441])

		names.append("LShoulderPitch")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([0.552198, 0.575208, 0.452489, 0.53379, 0.552198, 0.575208, 0.452489, 0.53379, 1.56771])

		names.append("LShoulderRoll")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([0.101202, 0.12728, 0.091998, 0.041376, 0.101202, 0.12728, 0.091998, 0.041376, 0.329768])

		names.append("LWristYaw")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([-1.00021, -1.00021, -1.00021, -1.00021, -1.00021, -1.00021, -1.00021, -1.00021, -1.02629])

		# names.append("RAnklePitch")
		# times.append([2.84])
		# keys.append([-0.0951351])

		# names.append("RAnkleRoll")
		# times.append([2.84])
		# keys.append([-0.00302827])

		names.append("RElbowRoll")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([0.627448, 0.604437, 0.604437, 0.605971, 0.627448, 0.604437, 0.604437, 0.605971, 0.291501])

		names.append("RElbowYaw")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([0.731675, 0.719404, 0.720938, 0.724006, 0.731675, 0.719404, 0.720938, 0.724006, 0.77923])

		names.append("RHand")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([0.920387, 0.920387, 0.920387, 0.920387, 0.920387, 0.920387, 0.920387, 0.920387, 0.918205])

		# names.append("RHipPitch")
		# times.append([2.84])
		# keys.append([0.0367591])

		# names.append("RHipRoll")
		# times.append([2.84])
		# keys.append([0.0107584])

		# names.append("RKneePitch")
		# times.append([2.84])
		# keys.append([0.0839559])

		names.append("RShoulderPitch")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([1.36377, 1.37144, 1.37911, 1.39291, 1.36377, 1.37144, 1.37911, 1.39291, 1.56779])

		names.append("RShoulderRoll")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([-0.248551, -0.248551, -0.248551, -0.268493, -0.248551, -0.248551, -0.248551, -0.268493, -0.320648])

		names.append("RWristYaw")
		times.append([0.76, 1.04, 1.28, 1.56, 1.8, 2.04, 2.28, 2.48, 2.84])
		keys.append([0.951039, 0.951039, 0.951039, 0.951039, 0.951039, 0.951039, 0.951039, 0.951039, 0.967912])


		return [names, keys, times]

	@staticmethod
	def CookMotion():
		names = list()
		times = list()
		keys = list()
		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04])
		keys.append([0.377406, 0.377406, 0.37127, 0.372804, 0.388144, 0.405018, 0.444902, 0.592166, 0.699546, 0.644322, 0.645856, 0.658128, 0.618244, 0.604438, 0.698012, 0.650458, 0.513932, 0.312978, 0.191792, 0.191792])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04])
		keys.append([1.37749, 1.37596, 1.37596, 1.37289, 1.33454, 1.26397, 1.30846, 1.30693, 1.14125, 0.969446, 1.01853, 1.05535, 0.97098, 1.09217, 1.22102, 1.175, 1.13972, 1.13972, 1.13972, 1.13972])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04])
		keys.append([0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04])
		keys.append([1.49723, 1.49723, 1.50336, 1.41746, 1.15054, 0.93118, 0.461776, 0.412688, 0.388144, 0.83914, 0.826868, 0.466378, 0.711818, 0.851412, 0.605972, 0.613642, 1.03396, 1.30241, 1.48956, 1.48956])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04])
		keys.append([0.00455999, 0.00455999, 0.00149202, -0.0874801, -0.12583, -0.10282, -0.280764, -0.254686, 0.22699, 0.253068, -0.37127, -0.021518, 0.314159, -0.139636, -0.0874801, 0.314159, 0.0137641, -0.14117, -0.131966, -0.066004])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04])
		keys.append([0.141086, 0.141086, 0.141086, 0.14262, 0.14262, 0.14262, 0.714802, 0.885076, 0.8636, 0.305224, 0.302156, 0.753152, 0.535324, 0.519984, 0.84059, 0.713268, 0.461692, 0.45709, 0.45709, 0.45709])

		return [names, keys, times]

	@staticmethod
	def CarddleMotion():
		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([-0.220854, -0.220854, -0.21932, -0.325166, -0.97098, -0.97865, -1.05535, -1.03081, -1.10137, -1.05382, -1.54009, -1.05535, -1.09523, -0.905018, -0.124212, -0.124212])

		names.append("LElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([-1.07998, -1.07844, -1.07998, -1.08151, -1.04776, -1.09072, -1.34076, -1.27019, -0.871354, -1.05697, -1.99884, -1.40672, -0.833004, -0.840674, -0.842208, -0.842208])

		names.append("LHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436, 0.5436])

		names.append("LShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([1.28085, 1.28085, 1.30846, 1.27625, 1.1658, 1.16273, 0.903484, 0.961776, 1.13358, 1.15506, 0.981718, 1.13052, 1.02007, 1.54009, 1.56771, 1.56924])

		names.append("LShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append( [-0.067538, -0.067538, -0.07214, -0.311444, -0.314159, -0.214802, 0.02757, -0.073674, -0.314159, -0.200996, -0.0107799, -0.26389, -0.314159, 0.305224, 0.223922, 0.153358])

		names.append("LWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([-0.3636, -0.3636, -0.360532, -0.420358, -0.47098, -0.45564, -0.408086, -0.358998, -0.319114, -0.343658, -0.191792, -0.188724, -0.316046, -0.352862, -0.34059, -0.342124])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([0.44797, 0.44797, 0.44797, 0.538476, 0.848344, 0.912772, 0.934248, 0.937316, 1.52177, 1.36684, 1.01095, 1.22878, 1.54171, 1.3607, 1.21804, 1.21344])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([1.51555, 1.51555, 1.51555, 1.53703, 1.60912, 1.58458, 0.765424, 0.920358, 2.08567, 1.7165, 0.553732, 1.61679, 2.01717, 2.04631, 2.04785, 2.04785])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([0.3464, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468, 0.3468])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([1.53711, 1.53711, 1.53711, 1.44047, 1.13674, 1.12293, 1.126, 1.12753, 1.10299, 1.24258, 1.22724, 1.21957,1.09839, 1.82857, 2.06787, 2.06787])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([0.026036, 0.026036, 0.02757, 0.0229681, -0.070606, 0.314159, 0.314159, 0.256136, 0.176368, 0.314159,0.314159, 0.314159, 0.164096, 0.20398, 0.251534, 0.25])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([0.308292, 0.308292, 0.308292, 0.343574, 0.446352, 0.355846, 0.44175, 0.446352, 0.452488, 0.417206, 0.466294, 0.466294, 0.47243, 0.424876, 0.42641, 0.42641])

		return [names, keys, times]

	@staticmethod
	def CryMotionCorrected():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92])
		keys.append([0.498847, 0.39653, 0.450723, 0.437496, 0.449255, 0.489453, 0.220854, -0.11816, -0.11816, -0.11816])

		names.append("HeadYaw")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92])
		keys.append([-0.0844118, -0.5937, 0.335904, -0.405018, 0.343573, -0.1335, -0.0552659, -0.0276539, -0.0291878,
					 -0.0276539])

		names.append("LElbowRoll")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append([-1.54462, -1.54462, -1.54462, -1.54462, -1.54462, -1.54462, -1.54462, -1.53856, -1.35755, -1.23329,
					 -1.18267])

		names.append("LElbowYaw")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append([-1.09685, -1.10912, -1.10759, -1.10759, -1.10452, -1.10452, -1.10452, -1.09685, -1.09225, -1.09225,
					 -1.09225])

		names.append("LHand")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append([0.7508, 0.7508, 0.7508, 0.7508, 0.7508, 0.7508, 0.7508, 0.7508, 0.7508, 0.7508, 0.7508])

		names.append("LShoulderPitch")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append(
			[0.869736, 0.569072, 0.473963, 0.473963, 0.509247, 0.509247, 0.509247, 0.59515, 1.10137, 1.60759, 1.61219])

		names.append("LShoulderRoll")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append([-0.0982179, -0.228608, -0.237812, -0.237812, -0.222472, -0.222472, -0.222472, -0.219404, -0.190258,
					 0.052114, 0.052114])

		names.append("LWristYaw")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append(
			[-1.01402, -1.01402, -0.995607, -0.981802, -0.978734, -0.975665, -0.971065, -0.937315, -0.811527, -0.566089,
			 -0.567621])

		names.append("RElbowRoll")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append([1.4466, 1.53711, 1.54171, 1.54171, 1.54018, 1.53864, 1.53864, 1.50643, 1.33309, 1.15208, 1.0493])

		names.append("RElbowYaw")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append(
			[1.10597, 1.10904, 1.11364, 1.10444, 1.07989, 1.07529, 1.07529, 1.03694, 0.958708, 0.937231, 0.938765])

		names.append("RHand")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append([0.6772, 0.6772, 0.6772, 0.6772, 0.6772, 0.6772, 0.6772, 0.6772, 0.6772, 0.6772, 0.6772])

		names.append("RShoulderPitch")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append([0.911238, 0.615176, 0.428028, 0.428028, 0.441834, 0.443368, 0.443368, 0.510865, 0.851412, 1.46348,
					 1.49109])

		names.append("RShoulderRoll")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append(
			[0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.174835, -0.073674,
			 -0.07214])

		names.append("RWristYaw")
		times.append([3.4, 3.92, 4.4, 4.92, 5.4, 5.92, 6.4, 6.92, 7.4, 7.92, 8.4])
		keys.append([0.960242, 0.961776, 0.961776, 0.961776, 0.944902, 0.944902, 0.944902, 0.915757, 0.831386, 0.449421,
					 0.449421])


		return [names, keys, times]

	@staticmethod
	def DanceAgMotion():

		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1, 1.96, 3.32])
		keys.append([-0.136568, -0.268493, 0.118076])

		names.append("HeadYaw")
		times.append([1, 1.96, 3.32])
		keys.append([-0.021518, 0.384992, -0.214803])

		# names.append("LAnklePitch")
		# times.append([1, 1.96, 3.32])
		# keys.append([0.095066, 0.174835, 0.179436])

		# names.append("LAnkleRoll")
		# times.append([1, 1.96, 3.32])
		# keys.append([-0.116542, -0.0720561, -0.141086])

		names.append("LElbowRoll")
		times.append([1, 1.96, 2.6, 3.32, 3.96])
		keys.append([-0.38806, -0.199378, -1.22562, -0.391128, -1.22562])

		names.append("LElbowYaw")
		times.append([1, 1.96, 2.6, 3.32, 3.96])
		keys.append([-1.20883, -1.56165, -0.803859, -0.337522, -0.803859])

		names.append("LHand")
		times.append([1, 1.96, 2.6, 3.32, 3.96])
		keys.append([0.3056, 0.8592, 0.8592, 0.8592, 0.8592])

		# names.append("LHipPitch")
		# times.append([1, 1.96, 3.32])
		# keys.append([0.136568, -0.243864, 0.0552659])

		# names.append("LHipRoll")
		# times.append([1, 1.96, 3.32])
		# keys.append([0.116626, 0.066004, 0.142704])

		# names.append("LHipYawPitch")
		# times.append([1, 1.96, 3.32])
		# keys.append([-0.1733, -0.371186, -0.538392])

		# names.append("LKneePitch")
		# times.append([1, 1.96, 3.32])
		# keys.append([-0.090548, 0.223922, -0.00310993])

		names.append("LShoulderPitch")
		times.append([1, 1.96, 2.6, 3.32, 3.96])
		keys.append([1.53089, -1.08611, 0.759288, 0.960242, 0.759288])

		names.append("LShoulderRoll")
		times.append([1, 1.96, 2.6, 3.32, 3.96])
		keys.append([0.130348, 0.636569, 0.228525, -0.314159, 0.228525])

		names.append("LWristYaw")
		times.append([1, 1.96, 2.6, 3.32, 3.96])
		keys.append([0.0843279, 0.900415, 1.23176, 0.730143, 1.23176])

		# names.append("RAnklePitch")
		# times.append([1, 1.96, 3.32])
		# keys.append([0.101286, 0.11049, 0.108956])

		# names.append("RAnkleRoll")
		# times.append([1, 1.96, 3.32])
		# keys.append([0.075208, 0.277696, -0.0168321])

		names.append("RElbowRoll")
		times.append([1, 1.96, 3.32])
		keys.append([0.389678, 0.392746, 0.194861])

		names.append("RElbowYaw")
		times.append([1, 1.96, 3.32])
		keys.append([1.1796, 1.18114, 1.16887])

		names.append("RHand")
		times.append([1, 1.96, 3.32])
		keys.append([0.3068, 0.3068, 0.684])

		# names.append("RHipPitch")
		# times.append([1, 1.96, 3.32])
		# keys.append([0.130348, 0.131882, -0.073674])

		# names.append("RHipRoll")
		# times.append([1, 1.96, 3.32])
		# keys.append([-0.06592, -0.292952, 0.00771189])

		# names.append("RHipYawPitch")
		# times.append([1, 1.96, 3.32])
		# keys.append([-0.1733, -0.371186, -0.538392])

		# names.append("RKneePitch")
		# times.append([1, 1.96, 3.32])
		# keys.append([-0.0923279, -0.0923279, 0.196393])

		names.append("RShoulderPitch")
		times.append([1, 1.96, 3.32])
		keys.append([1.52637, 1.51563, 1.49262])

		names.append("RShoulderRoll")
		times.append([1, 1.96, 3.32])
		keys.append([-0.10282, -0.10282, -0.158044])

		names.append("RWristYaw")
		times.append([1, 1.96, 3.32])
		keys.append([0.059784, 0.06592, -0.530805])

		return [names, keys, times]

	@staticmethod
	def EverywhereMotion():
		
		names = list()
		times = list()
		keys = list()
		 
		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52])
		keys.append([0.391212, 0.391212, 0.391212, 0.334454, 0.253152, 0.191792, 0.19486, 0.188724, 0.296104, 0.530806, 0.83914, 1.05237, 0.934248, 0.802324, 0.625914, 0.50166, 0.44797, 0.388144, 0.388144])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52])
		keys.append([-0.0261199, -0.0261199, -0.0261199, -0.0107799, 0.0183661, 0.0214341, 0.024502, 0.024502, 0.024502, 0.024502, 0.024502, 0.0137641, -0.0337899, -0.0337899, -0.0322559, -0.0322559, -0.0368581, -0.0368581, -0.0368581])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52])
		keys.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52])
		keys.append([1.37297, 1.37297, 1.37297, 1.28553, 0.880558, 0.47865, 0.259288, 0.196394, 0.197928, 0.197928, 0.197928, 0.2102, 0.380474, 0.380474, 0.375872, 0.37894, 1.11679, 1.38678, 1.38678])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52])
		keys.append([-0.257754, -0.257754, -0.257754, -0.276162, -0.446436, -0.58603, -0.346726, 0.24233, 0.314159, 0.314159, 0.314159, 0.314159, 0.214718, -0.265424, -0.636652, -0.91584, -0.596768, -0.24855, -0.24855])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52])
		keys.append([0.371186, 0.371186, 0.371186, 0.371186, 0.371186, 0.371186, 0.371186, 0.371186, 0.400332, 0.466294, 0.492372, 0.501576, 0.498508, 0.398798, 0.38039, 0.19631, 0.0689881, 0.20398, 0.20398])
		
		return [names, keys, times]

	@staticmethod
	def ExultMotion():
		names = list()
		times = list()
		keys = list()
		names.append("HeadPitch")
		times.append([1.46667, 2.73333, 3.8, 5.33333])
		keys.append([-0.315905, -0.315905, -0.315905, -0.0245859])

		names.append("HeadYaw")
		times.append([1.46667, 2.73333, 3.8, 5.33333])
		keys.append([0.010696, 0.010696, 0.010696, 0.00609404])

		# names.append("LAnklePitch")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([-0.348392, -0.179769, -0.348392, -0.179769, -0.348392, -0.179769, -0.104485])

		# names.append("LAnkleRoll")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([-0.0521356, -0.164061, -0.0521356, -0.164061, -0.0521356, -0.164061, 0.0092244])

		names.append("LElbowRoll")
		times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		keys.append([-1.55237, -0.31903, -1.55237, -0.31903, -1.55237, -0.31903, -0.326699])

		names.append("LElbowYaw")
		times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		keys.append([-1.2794, -0.346725, -1.2794, -0.346725, -1.2794, -0.346725, -0.759372])

		names.append("LHand")
		times.append([1.46667, 2.73333, 3.8, 5.33333])
		keys.append([0.0949353, 0.0949353, 0.0949353, 0.918933])

		# names.append("LHipPitch")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([-1.14459, -0.137881, -1.14459, -0.137881, -1.14459, -0.137881, 0.0596046])

		# names.append("LHipRoll")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([-0.00172607, 0.120428, -0.00172607, 0.120428, -0.00172607, 0.120428, -0.0324061])

		# names.append("LHipYawPitch")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([-0.256221, -0.172788, -0.256221, -0.172788, -0.256221, -0.172788, 0.0183645])

		# names.append("LKneePitch")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([1.31432, 0.338594, 1.31432, 0.338594, 1.31432, 0.338594, 0.0702441])

		names.append("LShoulderPitch")
		times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		keys.append([-0.412688, -0.900499, -0.412688, -0.900499, -0.412688, -0.900499, 1.56771])

		names.append("LShoulderRoll")
		times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		keys.append([0.983252, 0.418879, 0.983252, 0.424115, 0.983252, 0.424115, 0.329768])

		names.append("LWristYaw")
		times.append([1.46667, 2.73333, 3.8, 5.33333])
		keys.append([-1.78715, -1.78715, -1.78715, -1.02629])

		# names.append("RAnklePitch")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([-0.202516, -0.179769, -0.202516, -0.179769, -0.202516, -0.179769, -0.0951351])

		# names.append("RAnkleRoll")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([0.0690697, 0.164061, 0.0690697, 0.164061, 0.0690697, 0.164061, -0.00302827])

		names.append("RElbowRoll")
		times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		keys.append([1.55245, 0.286901, 1.55245, 0.286901, 1.55245, 0.286901, 0.291501])

		names.append("RElbowYaw")
		times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		keys.append([0.880473, 0.983252, 0.880473, 0.983252, 0.880473, 0.983252, 0.77923])

		names.append("RHand")
		times.append([1.46667, 2.73333, 3.8, 5.33333])
		keys.append([0.0396627, 0.0396627, 0.0396627, 0.918205])

		# names.append("RHipPitch")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([-1.18124, -0.137881, -1.18124, -0.137881, -1.18124, -0.137881, 0.0367591])

		# names.append("RHipRoll")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([0.0199624, -0.120428, 0.0199624, -0.120428, 0.0199624, -0.120428, 0.0107584])

		# names.append("RKneePitch")
		# times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		# keys.append([1.19611, 0.338594, 1.19611, 0.338594, 1.19611, 0.338594, 0.0839559])

		names.append("RShoulderPitch")
		times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		keys.append([-0.737812, -0.87127, -0.737812, -0.87127, -0.737812, -0.87127, 1.56779])

		names.append("RShoulderRoll")
		times.append([1.46667, 2.13333, 2.73333, 3.26667, 3.8, 4.33333, 5.33333])
		keys.append([-0.915841, -0.418879, -0.915841, -0.424115, -0.915841, -0.424115, -0.320648])

		names.append("RWristYaw")
		times.append([1.46667, 2.73333, 3.8, 5.33333])
		keys.append([0.923426, 0.923426, 0.923426, 0.967912])


		return [names, keys, times]

	@staticmethod
	def HereMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52])
		keys.append([0.082794, 0.501195, 0.501195, 0.450954, -0.185656, -0.185656, -0.185656, -0.185656])

		names.append("HeadYaw")
		times.append([3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52])
		keys.append([-0.0537319, -0.07214, -0.07214, -0.0782759, -0.0859461, -0.090548, -0.092082, -0.090548])

		names.append("RElbowRoll")
		times.append([3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52])
		keys.append([0.42496, 0.29457, 0.219404, 0.0349066, 0.0349066, 0.0349066, 0.0349066, 0.0349066])

		names.append("RElbowYaw")
		times.append([3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52])
		keys.append([1.20261, 1.14279, 1.11518, 1.0891, 1.08756, 1.0891, 1.0891, 1.0891])

		names.append("RHand")
		times.append([3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52])
		keys.append([0.2972, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968])

		names.append("RShoulderPitch")
		times.append([3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52])
		keys.append([0.998676, 0.975666, 0.997142, 1.03549, 1.33922, 1.48035, 1.48035, 1.48035])

		names.append("RShoulderRoll")
		times.append([3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52])
		keys.append([-0.00464392, 0.162562, 0.18097, 0.0873961, -0.0614018, -0.0598679, -0.0598679, -0.0598679])

		names.append("RWristYaw")
		times.append([3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52])
		keys.append([0.125746, 0.08126, 0.079726, 0.076658, 0.079726, 0.0843279, 0.0843279, 0.0843279])


		return [names, keys, times]

	@staticmethod
	def HugMotion():
		names = list()
		times = list()
		keys = list()
		names.append("LElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([-0.398798, -0.398798, -0.398798, -0.398798, -0.43408, -0.532256, -0.682588, -0.839056, -1.32687, -1.45879, -1.46339, -1.47106, -1.45726, -1.333, -0.371186, -0.369652, -0.369652])

		names.append("LElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([-1.19963, -1.19963, -1.19963, -1.19963, -1.2027, -1.2027, -1.2027, -1.03549, -0.544612, -0.216336, -0.197928, -0.250084, -0.504728, -0.500126, -0.481718, -0.480184, -0.480184])

		names.append("LHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([0.3052, 0.3052, 0.3052, 0.3052, 0.3052, 0.3048, 0.3052, 0.3048, 0.3052, 0.3052, 0.3052, 0.3052, 0.3052, 0.3052, 0.3052, 0.3048, 0.3052])

		names.append("LShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([1.48487, 1.48487, 1.48487, 1.48487, 1.45112, 0.967912, 0.506178, 0.133416, 0.13495, 0.13495, 0.13495, 0.122678, 0.12728, 1.04921, 1.44959, 1.49101, 1.49101])

		names.append("LShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([0.161028, 0.162562, 0.162562, 0.162562, 0.0183661, -0.205598, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, 0.00455999, 0.366584, 0.259204, 0.253068, 0.254602])

		names.append("LWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([0.079726, 0.079726, 0.079726, 0.079726, 0.0674541, -0.150374, -0.3636, -0.9005, -1.1352, -1.13827, -1.13827, -1.13213, -1.23491, -0.882092, -0.875956, -0.879024, -0.879024])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([0.397348, 0.397348, 0.397348, 0.400416, 0.457174, 0.673468, 0.937316, 1.06924, 1.09072, 1.14287, 1.14134, 1.15514, 1.24718, 1.14287, 0.926578, 0.872888, 0.872888])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([1.18267, 1.18267, 1.18267, 1.19648, 1.20722, 1.21182, 1.21028, 1.19034, 1.08603, 0.822182, 0.766958, 0.77923, 0.928028, 0.908086, 0.908086, 0.908086, 0.90962])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298, 0.298])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([1.50643, 1.50643, 1.50643, 1.50643, 1.42053, 1.16435, 0.898966, 0.825334, 0.826868, 0.845276, 0.843742, 0.842208, 0.797722, 1.06924, 1.70432, 1.70432, 1.70432])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([-0.0506639, -0.0506639, -0.04913, -0.0061779, 0.00455999, 0.00149202, 0.138018, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.0858622, -0.270026, -0.296104, -0.266958, -0.266958])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52])
		keys.append([0.082794, 0.082794, 0.082794, 0.0889301, 0.10427, 0.11194, 0.115008, 0.346642, 0.644238, 0.77923, 0.93263, 0.93263, 0.493906, 0.21932, 0.0904641, 0.0904641, 0.0904641])


		return [names, keys, times]

	@staticmethod
	def kissMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.96, 1.8])
		keys.append([-0.01078, -0.01078])

		names.append("HeadYaw")
		times.append([0.96, 1.8])
		keys.append([0.010696, 0.010696])

		# names.append("LAnklePitch")
		# times.append([1.12])
		# keys.append([-0.359129])

		# names.append("LAnkleRoll")
		# times.append([1.12])
		# keys.append([-0.0797476])

		names.append("LElbowRoll")
		times.append([0.96, 1.4, 1.8, 2.12])
		keys.append([-1.56617, -0.658043, -1.56617, -0.658043])

		names.append("LElbowYaw")
		times.append([0.96, 1.4, 1.8, 2.12])
		keys.append([-0.624379, -1.26866, -0.624379, -1.26866])

		names.append("LHand")
		times.append([0.96, 1.4, 1.8, 2.12])
		keys.append([0.917114, 1, 0.917114, 1])

		# names.append("LHipPitch")
		# times.append([1.12])
		# keys.append([-0.27941])

		# names.append("LHipRoll")
		# times.append([1.12])
		# keys.append([0.168548])

		# names.append("LHipYawPitch")
		# times.append([1.12])
		# keys.append([-0.170318])

		# names.append("LKneePitch")
		# times.append([1.12])
		# keys.append([0.680776])

		names.append("LShoulderPitch")
		times.append([0.96, 1.4, 1.8, 2.12])
		keys.append([0.496974, 0.225456, 0.496974, 0.225456])

		names.append("LShoulderRoll")
		times.append([0.96, 1.4, 1.8, 2.12])
		keys.append([0, 0.05058, 0, 0.05058])

		names.append("LWristYaw")
		times.append([0.96, 1.4, 1.8, 2.12])
		keys.append([-1.00941, -1.00941, -1.00941, -1.00941])

		# names.append("RAnklePitch")
		# times.append([1.12])
		# keys.append([-0.184108])

		# names.append("RAnkleRoll")
		# times.append([1.12])
		# keys.append([0.0675357])

		names.append("RElbowRoll")
		times.append([0.96, 1.4, 1.8, 2.12])
		keys.append([0.504728, 0.431096, 0.504728, 0.431096])

		names.append("RElbowYaw")
		times.append([0.96, 1.4, 1.8, 2.12])
		keys.append([0.42641, 0.41107, 0.42641, 0.41107])

		names.append("RHand")
		times.append([0.96, 1.8])
		keys.append([0.630909, 0.630909])

		# names.append("RHipPitch")
		# times.append([1.12])
		# keys.append([-0.336004])

		# names.append("RHipRoll")
		# times.append([1.12])
		# keys.append([0.0015544])

		# names.append("RKneePitch")
		# times.append([1.12])
		# keys.append([0.556428])

		names.append("RShoulderPitch")
		times.append([0.96, 1.4, 1.8, 2.12])
		keys.append([1.14441, 1.10912, 1.14441, 1.10912])

		names.append("RShoulderRoll")
		times.append([0.96, 1.4, 1.8, 2.12])
		keys.append([-0.271559, -0.253151, -0.271559, -0.253151])

		names.append("RWristYaw")
		times.append([0.96, 1.8])
		keys.append([0.958708, 0.958708])

		return [names, keys, times]

	@staticmethod
	def ListenAgMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([-0.177986, -0.177986, -0.177986, -0.17952, -0.177986, -0.113558, -0.070606, -0.0506639, -0.165714,
					 -0.467912, -0.337522, -0.27156, -0.273094, -0.273094, -0.273094])

		names.append("HeadYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([-0.00310993, -0.00310993, -0.00310993, -0.00310993, 0.11961, 0.45709, 0.589014, 0.598218, 0.504644,
					 0.101202, 0.0935321, 0.0935321, 0.0935321, 0.0935321, 0.0935321])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append(
			[0.40195, 0.40195, 0.398882, 0.449504, 1.54462, 1.54462, 1.54462, 1.54462, 1.54462, 1.52637, 1.33922,
			 1.20116, 1.17202, 1.17202, 1.17202])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append(
			[1.18574, 1.18574, 1.18574, 1.19034, 1.30079, 1.44345, 1.4726, 1.4726, 1.46646, 1.48027, 1.48487, 1.4864,
			 1.4864, 1.4864, 1.4864])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append(
			[0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956, 0.2956,
			 0.2956, 0.2956])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append(
			[1.43126, 1.4328, 1.4328, 1.41746, 0.980268, 0.190258, -0.0858622, -0.108872, 0.00771189, 1.47728, 1.94669,
			 1.94515, 1.94515, 1.94669, 1.94669])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append(
			[-0.0782759, -0.0782759, -0.0782759, 0.030638, 0.133416, 0.159494, 0.237728, 0.314159, 0.248466, 0.0398421,
			 -0.047596, -0.0261199, -0.0322559, -0.0322559, -0.0322559])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.10427, 0.10427, 0.10427, 0.113474, 0.113474, 0.113474, 0.115008, 0.115008, 0.0659201, -0.47865,
					 -0.552282, -0.550748, -0.549214, -0.550748, -0.549214])

		return [names, keys, times]

	@staticmethod
	def LoadMotion():
		names = list()
		times = list()
		keys = list()
		
		names.append("HeadPitch")
		times.append([1])
		keys.append([-0.315905])

		names.append("HeadYaw")
		times.append([1])
		keys.append([0.010696])

		# names.append("LAnklePitch")
		# times.append([1])
		# keys.append([-0.348392])

		# names.append("LAnkleRoll")
		# times.append([1])
		# keys.append([-0.0521356])

		names.append("LElbowRoll")
		times.append([1])
		keys.append([-1.55237])

		names.append("LElbowYaw")
		times.append([1])
		keys.append([-1.2794])

		names.append("LHand")
		times.append([1])
		keys.append([0.0949353])

		# names.append("LHipPitch")
		# times.append([1])
		# keys.append([-1.14459])

		# names.append("LHipRoll")
		# times.append([1])
		# keys.append([-0.00172607])

		# names.append("LHipYawPitch")
		# times.append([1])
		# keys.append([-0.256221])

		# names.append("LKneePitch")
		# times.append([1])
		# keys.append([1.31432])

		names.append("LShoulderPitch")
		times.append([1])
		keys.append([-0.412688])

		names.append("LShoulderRoll")
		times.append([1])
		keys.append([0.983252])

		names.append("LWristYaw")
		times.append([1])
		keys.append([-1.78715])

		# names.append("RAnklePitch")
		# times.append([1])
		# keys.append([-0.202516])

		# names.append("RAnkleRoll")
		# times.append([1])
		# keys.append([0.0690697])

		names.append("RElbowRoll")
		times.append([1])
		keys.append([1.55245])

		names.append("RElbowYaw")
		times.append([1])
		keys.append([0.880473])

		names.append("RHand")
		times.append([1])
		keys.append([0.0396627])

		# names.append("RHipPitch")
		# times.append([1])
		# keys.append([-1.18124])

		# names.append("RHipRoll")
		# times.append([1])
		# keys.append([0.0199624])

		# names.append("RKneePitch")
		# times.append([1])
		# keys.append([1.19611])

		names.append("RShoulderPitch")
		times.append([1])
		keys.append([-0.737812])

		names.append("RShoulderRoll")
		times.append([1])
		keys.append([-0.915841])

		names.append("RWristYaw")
		times.append([1])
		keys.append([0.923426])
 
		return [names, keys, times]

	@staticmethod
	def ManyMotion():
		names = list()
		times = list()
		keys = list()

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.55535, 0.55535, 0.553816, 0.582962, 0.653526, 0.906636, 0.99254, 0.753236, 1.10299, 0.817664, 0.926578, 0.888228, 0.651992, 0.538476, 0.535408])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([1.13972, 1.13972, 1.13972, 1.15199, 1.15659, 1.09217, 0.25767, 0.478566, 0.79457, 0.338972, 1.12591, 1.0983, 1.09677, 1.09677, 1.09677])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.304, 0.3036, 0.3036, 0.3036, 0.3036, 0.3036, 0.304, 0.3036, 0.3036, 0.304, 0.3036, 0.304, 0.3036, 0.3036, 0.3036])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([1.54785, 1.54785, 1.54785, 1.44967, 0.995608, 0.70875, 0.728692, 0.645856, 0.596768, 0.682672, 0.618244, 1.10299, 1.59847, 1.64142, 1.64142])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([-0.0614018, -0.0614018, -0.0614018, -0.136568, -0.131966, 0.078192, 0.0168321, -0.231676, 0.0367742, -0.17952, -0.0322559, 0.191708, -0.219404, -0.16418, -0.161112])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.337438, 0.337438, 0.337438, 0.337438, 0.34204, 0.431012, 0.431012, 0.77923, 0.797638, 0.826784, 0.951038, 0.45709, 0.338972, 0.338972, 0.338972])


		return [names, keys, times]

	@staticmethod
	def Pull_ropeMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([0.145688, 0.133416, 0.133416, 0.133416, 0.133416])

		names.append("HeadYaw")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([0.024502, 0.0183661, 0.016832, 0.0183661, 0.016832])

		# names.append("LAnklePitch")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([-0.173384, -0.173384, -0.173384, -0.173384, -0.173384])

		# names.append("LAnkleRoll")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([-0.0183661, -0.0183661, -0.0183661, -0.0183661, -0.0183661])

		names.append("LElbowRoll")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([-1.55083, -1.56004, -1.55237, -1.56004, -1.55237])

		names.append("LElbowYaw")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([-1.18582, -1.17202, -1.25332, -1.17202, -1.25332])

		names.append("LHand")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([0.0251173, 0.0251173, 0.0251173, 0.0251173, 0.0251173])

		# names.append("LHipPitch")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([-0.291418, -0.289883, -0.291418, -0.289883, -0.291418])

		# names.append("LHipRoll")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([-0.049046, -0.049046, -0.049046, -0.049046, -0.049046])

		# names.append("LHipYawPitch")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([-0.162562, -0.162562, -0.162562, -0.162562, -0.162562])

		# names.append("LKneePitch")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([0.532256, 0.532256, 0.532256, 0.532256, 0.532256])

		names.append("LShoulderPitch")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([1.22869, 0.674919, 1.64594, 0.674919, 1.64594])

		names.append("LShoulderRoll")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([0.00872665, 0.00872665, 0.00872665, 0.00872665, 0.00872665])

		names.append("LWristYaw")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([-1.11373, -1.10606, -1.10606, -1.10606, -1.10606])

		# names.append("RAnklePitch")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([-0.380389, -0.380389, -0.380389, -0.380389, -0.380389])

		# names.append("RAnkleRoll")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([0.039926, 0.039926, 0.039926, 0.039926, 0.039926])

		names.append("RElbowRoll")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([1.56165, 1.56012, 1.56012, 1.56012, 1.56012])

		names.append("RElbowYaw")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([1.1704, 1.16733, 1.24863, 1.16733, 1.24863])

		names.append("RHand")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([0.00802646, 0.00802646, 0.00802646, 0.00802646, 0.00802646])

		# names.append("RHipPitch")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([-0.291501, -0.291501, -0.291501, -0.291501, -0.291501])

		# names.append("RHipRoll")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([-0.101202, -0.101202, -0.101202, -0.101202, -0.101202])

		# names.append("RKneePitch")
		# times.append([1.33333, 2, 2.66667, 3.33333, 4])
		# keys.append([0.737896, 0.736361, 0.737896, 0.736361, 0.737896])

		names.append("RShoulderPitch")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([0.840674, 1.50796, 0.561486, 1.50796, 0.561486])

		names.append("RShoulderRoll")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([-0.00872665, -0.00872665, -0.00872665, -0.00872665, -0.00872665])

		names.append("RWristYaw")
		times.append([1.33333, 2, 2.66667, 3.33333, 4])
		keys.append([1.13665, 1.13665, 1.13665, 1.13665, 1.13665])
		
		return [names, keys, times]

	@staticmethod
	def PullMotion():
		names = list()
		times = list()
		keys = list()
		names.append("HeadPitch")
		times.append([3.12])
		keys.append([-0.0245859])

		names.append("HeadYaw")
		times.append([3.12])
		keys.append([0.00609404])

		# names.append("LAnklePitch")
		# times.append([3.12])
		# keys.append([-0.104485])

		# names.append("LAnkleRoll")
		# times.append([3.12])
		# keys.append([0.0092244])

		names.append("LElbowRoll")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([-0.805309, -0.914223, -0.912689, -0.912689, -0.912689, -0.326699])

		names.append("LElbowYaw")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([-0.93118, -0.490923, -0.492455, -0.546147, -0.553816, -0.759372])

		names.append("LHand")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([0.9088, 0.9088, 0.9088, 0.9088, 0.9088, 0.918933])

		# names.append("LHipPitch")
		# times.append([3.12])
		# keys.append([0.0596046])

		# names.append("LHipRoll")
		# times.append([3.12])
		# keys.append([-0.0324061])

		# names.append("LHipYawPitch")
		# times.append([3.12])
		# keys.append([0.0183645])

		# names.append("LKneePitch")
		# times.append([3.12])
		# keys.append([0.0702441])

		names.append("LShoulderPitch")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([1.25784, 1.25324, 1.2517, 1.25324, 1.25477, 1.56771])

		names.append("LShoulderRoll")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([-0.314159, -0.314159, -0.314159, -0.314159, -0.314159, 0.329768])

		names.append("LWristYaw")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([-1.15821, -1.28707, -1.34843, -1.3607, -1.39291, -1.02629])

		# names.append("RAnklePitch")
		# times.append([3.12])
		# keys.append([-0.0951351])

		# names.append("RAnkleRoll")
		# times.append([3.12])
		# keys.append([-0.00302827])

		names.append("RElbowRoll")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([0.487854, 1.38678, 1.54462, 1.5187, 0.780848, 0.291501])

		names.append("RElbowYaw")
		times.append([1.04, 1.32, 1.76, 2.28, 2.76, 3.12])
		keys.append([0.984786, 0.937977, 0.697927, -0.108956, 1.27318, 0.77923])

		names.append("RHand")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([0.29, 0.2896, 0.29, 0.29, 0.29, 0.918205])

		# names.append("RHipPitch")
		# times.append([3.12])
		# keys.append([0.0367591])

		# names.append("RHipRoll")
		# times.append([3.12])
		# keys.append([0.0107584])

		# names.append("RKneePitch")
		# times.append([3.12])
		# keys.append([0.0839559])

		names.append("RShoulderPitch")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([1.47728, 0.642787, 0.437231, 0.40962, 0.389678, 1.56779])

		names.append("RShoulderRoll")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([-0.17185, -0.271559, -0.658129, -0.196393, -0.440299, -0.320648])

		names.append("RWristYaw")
		times.append([1.04, 1.2, 1.76, 2.28, 2.76, 3.12])
		keys.append([0.193243, -0.286901, -0.27923, -0.190258, -0.325249, 0.967912])


		return [names, keys, times]
	

	@staticmethod
	def RememberMotion():
		names = list()
		times = list()
		keys = list()


		names.append("RElbowRoll")
		times.append(
			[0.48, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04,
			 9.52, 10.04, 10.52])
		keys.append(
			[0.145772, 0.145772, 0.145772, 0.167248, 0.184122, 0.368202, 0.722556, 1.47422, 1.54462, 1.54462, 1.54462,
			 1.54462, 1.54462, 1.48649, 0.826868, 0.681138, 0.62438, 0.484786, 0.484786, 0.484786, 0.484786])

		names.append("RElbowYaw")
		times.append(
			[0.48, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04,
			 9.52, 10.04, 10.52])
		keys.append(
			[0.981718, 0.981718, 0.981718, 0.998592, 1.04461, 1.23023, 1.44805, 1.42044, 1.27471, 1.16733, 1.12745,
			 1.12591, 1.12591, 1.13972, 1.12745, 1.09984, 1.08756, 1.08756, 1.08756, 1.08603, 1.08756])

		names.append("RHand")
		times.append(
			[0.48, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04,
			 9.52, 10.04, 10.52])
		keys.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

		names.append("RShoulderPitch")
		times.append(
			[0.48, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04,
			 9.52, 10.04, 10.52])
		keys.append(
			[1.4466, 1.4466, 1.4466, 1.30241, 0.62438, 0.0061779, -0.217786, -0.216252, -0.214718, -0.217786, -0.21932,
			 -0.220854, -0.220854, -0.217786, -0.21932, -0.0106959, 1.31928, 1.55859, 1.55859, 1.55859, 1.55859])

		names.append("RShoulderRoll")
		times.append(
			[0.48, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04,
			 9.52, 10.04, 10.52])
		keys.append(
			[-0.066004, -0.066004, -0.066004, -0.0567999, -0.0383921, -0.139636, -0.362066, -0.527738, -0.510864,
			 -0.254686, -0.21787, -0.40195, -0.523136, -0.63205, -0.645856, -0.581428, -0.253152, -0.199462, -0.173384,
			 -0.173384, -0.173384])

		names.append("RWristYaw")
		times.append(
			[0.48, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04,
			 9.52, 10.04, 10.52])
		keys.append([0.35738, 0.35738, 0.35738, 0.35738, 0.691792, 1.32994, 1.43271, 1.44959, 1.46493, 1.46646, 1.46493,
					 1.46339, 1.46339, 1.45266, 1.43578, 0.941834, -0.635118, -0.721022, -0.721022, -0.721022,
					 -0.721022])

		return [names, keys, times]

	@staticmethod
	def RunMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.8, 6.64])
		keys.append([-0.0245859, -0.0245859])

		names.append("HeadYaw")
		times.append([1.8, 6.64])
		keys.append([0.00609404, 0.00609404])

		# names.append("LAnklePitch")
		# times.append([1.8, 6.64])
		# keys.append([-0.411285, -0.104485])

		# names.append("LAnkleRoll")
		# times.append([1.8, 6.64])
		# keys.append([-0.0812816, 0.0092244])

		names.append("LElbowRoll")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append([-0.507712, -0.484702, -0.501576, -0.484702, -0.501576, -0.484702, -0.501576, -0.484702, -0.501576,
					 -0.326699])

		names.append("LElbowYaw")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append(
			[-1.6629, -1.64296, -1.65676, -1.64296, -1.65676, -1.64296, -1.65676, -1.64296, -1.65676, -0.759372])

		names.append("LHand")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append([0.064, 0.064, 0.064, 0.064, 0.064, 0.064, 0.064, 0.064, 0.064, 0.918933])

		# names.append("LHipPitch")
		# times.append([1.8, 6.64])
		# keys.append([-0.191972, 0.0596046])

		# names.append("LHipRoll")
		# times.append([1.8, 6.64])
		# keys.append([0.15014, -0.0324061])

		# names.append("LHipYawPitch")
		# times.append([1.8, 6.64])
		# keys.append([-0.372806, 0.0183645])

		# names.append("LKneePitch")
		# times.append([1.8, 6.64])
		# keys.append([0.966101, 0.0702441])

		names.append("LShoulderPitch")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append([0.742414, 1.99876, 0.76389, 1.99877, 0.76389, 1.99877, 0.76389, 1.99877, 0.76389, 1.56771])

		names.append("LShoulderRoll")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append(
			[0.0935321, 0.118076, 0.128814, 0.118076, 0.128814, 0.118076, 0.128814, 0.118076, 0.128814, 0.329768])

		names.append("LWristYaw")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append(
			[-0.88516, -0.849878, -1.23491, -0.849878, -1.23491, -0.849878, -1.23491, -0.849878, -1.23491, -1.02629])

		# names.append("RAnklePitch")
		# times.append([1.8, 6.64])
		# keys.append([-0.38813, -0.0951351])

		# names.append("RAnkleRoll")
		# times.append([1.8, 6.64])
		# keys.append([0.0475937, -0.00302827])

		names.append("RElbowRoll")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append([1.06617, 1.13827, 1.08151, 1.13827, 1.08151, 1.13827, 1.08151, 1.13827, 1.08151, 0.291501])

		names.append("RElbowYaw")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append([1.8561, 1.93433, 1.90058, 1.93433, 1.90058, 1.93433, 1.90058, 1.93433, 1.90058, 0.77923])

		names.append("RHand")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append([0.1168, 0.1168, 0.1168, 0.1168, 0.1168, 0.1168, 0.1168, 0.1168, 0.1168, 0.918205])

		# names.append("RHipPitch")
		# times.append([1.8, 6.64])
		# keys.append([-0.148855, 0.0367591])

		# names.append("RHipRoll")
		# times.append([1.8, 6.64])
		# keys.append([-0.0383295, 0.0107584])

		# names.append("RKneePitch")
		# times.append([1.8, 6.64])
		# keys.append([0.892375, 0.0839559])

		names.append("RShoulderPitch")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append([1.86078, 0.757838, 2.08567, 0.757838, 2.08567, 0.757838, 2.08567, 0.757838, 2.08567, 1.56779])

		names.append("RShoulderRoll")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append([0.0889301, 0.076658, -0.0859461, 0.076658, -0.0859461, 0.076658, -0.0859461, 0.076658, -0.0859461,
					 -0.320648])

		names.append("RWristYaw")
		times.append([2.04, 2.52, 3.04, 3.44, 3.96, 4.4, 4.92, 5.28, 5.8, 6.64])
		keys.append([-0.101286, -0.107422, -0.138102, -0.107422, -0.138102, -0.107422, -0.138102, -0.107422, -0.138102,
					 0.967912])

		return [names, keys, times]

	@staticmethod
	def SadMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.36])
		keys.append([0.514872])

		names.append("HeadYaw")
		times.append([1.36])
		keys.append([0.00349066])

		return [names, keys, times]

	@staticmethod
	def ShoutMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append([-0.414222, -0.538476, -0.538476, -0.538476, -0.538476, -0.543078, -0.543078, -0.544612, -0.543078,
					 -0.543078, -0.543078, -0.543078, -0.544612, -0.374338, -0.170316, -0.165714, -0.165714, -0.165714])

		names.append("HeadYaw")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append([-0.115092, -0.113558, -0.113558, -0.113558, -0.113558, -0.113558, -0.113558, -0.113558, -0.112024,
					 -0.115092, -0.115092, -0.115092, -0.115092, 0.0122299, 0.0106959, 0.0106959, 0.0106959, 0.0106959])

		names.append("LElbowRoll")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[-0.481634, -0.481634, -0.47243, -0.538392, -0.691792, -1.54462, -1.54462, -1.54462, -1.26244, -0.340506,
			 -0.340506, -0.340506, -0.34204, -0.34204, -0.34204, -0.340506, -0.34204, -0.340506])

		names.append("LElbowYaw")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[-1.6767, -1.6767, -1.6767, -1.67824, -1.67824, -1.51257, -1.37757, -1.40365, -1.44507, -1.43893, -1.43893,
			 -1.43893, -1.43893, -1.43893, -1.43893, -1.43893, -1.43893, -1.43893])

		names.append("LHand")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[0.258, 0.258, 0.258, 0.258, 0.258, 0.258, 0.258, 0.258, 0.258, 0.258, 0.258, 0.258, 0.258, 0.258, 0.258,
			 0.258, 0.258, 0.258])

		names.append("LShoulderPitch")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[1.59532, 1.59532, 1.59532, 1.15353, 0.194776, 0.179436, 0.21165, 0.355846, 1.55697, 1.59225, 1.59072,
			 1.59072, 1.59072, 1.59072, 1.59072, 1.59072, 1.59072, 1.59072])

		names.append("LShoulderRoll")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[0.0367742, 0.0367742, 0.024502, -0.067538, -0.176452, -0.314159, -0.314159, -0.219404, 0.228524, 0.128814,
			 0.128814, 0.128814, 0.128814, 0.128814, 0.128814, 0.128814, 0.128814, 0.128814])

		names.append("LWristYaw")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[0.734744, 0.734744, 0.737812, 0.585946, -0.042994, -0.14117, -0.185656, -0.16418, -0.047596, 0.730142,
			 0.743948, 0.743948, 0.743948, 0.743948, 0.743948, 0.743948, 0.743948, 0.743948])

		names.append("RElbowRoll")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[0.420358, 0.421892, 0.415756, 0.480184, 0.58603, 1.54462, 1.54462, 1.52177, 1.29781, 0.260822, 0.257754,
			 0.257754, 0.257754, 0.259288, 0.257754, 0.257754, 0.257754, 0.257754])

		names.append("RElbowYaw")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[1.50635, 1.50635, 1.50635, 1.50481, 1.50635, 1.4818, 1.41431, 1.45419, 1.44652, 1.44038, 1.44038, 1.44038,
			 1.44038, 1.43885, 1.44038, 1.44038, 1.44038, 1.44038])

		names.append("RHand")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[0.2336, 0.2336, 0.2336, 0.2336, 0.2336, 0.2336, 0.2336, 0.2336, 0.2336, 0.2336, 0.2336, 0.2336, 0.2336,
			 0.2336, 0.2336, 0.2336, 0.2336, 0.2336])

		names.append("RShoulderPitch")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[1.50183, 1.50183, 1.51717, 1.2073, 0.259288, 0.205598, 0.204064, 0.29457, 1.47882, 1.48035, 1.48189,
			 1.48189, 1.48189, 1.48189, 1.48035, 1.48189, 1.48189, 1.48189])

		names.append("RShoulderRoll")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[0.030638, 0.030638, 0.029104, 0.0843279, 0.314159, 0.314159, 0.314159, 0.25767, -0.200996, -0.0123138,
			 -0.0123138, -0.0123138, -0.0123138, -0.0153821, -0.0153821, -0.0153821, -0.0153821, -0.0153821])

		names.append("RWristYaw")
		times.append(
			[2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04,
			 10.52])
		keys.append(
			[-0.658128, -0.658128, -0.658128, -0.65506, -0.289968, -0.282298, -0.282298, -0.285366, -0.3636, -1.24412,
			 -1.24412, -1.24412, -1.24412, -1.24412, -1.24258, -1.24412, -1.24412, -1.24412])

		return [names, keys, times]
	@staticmethod
	def SleepMotion():
		names = list()
		times = list()
		keys = list()
		names.append("HeadPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([-0.021518, -0.023052, -0.023052, -0.023052, -0.023052, -0.023052, -0.021518, -0.021518, -0.023052, -0.023052, 0.0873961, 0.243864, 0.42641, 0.512937, 0.512937, 0.512937, 0.467828, 0.38806, 0.253068, 0.0950661, -0.070606, -0.0767419])

		names.append("HeadYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([-0.0123138, -0.0107799, -0.0123138, -0.0123138, -0.0123138, -0.0107799, -0.0123138, -0.0123138, -0.0123138, -0.0107799, -0.0107799, -0.0107799, -0.0107799, -0.0107799, -0.0107799, -0.0107799, -0.0153821, -0.0153821, -0.016916, -0.016916, -0.016916, -0.0123138])

		names.append("LElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([-0.57214, -0.573674, -0.57214, -0.57214, -0.665714, -0.739346, -0.914222, -1.06302, -1.1658, -1.1658, -1.16733, -1.16733, -1.1658, -1.1658, -1.1658, -1.1658, -1.1658, -1.1658, -1.16273, -1.15353, -1.15046, -1.15506])

		names.append("LElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([-1.22264, -1.22264, -1.22264, -1.22264, -1.22571, -1.22724, -1.21497, -0.87749, -0.538476, -0.538476, -0.538476, -0.538476, -0.538476, -0.538476, -0.538476, -0.538476, -0.538476, -0.538476, -0.538476, -0.538476, -0.538476, -0.54001])

		names.append("LHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([0.916, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164])

		names.append("LShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([1.50788, 1.50788, 1.50788, 1.50788, 1.40817, 0.92496, 0.73321, 0.707132, 0.713268, 0.757754, 0.768492, 0.768492, 0.773094, 0.777696, 0.777696, 0.791502, 0.79457, 0.79457, 0.808376, 0.811444, 0.83292, 0.877406])

		names.append("LShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([0.199378, 0.199378, 0.199378, 0.19631, -0.047596, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159])

		names.append("LWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([0.056716, 0.056716, 0.056716, 0.056716, 0.056716, -0.044528, -0.046062, -0.047596, -0.046062, -0.044528, -0.044528, -0.044528, -0.044528, -0.044528, -0.044528, -0.044528, -0.044528, -0.044528, -0.044528, -0.044528, -0.044528, -0.044528])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([0.403484, 0.403484, 0.403484, 0.403484, 0.451038, 0.682672, 1.01555, 1.25485, 1.29014, 1.28093, 1.28093, 1.28093, 1.284, 1.28553, 1.2886, 1.28553, 1.2886, 1.28707, 1.28093, 1.27019, 1.26099, 1.26099])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([1.32687, 1.32687, 1.32687, 1.32687, 1.33454, 1.36522, 1.56157, 1.78093, 1.88678, 1.88678, 1.88678, 1.88678, 1.88678, 1.88678, 1.88678, 1.88831, 1.88831, 1.88831, 1.88831, 1.88831, 1.88831, 1.88831])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([1.48802, 1.48802, 1.48802, 1.48802, 1.42973, 1.09685, 0.917374, 0.894364, 0.932714, 0.937316, 0.937316, 0.937316, 0.937316, 0.937316, 0.93885, 0.941918, 0.943452, 0.941918, 0.944986, 0.955724, 0.971064, 0.972598])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([-0.00464392, -0.00464392, -0.00464392, -0.00464392, 0.0919981, 0.223922, 0.28835, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.306758])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52, 11.04])
		keys.append([0.118076, 0.118076, 0.118076, 0.118076, 0.12728, 0.148756, 0.724006, 0.958708, 1.19034, 1.19034, 1.19034, 1.19034, 1.19034, 1.19034, 1.19034, 1.18881, 1.1796, 1.1796, 1.15506, 1.15046, 1.06916, 1.02007])



		return [names, keys, times]
	@staticmethod
	def SmallMotion():
		names = list()
		times = list()
		keys = list()
		
		names.append("LElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([-0.392662, -0.392662, -0.391128, -0.47243, -0.670316, -0.79457, -0.84059, -0.74088, -0.501576, -0.246932, -0.179436, -0.179436])

		names.append("LElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([-1.20116, -1.20116, -1.20116, -1.21037, -1.21344, -1.20423, -1.19963, -1.1981, -1.19656, -1.1981, -1.1981, -1.1981])

		names.append("LHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([0.3052, 0.3052, 0.3052, 0.3052, 0.3048, 0.3052, 0.3048, 0.3052, 0.3052, 0.3052, 0.3052, 0.3048])

		names.append("LShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([1.46186, 1.46033, 1.46186, 1.39436, 1.15199, 0.974048, 0.93263, 1.04308, 1.2425, 1.45726, 1.50635, 1.50635])

		names.append("LShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([0.14262, 0.14262, 0.14262, -0.00771189, -0.096684, -0.161112, -0.199462, -0.158044, 0.00916195, 0.133416, 0.0966001, 0.0950661])

		names.append("LWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([0.098134, 0.098134, 0.098134, 0.0950661, -0.265424, -0.296104, -0.280764, -0.16418, -0.130432, -0.1335, -0.1335, -0.1335])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([0.400416, 0.400416, 0.383542, 0.428028, 0.619778, 0.776246, 0.836072, 0.76244, 0.57836, 0.383542, 0.316046, 0.316046])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([1.18881, 1.19034, 1.18881, 1.19341, 1.20722, 1.20722, 1.20722, 1.20108, 1.19955, 1.19955, 1.19955, 1.19955])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([1.44047, 1.44047, 1.46808, 1.43893, 1.17202, 1.00174, 0.96186, 1.02629, 1.25792, 1.44507, 1.48189, 1.48189])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([-0.0337899, -0.0337899, -0.0107799, 0.113474, 0.25767, 0.277612, 0.294486, 0.253068, 0.0429101, -0.113558, -0.0399261, -0.0399261])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04])
		keys.append([0.0935321, 0.0935321, 0.0935321, 0.098134, 0.10427, 0.10427, 0.10427, 0.099668, 0.07359, 0.07359, 0.07359, 0.0720561])

		return [names, keys, times]

	@staticmethod
	def ThereMotion():
		names = list()
		times = list()
		keys = list()
		names.append("HeadPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([-0.300706, -0.30224, -0.30224, -0.30224, -0.339056, -0.365134, -0.444902, -0.443368, -0.383542, -0.377406, -0.377406])

		names.append("HeadYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([0.0152981, 0.0152981, 0.0168321, -0.200996, -0.605972, -0.605972, -0.536942, -0.199462, 0.0183661, -4.19617e-05, -4.19617e-05])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([0.173384, 0.174918, 0.174918, 0.228608, 0.220938, 0.247016, 0.167248, 0.138102, 0.1335, 0.1335, 0.1335])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([1.26091, 1.26091, 1.26091, 1.33147, 1.35755, 1.34221, 1.32687, 1.32227, 1.32073, 1.32227, 1.32227])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968, 0.2968])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([1.41746, 1.41746, 1.41746, 1.00635, 0.00157595, -0.427944, -0.294486, 0.880558, 1.40519, 1.42359, 1.42359])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([-0.023052, -0.023052, -0.016916, -0.024586, -0.464844, -0.492456, -0.414222, -0.191792, -0.0107799, -0.0061779, -0.0061779])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52])
		keys.append([-0.124296, -0.124296, -0.124296, -0.124296, -0.124296, -0.144238, -0.14884, -0.14884, -0.147306, -0.145772, -0.145772])

		return [names, keys, times]

	@staticmethod
	def TiredMotion():
		names = list()
		times = list()
		keys = list()
		names.append("HeadPitch")
		times.append([0.96, 1.68, 3.28, 3.96, 4.52, 5.08])
		keys.append([-0.0261199, 0.427944, 0.308291, 0.11194, -0.013848, 0.061318])

		names.append("HeadYaw")
		times.append([0.96, 1.68, 3.28, 3.96, 4.52, 5.08])
		keys.append([-0.234743, -0.622845, -0.113558, -0.00617796, -0.027654, -0.036858])

		names.append("LElbowRoll")
		times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
		keys.append([-0.866668, -0.868202, -0.822183, -0.992455, -0.966378, -0.990923])

		names.append("LElbowYaw")
		times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
		keys.append([-0.957257, -0.823801, -1.00788, -0.925044, -1.24412, -0.960325])

		names.append("LHand")
		times.append([1.52, 3.12, 3.8, 4.92])
		keys.append([0.132026, 0.132026, 0.132026, 0.132026])

		names.append("LShoulderPitch")
		times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
		keys.append([0.863599, 0.858999, 0.888144, 0.929562, 1.017, 0.977116])

		names.append("LShoulderRoll")
		times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
		keys.append([0.286815, 0.230059, 0.202446, 0.406468, 0.360449, 0.31903])

		names.append("LWristYaw")
		times.append([1.52, 3.12, 3.8, 4.92])
		keys.append([0.386526, 0.386526, 0.386526, 0.386526])

		names.append("RElbowRoll")
		times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
		keys.append([1.28093, 1.39752, 1.57239, 1.24105, 1.22571, 0.840674])

		names.append("RElbowYaw")
		times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
		keys.append([-0.128898, -0.285367, -0.15651, 0.754686, 1.17193, 0.677985])

		names.append("RHand")
		times.append([1.36, 2.96, 3.64, 4.76])
		keys.append([0.166571, 0.166208, 0.166571, 0.166208])

		names.append("RShoulderPitch")
		times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
		keys.append([0.0767419, -0.59515, -0.866668, -0.613558, 0.584497, 0.882091])

		names.append("RShoulderRoll")
		times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
		keys.append([-0.019984, -0.019984, -0.615176, -0.833004, -0.224006, -0.214801])

		names.append("RWristYaw")
		times.append([1.36, 2.96, 3.64, 4.76])
		keys.append([-0.058334, -0.0521979, -0.067538, -0.038392])
		return [names, keys, times]

	@staticmethod
	def TurnMotion():
		names = list()
		times = list()
		keys = list()
		names.append("RElbowRoll")
		times.append([5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52])
		keys.append([0.55535, 0.54768, 0.813062, 1.20883, 1.0539, 0.895898, 0.911238, 1.11526, 1.2794, 1.20423, 0.92351, 0.25622])

		names.append("RElbowYaw")
		times.append([5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52])
		keys.append([1.09063, 1.09063, 1.13819, 1.40357, 1.37596, 1.36368, 1.18881, 1.1612, 1.19341, 1.3146, 1.32687, 1.3284])

		names.append("RHand")
		times.append([5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52])
		keys.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

		names.append("RShoulderPitch")
		times.append([5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52])
		keys.append([0.780848, 1.0493, 0.949588, 0.400416, 0.503194, 1.25179, 1.25332, 1.15361, 0.872888, 0.87749, 1.36837, 1.66903])

		names.append("RShoulderRoll")
		times.append([5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52])
		keys.append([-0.219404, 0.314159, 0.314159, -0.0261199, -0.250084, -0.147306, 0.216252, 0.314159, 0.31136, -0.224006, -0.334454, -0.253152])

		names.append("RWristYaw")
		times.append([5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04, 8.52, 9.04, 9.52, 10.04, 10.52])
		keys.append([-0.520068, 0.0168321, 0.544528, 0.191708, -0.644322, -0.497058, 0.254602, 0.515382, -0.170316, -0.7471, -0.39428, -0.213268])

		return [names, keys, times]

	@staticmethod
	def UphillMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([-0.222472, -0.222472, -0.222472, -0.346726, -0.671952, -0.671952, -0.671952, -0.671952, -0.671952, -0.552282, 0.277612, 0.276078, 0.276078, 0.276078, 0.276078, 0.276078])

		names.append("HeadYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([-0.0153821, -0.0138481, -0.0153821, -0.016916, -0.0276539, -0.0399261, -0.04146, -0.04146, -0.0276539, -0.0322559, -0.0506639, -0.0537319, -0.0521979, -0.0521979, -0.0521979, -0.0521979])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([0.389678, 0.389678, 0.389678, 0.492456, 0.622846, 0.711818, 0.711818, 0.684206, 0.584496, 0.388144, 0.32525, 0.297638, 0.297638, 0.297638, 0.297638, 0.297638])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([1.20108, 1.20108, 1.20261, 1.22256, 1.30386, 1.49714, 1.59839, 1.60912, 1.60145, 1.60145, 1.57844, 1.5493, 1.5493, 1.5493, 1.5493, 1.55083])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([0.3088, 0.3088, 0.3088, 0.3088, 0.3088, 0.3088, 0.3088, 0.3092, 0.3092, 0.3088, 0.3088, 0.3088, 0.3092, 0.3088, 0.3092, 0.3092])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([1.45581, 1.45581, 1.45581, 1.32235, 0.451038, -0.340506, -0.858998, -0.869736, -0.845192, -0.651908, 0.293036, 1.48495, 1.48495, 1.48649, 1.48495, 1.48495])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([-0.066004, -0.066004, -0.0353239, 0.10427, 0.23466, 0.131882, 0.10427, 0.102736, 0.116542, 0.151824, 0.256136, 0.0659201, 0.0643861, 0.0643861, 0.0643861, 0.0643861])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52, 8.04])
		keys.append([0.0889301, 0.0889301, 0.0889301, 0.0935321, 0.371186, 0.401866, 0.404934, 0.404934, 0.415672, 0.414138, 0.408002, 0.392662, 0.392662, 0.392662, 0.392662, 0.392662])

		return [names, keys, times]


	def UpsetMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.12, 1.48, 2.08, 2.36, 2.76, 2.88, 3.16])
		keys.append([0.26315, 0.0724156, -0.121841, -0.426485, -0.191986, -0.0261799, -0.0245859])

		names.append("HeadYaw")
		times.append([3.16])
		keys.append([0.00609404])

		# names.append("LAnklePitch")
		# times.append([3.16])
		# keys.append([-0.104485])

		# names.append("LAnkleRoll")
		# times.append([3.16])
		# keys.append([0.0092244])

		names.append("LElbowRoll")
		times.append([1.36, 1.48, 1.96, 3.16])
		keys.append([-1.34414, -1.52156, -1.35727, -0.326699])

		names.append("LElbowYaw")
		times.append([3.16])
		keys.append([-0.759372])

		names.append("LHand")
		times.append([1.36, 1.84, 3.16])
		keys.append([0.06, 0.17, 0.918933])

		# names.append("LHipPitch")
		# times.append([3.16])
		# keys.append([0.0596046])

		# names.append("LHipRoll")
		# times.append([3.16])
		# keys.append([-0.0324061])

		# names.append("LHipYawPitch")
		# times.append([3.16])
		# keys.append([0.0183645])

		# names.append("LKneePitch")
		# times.append([3.16])
		# keys.append([0.0702441])

		names.append("LShoulderPitch")
		times.append([1.24, 1.36, 1.48, 1.72, 1.84, 2.16, 2.24, 2.48, 2.64, 2.76, 2.88, 3, 3.16])
		keys.append(
			[0.0715585, -0.219262, 0.820305, 1.72922, 0.617847, -0.536912, 0.207432, 1.75545, 0.389208, -0.514347,
			 0.762709, 1.75453, 1.56771])

		names.append("LShoulderRoll")
		times.append([1.72, 1.84, 3.16])
		keys.append([0.232129, 0.172788, 0.329768])

		names.append("LWristYaw")
		times.append([3.16])
		keys.append([-1.02629])

		# names.append("RAnklePitch")
		# times.append([3.16])
		# keys.append([-0.0951351])

		# names.append("RAnkleRoll")
		# times.append([3.16])
		# keys.append([-0.00302827])

		names.append("RElbowRoll")
		times.append([1.48, 3.16])
		keys.append([0.34732, 0.291501])

		names.append("RElbowYaw")
		times.append([3.16])
		keys.append([0.77923])

		names.append("RHand")
		times.append([1.24, 1.72, 3.16])
		keys.append([0.92, 0.79, 0.918205])

		# names.append("RHipPitch")
		# times.append([3.16])
		# keys.append([0.0367591])

		# names.append("RHipRoll")
		# times.append([3.16])
		# keys.append([0.0107584])

		# names.append("RKneePitch")
		# times.append([3.16])
		# keys.append([0.0839559])

		names.append("RShoulderPitch")
		times.append([1.48, 3.16])
		keys.append([0.18675, 1.56779])

		names.append("RShoulderRoll")
		times.append([1, 1.6, 3.16])
		keys.append([-0.119408, -0.0249289, -0.320648])

		names.append("RWristYaw")
		times.append([3.16])
		keys.append([0.967912])

		return [names, keys, times]

	@staticmethod
	def WearMotion():
		names = list()
		times = list()
		keys = list()

		names.append("LElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([-0.57981, -0.57981, -0.567538, -0.613558, -0.70253, -0.875872, -0.885076, -0.87894, -0.808376, -0.54146, -0.31136, -0.0950661, -0.082794, -0.082794, -0.082794])

		names.append("LElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([-1.22264, -1.22264, -1.22264, -1.24258, -1.24412, -1.23798, -1.1306, -0.92351, -0.773178, -0.771644, -0.771644, -0.77011, -0.773178, -0.773178, -0.773178])

		names.append("LHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164, 0.9164])

		names.append("LShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([1.52015, 1.52015, 1.55237, 1.37135, 0.934164, 0.743948, 0.774628, 0.961776, 1.12285, 1.27778, 1.33454, 1.42811, 1.47873, 1.47873, 1.47873])

		names.append("LShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.182504, 0.182504, 0.179436, 0.254602, 0.207048, 0.00455999, -0.297638, -0.314159, -0.314159, -0.216336, 0.05825, 0.262272, 0.161028, 0.154892, 0.154892])

		names.append("LWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.0889301, 0.0889301, 0.0889301, 0.0873961, -0.645856, -0.822266, -0.668866, -0.316046, -0.27923, -0.251618, -0.251618, -0.253152, -0.24855, -0.24855, -0.24855])

		names.append("RElbowRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.405018, 0.405018, 0.403484, 0.43263, 0.533874, 0.780848, 1.06004, 1.19963, 1.17355, 1.11373, 0.918908, 0.092082, 0.066004, 0.066004, 0.066004])

		names.append("RElbowYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([1.33761, 1.33761, 1.33761, 1.35908, 1.36982, 1.36982, 1.26091, 0.608956, 0.391128, 0.302156, 0.299088, 0.308292, 0.308292, 0.308292, 0.308292])

		names.append("RHand")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156, 0.9156])

		names.append("RShoulderPitch")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([1.48802, 1.48956, 1.48956, 1.40979, 0.790052, 0.58603, 0.446436, 0.45564, 0.529272, 0.760906, 1.24565, 1.30394, 1.32388, 1.32388, 1.32542])

		names.append("RShoulderRoll")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([-0.021518, -0.023052, -0.021518, -0.242414, -0.151908, 0.147222, 0.314159, 0.314159, 0.314159, 0.11194, -0.38661, -0.245482, -0.113558, -0.11049, -0.11049])

		names.append("RWristYaw")
		times.append([0.52, 1.04, 1.52, 2.04, 2.52, 3.04, 3.52, 4.04, 4.52, 5.04, 5.52, 6.04, 6.52, 7.04, 7.52])
		keys.append([0.194776, 0.194776, 0.194776, 0.197844, 0.638102, 0.73321, 0.731676, 0.73321, 0.73321, 0.73321, 0.759288, 0.845192, 0.87894, 0.87894, 0.87894])

		return [names, keys, times]

	@staticmethod
	def WorkoutMotion():
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([-0.116626, -0.116626, -0.115092, -0.115092, -0.11816, -0.115092, -0.11816, -0.115092, -0.11816, -0.115092, -0.11816, -0.115092, -0.601371, -0.535408, -0.536942, -0.544613, -0.437231, -0.270025, -0.222472, -0.230143])

		names.append("HeadYaw")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([-0.0107799, -0.0107799, -0.0138481, -0.00464392, 0.0413762, -0.00464392, 0.0413762, -0.00464392, 0.0413762, -0.00464392, 0.0413762, -0.00464392, -0.0261199, -0.0276539, -0.0276539, -0.0353239, -0.019984, -0.00617791, -0.019984, -0.0123138])

		# names.append("LAnklePitch")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([-1.18429, -1.18944, -1.18944, -1.18944, -1.18944, -1.18944, -1.18944, -1.18944, -1.18944, -1.18944, -1.18944, -1.18944, -1.18944, -1.18944, -1.18944, -1.01095, -1.17355, -1.18944, -0.895898, 0.0981341])

		# names.append("LAnkleRoll")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([0.075208, 0.066004, -0.05058, -0.049046, -0.049046, -0.049046, -0.049046, -0.049046, -0.049046, -0.049046, -0.049046, -0.049046, -0.00455999, 0.066004, 0.0429941, -0.05825, -0.061318, 0.066004, 0.067538, -0.115008])

		names.append("LElbowRoll")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([-0.361981, -0.0398422, -0.0398422, -0.0536479, -1.44345, -0.0536479, -1.44345, -0.0536479, -1.44345, -0.0536479, -1.44345, -0.0536479, -0.0352399, -0.0643861, -0.049046, -0.052114, -0.0429101, -0.0352399, -0.0444441, -0.389594])

		names.append("LElbowYaw")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([-1.25179, -0.834538, -0.668866, -0.668866, -0.983336, -0.668866, -0.983336, -0.668866, -0.983336, -0.668866, -0.983336, -0.668866, -1.22571, -1.23951, -1.23798, -1.23951, -1.23951, -1.23491, -1.21037, -1.21344])

		names.append("LHand")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([0.6256, 0.0140001, 0.0244, 0.0244, 0.064, 0.0244, 0.064, 0.0244, 0.064, 0.0244, 0.064, 0.0244, 0.0648, 0.0684, 0.0684, 0.0684, 0.0668, 0.0648, 0.0707999, 0.2976])

		# names.append("LHipPitch")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([-0.608956, -1.39283, -1.57384, -0.400331, -0.400331, -0.400331, -0.400331, -0.400331, -0.400331, -0.400331, -0.400331, -0.400331, -1.47106, -1.38516, -1.26704, -0.990921, -0.766959, -0.631966, -0.581345, 0.1335])

		# names.append("LHipRoll")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([-0.0536479, 0.460242, -0.0843279, -0.021434, -0.021434, -0.021434, -0.021434, -0.021434, -0.021434, -0.021434, -0.021434, -0.021434, -0.303691, -0.185572, -0.345107, -0.151824, 0.167248, -0.0413762, -0.0152981, 0.112024])

		# names.append("LHipYawPitch")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([-0.366584, -0.253067, -0.340507, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.493905, -0.673385, -0.739346, -0.601285, -0.530721, -0.473963, -0.481634, -0.1733])

		# names.append("LKneePitch")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([2.11255, 2.11228, 2.06319, 0.501576, 0.506179, 0.501576, 0.506179, 0.501576, 0.506179, 0.501576, 0.506179, 0.501576, 2.11228, 2.11255, 2.11255, 1.82849, 2.11255, 2.11075, 1.66895, -0.0874801])

		names.append("LShoulderPitch")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([1.65975, 0.562937, 0.167164, -0.0153821, 0.745483, -0.0153821, 0.745483, -0.0153821, 0.745483, -0.0153821, 0.745483, -0.0153821, 0.378855, 0.259204, 0.386526, 1.25017, 1.28238, 1.15353, 1.17193, 1.48947])

		names.append("LShoulderRoll")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([0.223922, 0.345107, 0.00762796, 0.0106959, 0.734743, 0.0106959, 0.734743, 0.0106959, 0.734743, 0.0106959, 0.734743, 0.0106959, 0.0152981, -0.0414601, -4.19617e-05, 0.289883, 0.268407, 0.260738, 0.225456, 0.128814])

		names.append("LWristYaw")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([0.0367741, 0.812978, 0.584411, 0.584411, 1.51862, 0.584411, 1.51862, 0.584411, 1.51862, 0.584411, 1.51862, 0.584411, 1.10904, 0.983252, 1.017, 0.960242, 0.94797, 0.710201, 0.693327, 0.147222])

		# names.append("RAnklePitch")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([-1.1863, -1.07836, -1.1863, -1.1863, -1.18574, -1.1863, -1.18574, -1.1863, -1.18574, -1.1863, -1.18574, -1.1863, -1.1863, -0.228525, 0.713353, 0.823801, -0.506179, -1.18421, -0.776162, 0.10282])

		# names.append("RAnkleRoll")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([-0.0367741, 0.142704, -0.0444441, 0.0291878, 0.0291878, 0.0291878, 0.0291878, 0.0291878, 0.0291878, 0.0291878, 0.0291878, 0.0291878, 0.00464392, 0.207132, 0.093616, -0.115008, 0.231675, -0.0137641, 0.0614019, 0.07214])

		names.append("RElbowRoll")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([0.27923, 0.297638, 0.204064, 0.231675, 1.35763, 0.231675, 1.35763, 0.231675, 1.35763, 0.231675, 1.35763, 0.231675, 0.038392, 0.0583338, 0.0567998, 0.06447, 0.0598679, 0.0349066, 0.0429941, 0.411154])

		names.append("RElbowYaw")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([1.18267, 1.18114, 1.15659, 1.21182, 0.990921, 1.21182, 0.990921, 1.21182, 0.990921, 1.21182, 0.990921, 1.21182, 1.15813, 1.18574, 1.18574, 1.18114, 1.17807, 1.18881, 1.17654, 1.16887])

		names.append("RHand")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([0.7316, 0.7316, 0.2236, 0.224, 0.1612, 0.224, 0.1612, 0.224, 0.1612, 0.224, 0.1612, 0.224, 0.1528, 0.1572, 0.1572, 0.1572, 0.1556, 0.1528, 0.1572, 0.306])

		# names.append("RHipPitch")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([-0.602905, -0.472515, -1.57699, -0.403483, -0.40962, -0.403483, -0.40962, -0.403483, -0.40962, -0.403483, -0.40962, -0.403483, -1.49723, -1.65369, -1.63989, -1.26559, -1.24718, -0.658129, -0.619779, 0.133416])

		# names.append("RHipRoll")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([-0.0106959, 0.366667, 0.312978, -0.136484, -0.136484, -0.136484, -0.136484, -0.136484, -0.136484, -0.136484, -0.136484, -0.136484, 0.265424, 0.280764, 0.29457, 0.288435, -0.216252, -0.0413762, -0.021434, -0.061318])

		# names.append("RHipYawPitch")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([-0.366584, -0.253067, -0.340507, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.493905, -0.673385, -0.739346, -0.601285, -0.530721, -0.473963, -0.481634, -0.1733])

		# names.append("RKneePitch")
		# times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		# keys.append([2.11255, 1.2073, 2.06481, 0.513931, 0.520068, 0.513931, 0.520068, 0.513931, 0.520068, 0.513931, 0.520068, 0.513931, 2.11255, 1.6, 0.598302, 0.2102, 1.97891, 2.11255, 1.61995, -0.0889301])

		names.append("RShoulderPitch")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([1.61995, 1.61688, 0.319114, 0.0414601, 0.605971, 0.0414601, 0.605971, 0.0414601, 0.605971, 0.0414601, 0.605971, 0.0414601, 0.365133, 1.29627, 1.29934, 1.30087, 1.30701, 1.1398, 1.17202, 1.47728])

		names.append("RShoulderRoll")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([-0.188724, -0.182588, 0.022968, 0.022968, -0.70108, 0.022968, -0.70108, 0.022968, -0.70108, 0.022968, -0.70108, 0.022968, 0.0152981, -0.377407, -0.397349, -0.343659, -0.296104, -0.204064, -0.181053, -0.101286])

		names.append("RWristYaw")
		times.append([1.68, 3.16, 4.32, 5.96, 6.8, 7.56, 8.24, 9, 9.8, 10.56, 11.4, 12.16, 13.68, 14.68, 15.68, 16.68, 17.68, 18.68, 19.76, 21.4])
		keys.append([0.10427, 0.10427, -1.1352, -1.13367, -1.06617, -1.13367, -1.06617, -1.13367, -1.06617, -1.13367, -1.06617, -1.13367, -1.13827, -1.14441, -1.14441, -1.13827, -1.12293, -0.857548, -0.840674, 0.0720561])

		return [names, keys, times]