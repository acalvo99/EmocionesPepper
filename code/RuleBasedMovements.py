import nltk
# nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import global_gestures as gg
import random
import math
import bisect

class RuleBasedKeywordsMovement():
	'''
	Class to insert new rule based movements into an existing movement

	Methods
	-------
	setKeywords(keywords)
		Set the keywords to find in the movement
	
	findMovement(keyword)
		Finds the corresponding movement of a keyword
	
	modifyMovement()
		Modify an existing movement to add a rule based movement
	'''
	def __init__(self):
		# self.keyword_movement = {}
		# self.all_keywords = self.keyword_movement.keys()
		# self.used_movements = {}
		self.global_gest = gg.GlobalGestures()
		self.initialposture = self.global_gest.getMotion("InitPosture17")
		self.proportion = 0.0

	def __calculateInsertIndices(self, start_time, end_time, duration, time_interval, rb_movement_times):

		try:
			# Get key movement min time value
			rb_movement_start_time = float(min([time[0] for time in rb_movement_times]))
			# rb_movement_end_time = float(max([max(time) for time in rb_movement_times]))

			# Get word times in speech and modify start and end times according to the compound score
			word_start_time = float(start_time) * self.proportion
			word_end_time = float(end_time) * self.proportion
			
			# If movements fits in text duration
			if rb_movement_start_time + word_end_time < duration:
				# Find movement insert positions:
				word_start_pose = int(word_start_time / time_interval)
				word_end_pose = int(math.ceil(word_end_time / time_interval)) 
			else:
				# Check if can be fitted moving few positions backwards
				# Get the excedent time
				extra_time = duration - rb_movement_start_time - word_end_time
				# time_before = word_start_time
				if extra_time < word_start_time:
					# Move n indexes start and end movement 
					word_start_time = word_start_time - extra_time
					word_end_time = word_end_time - extra_time
					word_start_pose = int(word_start_time / time_interval)
					word_end_pose = int(math.ceil(word_end_time / time_interval))

			return (word_start_pose, word_end_pose)

		except AssertionError:	
			print("Movement longer than sentence")
			return(None, None, None, None)

	def setProportion(self, p):
		self.proportion = p

	def setKeywords(self, keywords):
		self.keywords = keywords


	# def findMovement(self, keyword):
	# 	'''
	# 	Finds the corresponding movement to a keyword.
	# 	Parameters
	# 	----------
	# 	keyword : string
	# 		The keyword to find in movements database
	# 	Returns
	# 	-------
	# 	movement : list
	# 		List of lists containing the joint names, keys and times of the movement if exists, else -1
	# 	'''
	# 	print("Keyword: %s" % keyword)
	# 	movement = self.keyword_movement.get(keyword, -1)

	# 	print("ALL MOVEMENTS %s", self.keyword_movement.keys())

	# 	print("MOVEMENT: %d", movement)
	# 	assert(movement != -1), 'Movement for keyword "%s" does not exist.' % keyword
	# 	return random.choice(movement)()

	def modifyMovement(self, gan_movement, rb_movement, first_index, last_index, text_duration, movement_duration, time_interval):
		'''
		Modify an existing movement to add a rule based movement
		Parameters
		----------
		rb_movement : list
			List of lists, containing joint, keys and times of the rule based movement.  
		first_index : int
			Rule based movement initial index in movement object
		last_index : int
			Rule based movement final index in movement object
		text_duration : float
			Time in seconds of the sentence
		'''

		gan_names, gan_keys, gan_times = gan_movement

		# Prepare new keys and times to insert
		new_keys = [[] for _ in gan_names]
		new_times = [[] for _ in gan_times]
		assert len(new_keys) == len(new_times)

		if first_index == last_index:
			last_index = last_index + 1

		if first_index == 0: 
			added_time = 0
		else:
			# TODO. Error thrown when first_index-1 is higher than the length of every list in runGAN.times
			insert_index_times = [time[first_index-1] for time in gan_times if len(time) > (first_index-1)]
			if not insert_index_times:
				insert_index_times = [time[-1] for time in gan_times if len(time)]
			# If all times length is lower than first_index-1, take the max time value as added_time
			added_time = max(insert_index_times)
		# Modify the first index so the new movement can be reproduced from beginning to end
		while movement_duration + added_time > text_duration:
			first_index = first_index -1
			last_index = last_index -1
			if first_index == 0:
				added_time = 0.0
			else:
				insert_index_times = [time[first_index-1] for time in gan_times if len(time) > (first_index-1)]
				if not insert_index_times:
					insert_index_times = [time[-1] for time in gan_times if len(time)]
				# If all times length is lower than first_index-1, take the max time value as added_time
				added_time = max(insert_index_times)

		for i, (keys, times) in enumerate(zip(rb_movement[1], rb_movement[2])):
			new_keys[i].extend(keys)
			
			if first_index != 0:
				new_times[i].extend(map(lambda x : x + added_time, times))
			else:
				new_times[i].extend(times)


		# Find max time value in new_times and 
		new_times_max_value = max([max(x) for x in new_times if x])
		
		# Insert new values i the corresponding position
		for name, key, time in zip(rb_movement[0], new_keys, new_times):
			i = gan_names.index(name)
			if last_index < len(gan_times[i]):
				added_time_after = new_times_max_value + time_interval - gan_times[i][first_index]
				gan_keys[i] = gan_keys[i][:first_index] + key + gan_keys[i][first_index:]
				gan_times[i] = gan_times[i][:first_index] + time + map(lambda x : x + added_time_after, gan_times[i][first_index:])
			else:
				gan_keys[i] = gan_keys[i][:first_index] + key 
				gan_times[i] = gan_times[i][:first_index] + time

			# Get the index of the first value grater than speech duration
			first_duration_exceed_index = bisect.bisect_left(gan_times[i], text_duration)
			
			# Remove movevements longer than speech duration
			if not gan_times[i]:
				gan_times[i] = [text_duration]
				index = self.initialposture[0].index(gan_names[i])
				gan_keys[i] = self.initialposture[1][index]

			elif gan_times[i][0] > text_duration or not gan_times[i]:
				gan_times[i] = gan_times[i][:1]
				gan_keys[i] = gan_keys[i][:1]
			
			else:
				gan_times[i] = gan_times[i][:first_duration_exceed_index]
				gan_keys[i] = gan_keys[i][:first_duration_exceed_index]

		return gan_names, gan_keys, gan_times

	def getWordPosition(self, key_movement, keyword_start_time, text_duration, time_interval):
		try:
			# Find matching movement for keyword
			# key_movement = self.findMovement(keyword[0])
			
			# Modify key movement duration according to emotion proportion
			key_movement[2] = [map(lambda x: x * (2.0-float(self.proportion)), time) for time in key_movement[2]]
			assert(key_movement !=- 1)

			# Get key movement min time value
			key_movement_start_time = float(min([time[0] for time in key_movement[2]]))
			key_movement_end_time = float(max([max(time) for time in key_movement[2]]))
			key_movement_duration = key_movement_end_time - key_movement_start_time
			# Get word times in speech and modify start and end times according to the compound score
			word_start_time = float(keyword_start_time) * self.proportion
			# word_end_time = float(keyword[2]) * self.proportion
			
			# If there is more than one occurrence, choose a random occurrence of that word
			# As there ir always a start and end point, the number of occurrences is the length / 2
			# keyword structure example: "keyword", start time occurrence 1, end time occurrence 1, ... start time occurrence n, end time occurrence n 
			# occurrences = len(keyword[1:])/2
			
			# if occurrences > 1:
			# 	occurrence_index = random.randrange(0, len(keyword[1:]), 2)
			# 	word_start_time = float(keyword[occurrence_index+1])
			# 	word_end_time = float(keyword[occurrence_index+2])




			# If movements fits in text duration
			if key_movement_start_time + word_end_time < text_duration:
				# Find movement insert positions:
				word_start_pose = int(word_start_time / time_interval)
				word_end_pose = int(math.ceil(word_end_time / time_interval)) 
			else:
				# Check if can be fitted moving few positions backwards
				# Get the excedent time
				extra_time = text_duration - key_movement_start_time - word_end_time
				# time_before = word_start_time
				if extra_time < word_start_time:
					# Move n indexes start and end movement 
					word_start_time = word_start_time - extra_time
					word_end_time = word_end_time - extra_time
					word_start_pose = int(word_start_time / time_interval)
					word_end_pose = int(math.ceil(word_end_time / time_interval))

			return (key_movement, word_start_pose, word_end_pose, key_movement_duration)

		except AssertionError:	
			print("Movement longer than sentence")
			return(None, None, None, None)


	def insertMovement(self, gan_movement, rb_movement, word_start_time, word_end_time, speech_duration, time_interval):
		'''
		Modify an existing movement to add a rule based movement
		Parameters
		----------
		rb_movement : list
			List of lists, containing joint, keys and times of the rule based movement.  
		first_index : int
			Rule based movement initial index in movement object
		last_index : int
			Rule based movement final index in movement object
		speech_duration : float
			Time in seconds of the sentence
		'''


		gan_names, gan_keys, gan_times = gan_movement
		rb_names, rb_keys, rb_times = rb_movement

		movement_duration = max([t[-1] for t in rb_times])

		if movement_duration > speech_duration:
			print("Rule based movement can't be inserted, it is too long for current sentence. ")
			return gan_names, gan_keys, gan_times


		# keyword_insert_pos = self.getWordPosition(rb_movement, speech_duration, time_interval)

		# Calculate insert indices
		first_index, last_index = self.__calculateInsertIndices(word_start_time, word_end_time, speech_duration, time_interval, rb_times)


		# Prepare new keys and times to insert
		new_keys = [[] for _ in gan_names]
		new_times = [[] for _ in gan_times]
		assert len(new_keys) == len(new_times)

		# First and last index can't be the same
		if first_index == last_index:
			last_index = last_index + 1

		if first_index == 0: 
			added_time = 0
		else:
			insert_index_times = [time[first_index-1] for time in gan_times if len(time) > (first_index-1)]
			if not insert_index_times:
				insert_index_times = [time[-1] for time in gan_times if len(time)]
			# If all times length is lower than first_index-1, take the max time value as added_time
			added_time = max(insert_index_times)
		# Modify the first index so the new movement can be reproduced from beginning to end
		while movement_duration + added_time > speech_duration:
			first_index = first_index -1
			last_index = last_index -1
			if first_index == 0:
				added_time = 0.0
			else:
				insert_index_times = [time[first_index-1] for time in gan_times if len(time) > (first_index-1)]
				if not insert_index_times:
					insert_index_times = [time[-1] for time in gan_times if len(time)]
				# If all times length is lower than first_index-1, take the max time value as added_time
				added_time = max(insert_index_times)

		for i, (keys, times) in enumerate(zip(rb_keys, rb_times)):
			new_keys[i].extend(keys)
			
			if first_index != 0:
				new_times[i].extend(map(lambda x : x + added_time, times))
			else:
				new_times[i].extend(times)


		# Find max time value in new_times and 
		new_times_max_value = max([max(x) for x in new_times if x])
		
		# Insert new values i the corresponding position
		for name, key, time in zip(rb_names, new_keys, new_times):
			i = gan_names.index(name)
			if last_index < len(gan_times[i]):
				added_time_after = new_times_max_value + time_interval - gan_times[i][first_index]
				gan_keys[i] = gan_keys[i][:first_index] + key + gan_keys[i][first_index:]
				gan_times[i] = gan_times[i][:first_index] + time + map(lambda x : x + added_time_after, gan_times[i][first_index:])
			else:
				gan_keys[i] = gan_keys[i][:first_index] + key 
				gan_times[i] = gan_times[i][:first_index] + time

			# Get the index of the first value grater than speech duration
			first_duration_exceed_index = bisect.bisect_left(gan_times[i], speech_duration)
			
			# Remove movevements longer than speech duration
			if not gan_times[i]:
				gan_times[i] = [speech_duration]
				index = self.initialposture[0].index(gan_names[i])
				gan_keys[i] = self.initialposture[1][index]

			elif gan_times[i][0] > speech_duration or not gan_times[i]:
				gan_times[i] = gan_times[i][:1]
				gan_keys[i] = gan_keys[i][:1]
			
			else:
				gan_times[i] = gan_times[i][:first_duration_exceed_index]
				gan_keys[i] = gan_keys[i][:first_duration_exceed_index]

		return gan_names, gan_keys, gan_times

