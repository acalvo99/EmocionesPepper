from ast import Load
import yaml
from copy import deepcopy
import types


class Story:
	def __init__(self, storyname):
		self.__story = None
		
		self.__loadInfo(storyname)


	def __loadInfo(self, storyname):
		with open("story_info/%s_onomatopoeia_ssml.yml" % storyname) as f:
			# self.__story = yaml.load(f)
			# TODO. yaml loads the story as a dict, it doesn't recognize data types as they are write using python3. 
			self.__story = yaml.load(f, Loader=yaml.BaseLoader)
			print("Story: %s" % self.__story)
			

	def getStoryInfo(self):
		return self.__story

	def getTimesOrdered(self):
		'''
		Returns the start and end times of the keywords in the story in the same order they appear in the story.

		Returns
		-------
		A tuple of lists with start and end times (start_times, end_times)

		'''
		start_times = []
		end_times = []
		print("Story: ", self.__story)
		for i in range(len(self.__story)):
			# if self.__story["sentence_%d" % i]["keywords_in_sentence"]["start_times"]:
			# TODO: compare data type using other condition
			if type(self.__story["sentence_%d" % i]["keywords_in_sentence"]["start_times"]) != type(u''):

				keyword_start_times_ordered = deepcopy(self.__story["sentence_%d" % i]["keywords_in_sentence"]["start_times"])
				keyword_end_times_ordered = deepcopy(self.__story["sentence_%d" % i]["keywords_in_sentence"]["end_times"])
				
				print("Sentence %d" % i)
				print(type(keyword_start_times_ordered))
				print(keyword_start_times_ordered)
				keyword_start_times_ordered.sort()
				keyword_end_times_ordered.sort()
				
				start_times.extend(keyword_start_times_ordered)
				end_times.extend(keyword_end_times_ordered)


		
		return start_times, end_times

		

class SentenceInfo():
	def __init__(self, filename, duration):
		self.filename = filename
		self.duration = duration

class Keywords():
	def __init__(self, keywords, start_times, end_times):
		self.keywords = keywords
		self.start_times = start_times
		self.end_times = end_times

class Sentence():
	def __init__(self, sentence_info, keywords_in_sentence):
		self.sentence_info = sentence_info
		self.keywords_in_sentence = keywords_in_sentence	

# story = Story("ColorMonster")
# info = story.getStoryInfo()

# print("Dena", info)
# print("Sentence", info['sentence_8'])
# print("Filename", info['sentence_8'].sentence_info.filename)
# print("Duration", info['sentence_8'].sentence_info.duration)
# print("Keywords type", info['sentence_8'].keywords_in_sentence)
# print("Keywords", info['sentence_8'].keywords_in_sentence.keywords)
# print("Start times", info['sentence_8'].keywords_in_sentence.start_times)
# print("End times", info['sentence_8'].keywords_in_sentence.end_times)

