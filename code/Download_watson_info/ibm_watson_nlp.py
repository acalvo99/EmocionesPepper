import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, EmotionOptions

from code.RuleBasedMovements import Lemmatizer

class TextAnalyzer():
	'''
	Converts text to speech using IBM Watson services

	Methods
	-------

	getSpeech(data, filename)
			Given a string containing the text, it converts to speech and save in the file filename
	'''

	def __init__(self):
		# APIKEY unai.zabalac@ehu.eus
		
		authenticator = IAMAuthenticator('S5ry1uWyD1dt-Rlhx404-gJqf5gqyHOL58eFxezLRnLV')
		self.natural_language_understanding = NaturalLanguageUnderstandingV1(version='2022-04-07',authenticator=authenticator)

		self.natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/71eae341-1a3a-4c03-b10f-e0e90d671e2b')

	def analyzeText(self, text):
		'''
		Given a string containing SSML, it converts to speech and save in the file filename

		Parameters
		----------
		data : str
				A string containing the text
		filename : str
				Destination audio file name
		'''
		print("Sentence: %s" % sentence)
		# WARNING: Some voice parameter options are deprecated and will be removed on 31 March 2023
		response = self.natural_language_understanding.analyze(
			text=text,
			features=Features(
				keywords=KeywordsOptions(emotion=False, sentiment=False),
				emotion=EmotionOptions())).get_result()

		

		# print(json.dumps(response, indent=2))
		return response

	def saveAsJSON(self, data, filename, path="text/annotated_stories/"):

		with open(path+filename, "w+") as f:
			f.write(json.dumps(data))
		return


def findDominantEmotion(emotions):
	
	score = -1
	emotion = "neutral"
	for e, s in emotions["document"]["emotion"].items():
		if s > score:
			emotion = e
			score = s 
	return emotion, score

def adaptEmotionLabel(emotion):
	
	if emotion == "sadness": 
		return "SADNESS"
	if emotion == "joy": 
		return "HAPPINESS"
	if emotion == "fear": 
		return "FEAR"
	if emotion == "disgust": 
		return "DISGUST"
	if emotion == "anger": 
		return "ANGER"
	if emotion == "neutral": 
		return "NEUTRAL"

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("--story",type=str, default='ColorMonster', help="The name of the story to be processed")
	args = parser.parse_args()
	story = args.story


	storyname = args.story 

	with open("/home/bee/workspace_unai/NarRob/NarRob/narrob_annotate/src/main/resources/stories/%s.txt" % storyname) as f:
		sentences = f.read()

	sentences = sentences.split(".")

	# If the story ends with a dot the last element will be empty, so remove it .
	if not sentences[-1]:
		sentences = sentences[:-1]

	# Save keywords together with the story and get them
	
	lemmatizer = Lemmatizer()
	ta = TextAnalyzer()


	story_dict = {}
	story_dict["storypath"] = "text/annotated_stories/%s_annotated.json" % storyname
	story_dict["sentences"] = []

	for i, sentence in enumerate(sentences):

		sentence_dict = {"duration":0,
        				 "emotion_intensity":1,
        				 "emotion":"",
        				 "keywords":[],
        				 "text":sentence,
        				 "audio_filename": "%s_%d.wav" % (storyname, i)}

		# sentence = sentence.decode('UTF-8')
		print("Processing file %s, sentence %d..." % (storyname, i))
		# print("SSML Sentence: %s" % sentence)
		json_response = ta.analyzeText(sentence)


		emotions = json_response["emotion"]
		emotion, intensity = findDominantEmotion(emotions)

		emotion = adaptEmotionLabel(emotion)

		sentence_dict["emotion"] = emotion
		sentence_dict["emotion_intensity"] = intensity

		for keyword in json_response["keywords"]:
			word = keyword["text"]
			weight = keyword["relevance"]
			lemma = lemmatizer.lemmatize(word)
			keyword_dict = {"start_time":0,"end_time":0,"lemma":lemma,"weight":weight}
			sentence_dict["keywords"].append(keyword_dict)

		story_dict["sentences"].append(sentence_dict)


	ta.saveAsJSON(data=story_dict, filename="%s_annotated.json" % storyname)

	# print("Done")