class Lemmatizer():
	def __init__(self):
		self.lemmatizer = WordNetLemmatizer()

	def lemmatize(self, word, pos="n"):
		'''
		word : str
			The input word to lemmatize.
		pos : str
			The Part Of Speech tag. Valid options are `"n"` for nouns,
			`"v"` for verbs, `"a"` for adjectives, `"r"` for adverbs and `"s"`
			for satellite adjectives.
		'''
		return self.lemmatizer.lemmatize(word, pos=pos)

	
	def nltk_tag_to_wordnet_tag(self, nltk_tag):
		if nltk_tag.startswith('J'):
			return wordnet.ADJ
		elif nltk_tag.startswith('V'):
			return wordnet.VERB
		elif nltk_tag.startswith('N'):
			return wordnet.NOUN
		elif nltk_tag.startswith('R'):
			return wordnet.ADV
		else:          
			return None
	
	def lemmatize_sentence(self, sentence):
		# tokenize the sentence and find the POS tag for each token
		nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))  
		# tuple of (token, wordnet_tag)
		wordnet_tagged = map(lambda x: (x[0], self.nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
		lemmatized_sentence = []
		for word, tag in wordnet_tagged:
			if tag is None:
				# if there is no available tag, append the token as is
				lemmatized_sentence.append(word)
			else:        
				# else use the tag to lemmatize the token
				lemmatized_sentence.append(self.lemmatizer.lemmatize(word, tag))
		return " ".join(lemmatized_sentence)

# l = Lemmatizer()
# lemmatized_sentence = l.lemmatize_sentence("Hello, my name is John, i am very happy to see you")
# lemmatized_sentence_2 = l.lemmatize_sentence("Hello, seeing you has been not as good as knowing you")

# print(lemmatized_sentence)
# print(lemmatized_sentence_2)