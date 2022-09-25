import argparse
import re

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from code.AnnotatedStoryReader import AnnotatedStory
from code.AnnotatedStoryReader import AnnotatedKeyword


class SpeechRecognizer():
	
	'''
	By using IBM Watson services recognizes words in a speech. 

	Methods
	-------
	findWords(keywords, filename)
		Finds all keywords in keyword in the audio file filename
	'''
	def __init__(self):

		authenticator = IAMAuthenticator('xNAynn3fQKhLEdwFnDlVNHbqZnWbfraHiP6Rr3NqrcOE')
		self.speech_to_text = SpeechToTextV1(
		authenticator=authenticator
		)

		self.speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/55cd5f3d-2774-4e70-b6cd-c07696410191')
		self.output_dict = {}


	def findWords(self, keywords, storyname, i):
		'''
		Finds all keywords in keyword in the audio file filename

		Parameters
		----------
		keywords : list
			Listo containing all the keywords to find in the speech
		filename : 
			The filename of the audio file
		'''

		filename = "%s_%d.wav" % (storyname, i)
		speech_recognition_results = None
		# Call IBM Watson ASR
		if len(keywords):
			with open('Download_watson_info/audio/' + filename,'rb') as audio_file:
				speech_recognition_results = self.speech_to_text.recognize(
					audio=audio_file, 
					content_type='audio/wav', 
					keywords=keywords, 
					keywords_threshold=0.5
					).get_result()
		
		keywords = []
		if speech_recognition_results:
			# print(speech_recognition_results)
			for found_word in speech_recognition_results["results"][0]["keywords_result"]:
		
				for occurrence in speech_recognition_results["results"][0]["keywords_result"][str(found_word)]:
					keywords.append(AnnotatedKeyword(found_word, -1, occurrence["start_time"], occurrence["end_time"]))

			return keywords

		else:
			return []

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--story",type=str, default='ColorMonster', help="The name of the story to be processed")
	args = parser.parse_args()

	storyname = args.story

	asr = AnnotatedStory(storyname)
	# Get only the movement that matches two conditions: 1. It has been automatically detected and 2, it haves a corresponding movement. 
	annotated_keyword = asr.getAnnotatedKeywords()
	
	sr = SpeechRecognizer()
	keywords_dict = {}

	for i, sentence in enumerate(asr.sentences):
		words_in_sentence = [word for word in annotated_keyword if re.search(r'\b' + word.lower() + r'\b', sentence.text.lower()) and word in annotated_keyword]
		# print("Words to find: %s" % str(words_in_sentence))
		
		keywords_dict["sentence_%d" % i] = sr.findWords(words_in_sentence, storyname, i)

	asr.setKeywordsTimes(keywords_dict)

	asr.saveAsJSON()