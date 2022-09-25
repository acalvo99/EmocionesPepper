from ast import Global
import os
import math
import subprocess

import soundfile
import librosa
import numpy as np
import pickle
from convert_wavs import convert_audio


AVAILABLE_EMOTIONS = {
    "neutral",
    "calm",
    "happy",
    "sad",
    "angry",
    "fear",
    "disgust",
    "ps", # pleasant surprised
    "boredom"
}


def get_label(audio_config):
    """Returns label corresponding to which features are to be extracted
        e.g:
    audio_config = {'mfcc': True, 'chroma': True, 'contrast': False, 'tonnetz': False, 'mel': False}
    get_label(audio_config): 'mfcc-chroma'
    """
    features = ["mfcc", "chroma", "mel", "contrast", "tonnetz"]
    label = ""
    for feature in features:
        if audio_config[feature]:
            label += "{%s}-" % feature
    return label.rstrip("-")


def get_dropout_str(dropout, n_layers=3):
    if isinstance(dropout, list):
        return "_".join([ str(d) for d in dropout])
    elif isinstance(dropout, float):
        return "_".join([ str(dropout) for i in range(n_layers) ])


def get_first_letters(emotions):
    return "".join(sorted([ e[0].upper() for e in emotions ]))


def extract_feature(file_name, **kwargs):
    """
    Extract feature from audio file `file_name`
        Features supported:
            - MFCC (mfcc)
            - Chroma (chroma)
            - MEL Spectrogram Frequency (mel)
            - Contrast (contrast)
            - Tonnetz (tonnetz)
        e.g:
        `features = extract_feature(path, mel=True, mfcc=True)`
    """
    mfcc = kwargs.get("mfcc")
    chroma = kwargs.get("chroma")
    mel = kwargs.get("mel")
    contrast = kwargs.get("contrast")
    tonnetz = kwargs.get("tonnetz")
    try:
        with soundfile.SoundFile(file_name) as sound_file:
            pass
    except RuntimeError:
        # not properly formated, convert to 16000 sample rate & mono channel using ffmpeg
        # get the basename
        basename = os.path.basename(file_name)
        dirname  = os.path.dirname(file_name)
        name, ext = os.path.splitext(basename)
        new_basename = "{%s}_c.wav" % name
        new_filename = os.path.join(dirname, new_basename)
        v = convert_audio(file_name, new_filename)
        if v:
            raise NotImplementedError("Converting the audio files failed, make sure `ffmpeg` is installed in your machine and added to PATH.")
    else:
        new_filename = file_name
    with soundfile.SoundFile(new_filename) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        if chroma or contrast:
            stft = np.abs(librosa.stft(X))
        result = np.array([])
        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result = np.hstack((result, mfccs))
        if chroma:
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result = np.hstack((result, chroma))
        if mel:
            mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result = np.hstack((result, mel))
        if contrast:
            contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
            result = np.hstack((result, contrast))
        if tonnetz:
            tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
            result = np.hstack((result, tonnetz))
    return result


def get_best_estimators(classification):
    """
    Loads the estimators that are pickled in `grid` folder
    Note that if you want to use different or more estimators,
    you can fine tune the parameters in `grid_search.py` script
    and run it again ( may take hours )
    """
    if classification:
        return pickle.load(open("/home/bee/TFM-MAL/pepper_expression/code/grid/best_classifiers.pickle", "rb"))
    else:
        return pickle.load(open("/home/bee/TFM-MAL/pepper_expression/code/grid/best_regressors.pickle", "rb"))


def get_audio_config(features_list):
    """
    Converts a list of features into a dictionary understandable by
    `data_extractor.AudioExtractor` class
    """
    audio_config = {'mfcc': False, 'chroma': False, 'mel': False, 'contrast': False, 'tonnetz': False}
    for feature in features_list:
        if feature not in audio_config:
            raise TypeError("Feature passed: {%s} is not recognized." % feature)
        audio_config[feature] = True
    return audio_config
    

def rangeConversion(first_old, last_old, first_new, last_new, value):
	'''
	Converts a given value from a range of values to a new one

	Parameters
	----------

	first_old : float
		The first value of the old range
	last_old : float
		The last value of the old range
	first_new : float
		The first value of the new range
	last_new : float
		The last value of the new range
	value : float
		The value to be converted

	Returns
	-------
	new value : float
		The old value converted to the new range value
	'''
	old_range = (last_old - first_old)
	new_range = (last_new - first_new)
	new_value = (((value - first_old) * new_range) / old_range) + first_new
	return new_value

def sigmoid_function(min_value, max_value, compound, k):
	'''
	Sigmoid function

	min_value : float
		The minimum value
	max_value : float
		The max value
	compound : float
		The compound score
	k : float
		The exponential value of the sigmoid function
	'''
	gap = max_value - min_value
	return (gap / (1.0 + math.exp(-k*compound))) + min_value

def sendFileToNao(nao_ip, orig_audio_path, dest_audio_path, file_name):
	'''
	Uplaodads a file from local to pepper

	Parameters
	----------

	nao_ip : str
		The ip address of nao

	orig_audio_path : str
		The path of the file to upload

	dest_audio_path : str
		The destination file path in pepper 

	filename : str
		The name of the file to upload
	
	'''
	try:
		with open(os.devnull, 'wb') as devnull:
			subprocess.check_call(['scripts/nao-ftp-put.sh', nao_ip, orig_audio_path, dest_audio_path, file_name], stdout=devnull, stderr=subprocess.STDOUT)
			
		
	except Exception as e:
		print(str(e))


# def exponential_porp(a, x, xmax, xmin):
# 	return a * (math.exp(x)) / (math.exp(xmax) - math.exp(xmin))

def exponential(t, x):
	return min(1.0, max(0, math.exp(t-x)))

def readcsv(filename):
	import csv
	story = []
	with open(filename) as f:
		reader = csv.reader(f, delimiter=";")
		for row in reader:
			story.append((row[0], row[1], row[2]))
	return story


def trimMovement(movement, text_duration):
	
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
	import bisect
	from Gestures import GlobalGestures
	# gan_names, gan_keys, gan_times = movement
	gg = GlobalGestures()
	initialposture = gg.getMotion("InitPosture17")

	new_gan_times = []
	new_gan_keys = []

	
	for gan_names, gan_keys, gan_times in zip(movement[0], movement[1], movement[2]):
	
		# Get the index of the first value grater than speech duration
		first_duration_exceed_index = bisect.bisect_left(gan_times, text_duration)

		# Remove movevements longer than speech duration
		if not gan_times:
			gan_times = [text_duration]
			index = initialposture[0].index(gan_names)
			gan_keys = initialposture[1][index]

		elif gan_times[0] > text_duration or not gan_times:
			gan_times = gan_times[:1]
			gan_keys = gan_keys[:1]

		else:
			gan_times = gan_times[:first_duration_exceed_index]
			gan_keys = gan_keys[:first_duration_exceed_index]

		new_gan_keys.append(gan_keys)
		new_gan_times.append(gan_times)

	return movement[0], new_gan_keys, new_gan_times
