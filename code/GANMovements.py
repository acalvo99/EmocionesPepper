from keras.models import load_model
import numpy as np
import pickle

class RunGANMovement:
	'''This class is used for generating random beat movements in Pepper robot

		Methods
		-------

		on_text_done()
			Function to call when all the text ends. Set the robot posture to initial.
		
		loadModels(epoch, um)
			Load the models to generate new movements
		
		runMovement(names, t_interval, movement_object)
			Given a set of parameters, runs or stores parameters needed by angleInterpolation function

		generateGANMovements(epo, tim, text, um, duration)
			Generates beat gestures for a given text

		emptyKeysAndTimes()
			Empty the keys and times lists
	'''
	def __init__(self, n_joints, global_gest, models_path, simulation, time_interval):
		
		self.n_joints = n_joints
		# self.count = count
		self.global_gest = global_gest
		self.models_path = models_path
		self.simulation = simulation
		self.time_interval = time_interval
		self.gen = None

		

		# Initialize times and keys with names length
		self.names = ["HeadYaw", "HeadPitch", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand", "HipRoll", "HipPitch", "KneePitch"]
		self.times = [[] for _ in self.names]
		self.keys = [[] for _ in self.names]
		self.old_last_keys = [[] for _ in self.names]
		self.p = 1.0

		# Add initial posture
		initialposture = self.global_gest.getMotion("InitPosture17")
		initialposture[1] = [float(p[0]) for p in initialposture[1]]
		self.runMovement(initialposture[0], time_interval, [initialposture[1]])
		
	def setProportion(self, p): 
		''' Set the value of the proportion 

		Parameters 
		----------
		p : float
			Value of the proportion
		'''
		self.p = p
		
	def loadModels(self, epoch, um):
		'''
		Load the models to generate new movements
		Parameters
		----------
		epoch : int
			Number of epochs of the model
		um : int
			Unit of Movement. Number of poses in a movement in the model

		Returns
		-------
		tuple
			A tuple with the generator and discriminator models
		'''
		generatorLoad = load_model(self.models_path + 'gan_generator_epoch_%d.h5' % epoch)
		discriminatorLoad = load_model(self.models_path + 'gan_discriminator_epoch_%d.h5' % epoch)
		return generatorLoad, discriminatorLoad

	def loadGenModel(self, epoch):
		self.gen = load_model(self.models_path + 'gan_generator_epoch_%d.h5' % epoch)

	def runMovement(self, names, t_interval, movement_object):
		'''Given the joint names, time interval and joints angles, saves joints names, times and angles in a proper way to later call naoqi's AngleInterpolation method
		Parameters
		----------
		names : list 
			Joint names
		t_interval : float
			Time between poses
		movement_object : list
			List of lists, containing in each list every joint value in names in the same order.
		'''

		# Add keys and times to class variables
		for i, name in enumerate(names):
			index = self.names.index(name)
			for j, movement in enumerate(movement_object):
				self.keys[index].append(float(movement[i]))
				if not self.times[index]:
					self.times[index].append((j+1)*t_interval*self.p)
				else:
					# Incremental time, taking into account previous times
					self.times[index].append(self.times[index][-1] + t_interval*self.p)

			# Last value of a joint is saved in case there is not information about that joint in future movements. First time this function is called, movement_object
			# must cointain all 17 joint values
			self.old_last_keys[index] = movement[i]

		# If there is some empty key value, replace with previous movement last value
		# print("keys before: ", self.keys)
		for i, key in enumerate(self.keys):
			# Check empty list
			if not key:
				self.keys[i].append(self.old_last_keys[i])
				self.times[i].append(t_interval*self.p)
	
	def generateGANMovements(self, tim, um, duration):
		'''Generates beat gestures for a given text
		Parameters
		----------
		epo : int
			An integer value to look for a model with that number of epochs
		tim: float
			Time interval
		um : int
			Unit of Movement of the model. Number of poses in one movement
		duration : float
			Duration in seconds of the sentence
		'''
		# Calculate time interval according to the sentimen mapping sentiment compound to interval
		time_interval = tim
		# self.count = self.count + 1
		rows,cols = um,14
		tempo = duration
		n_movements = int(round(tempo/(time_interval*rows)))

		# if self.count == 1:
		noise = np.random.uniform(-1,1,size=[n_movements, 100])
		generated_movements = self.gen.predict(noise)
		# Check if the length of movement is more than 0 -> resolve problem when the phrase is short
		if(len(generated_movements)>0): 
			_,c1 = generated_movements.shape
			generated_movements = np.reshape(generated_movements,(n_movements,(c1/cols),cols))
			filehandler = open(self.models_path + "pickle_min_maxScaler", 'r')
			input_minmax_scaler = pickle.load(filehandler)
			# Run every movement by UM
			for movement in generated_movements:
				names = ["HeadYaw", "HeadPitch", "RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw", "RHand", "LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw", "LHand"]
				self.runMovement(names, tim, input_minmax_scaler.inverse_transform(movement))

		return self.names, self.keys, self.times
		
	def emptyKeysAndTimes(self):
		'''
		Empty the times and keys lists
		'''
		self.times = [[] for _ in self.names]
		self.keys = [[] for _ in self.names]