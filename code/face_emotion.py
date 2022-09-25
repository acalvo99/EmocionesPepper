import numpy as np
from pathlib import Path
import argparse
from pathlib import Path 
import pickle
import cv2
from time import sleep
import os
import pandas as pd

import torch
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.data.sampler import WeightedRandomSampler
from torchvision import transforms 

from emonet.models import EmoNet
#from emonet.data import AffectNet
# from emonet.data.affecnet import MyAffectNet
from emonet.data_augmentation import DataAugmentor
# from emonet.metrics import CCC, PCC, RMSE, SAGR, ACC
# from emonet.evaluation import evaluate, evaluate_flip

torch.backends.cudnn.benchmark =  True

# Parameters of the experiments
n_expression = 8
batch_size = 64
n_workers = 8 #16
device = 'cuda:0'
image_size = 256
#subset = 'val'  #'test'

exp_names = ['neutral', 'happy', 'sad', 'surprised', 'fear', 'disgust', 'anger', 'calm', 'none']



def predict_emotion(dataframe,index):
    # Create the data loaders
    transform_image = transforms.Compose([transforms.ToTensor()])
    transform_image_shape = DataAugmentor(image_size, image_size)


    # Loading the model 
    state_dict_path ='/home/bee/TFM-MAL/pepper_expression/code/pretrained/emonet_8.pth'

    #print(f'Loading the model from {state_dict_path}.')
    state_dict = torch.load(str(state_dict_path), map_location=torch.device("cuda", 0)) #'cpu')
    # state_dict = torch.load(str(state_dict_path), map_location='cpu')
    state_dict = {k.replace('module.',''):v for k,v in state_dict.items()}
    
    #net = EmoNet() # n_expression=n_expression).to(device)
    net = EmoNet(n_expression=n_expression)
    
    #print("NET type:", type(net))
    net.load_state_dict(state_dict, strict=False)
    net.eval()

    for indice_fila, fila in dataframe.iterrows():
        if indice_fila==index:
            filename = fila[1]
            #print(filename)

    using_webcam = not os.path.exists(filename)
    vid = cv2.VideoCapture(int(filename) if using_webcam else filename)
    length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    #print("LENGTH: ", length)
    assert vid.isOpened()
    #if using_webcam:
        #print(f'Webcam #{int(filename)} opened.')
    #else:
        #print(f'Input video "{filename}" opened.')

    # Load the cascade
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    torch.set_grad_enabled(False)
    frame_count = 0
    expr_list = []
    val_list = []
    arou_list = []
    while frame_count<length-1:
        frame_count += 1
        #print ("FRame count: ", frame_count)
        ret, frame = vid.read()
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #cv2.imshow("orig", frame)
        # Detect faces
        faces = faceCascade.detectMultiScale(cv2.cvtColor(im, cv2.COLOR_RGB2GRAY), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        maxValueFace = 0
        x_max = y_max = h_max = w_max = -1
        crop_img = im
        for i, (x, y, w, h) in enumerate(faces):
            if w*h > maxValueFace:
                x_max = x
                y_max = y
                h_max = h
                w_max = w
                maxValueFace = w*h
        # bounding_box = [landmarks.min(axis=0)[0], landmarks.min(axis=0)[1],
        #                 landmarks.max(axis=0)[0], landmarks.max(axis=0)[1]]
        bounding_box = [x_max, y_max, x_max+w_max, y_max+h_max]
        iimage, landmarks_new = transform_image_shape(im, bb=bounding_box)
        
        cv2.rectangle(frame, (x_max, y_max), (x_max+w_max, y_max+h_max), (255, 0, 0), 2)
        if maxValueFace > 0:
            # if self.transform_image is not None: transform to torch tensor
            image = transform_image(iimage)
            #with torch.no_grad():
            out = net(image[None, ...])
        
            expr = out['expression']
            nexpr = np.argmax(expr.numpy())

            val = out['valence'].item()

            ar = out['arousal'].item()
            predicted_exp = exp_names[nexpr]
           
            expr_list.append(predicted_exp)
            val_list.append(val)
            arou_list.append(ar)
        
            prediction = predicted_exp + " val={:.2f}".format(val) +" ar={:.2f}".format(ar)
            cv2.putText(frame, prediction, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2)
            
        cv2.imshow('original', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #sleep(1.0)
        
    vid.release()
    cv2.destroyAllWindows()



    #Predicted emotion
    num_calm = expr_list.count('calm')
    #print("Calm count:",num_calm)
    num_neutral = expr_list.count('neutral')
    #print("Neutral count:",num_neutral)
    num_happy = expr_list.count('happy')
    #print("Happy count:",num_happy)
    num_sad = expr_list.count('sad')
    #print("Sad count:",num_sad)
    num_anger = expr_list.count('anger')
    #print("Anger count:",num_anger)
    num_surprise = expr_list.count('surprised')
    #print("Surprise count:",num_surprise)
    num_disgust = expr_list.count('disgust')
    #print("Disgust count:",num_disgust)
    num_fear = expr_list.count('fear')
    #print("Fear count:",num_fear)

    list_emotions = ['calm','neutral','happy','sad','anger','surprised','disgust','fear']
    #print(list_emotions)
    list = [num_calm,num_neutral,num_happy,num_sad,num_anger,num_surprise,num_disgust,num_fear]
    #print(list)

    predicted_emotion = list_emotions[list.index(max(list))]

    #Predicted valence and arousal
    """
    list_val = []
    list_ar = []
    
    for x in list_emotions:
        if list[list_emotions.index(x)]!=0:
            print(list[list_emotions.index(x)])
            expr_list = np.array(expr_list)
            result = np.where(expr_list == x)
            sum_val = 0
            sum_ar = 0

            for el in result[0]:
                    sum_val += val_list[el]
                    sum_ar += arou_list[el]
                    

            predicted_val = sum_val/list[list_emotions.index(x)]
            list_val.append(predicted_val)
            predicted_ar = sum_ar/list[list_emotions.index(x)]
            list_ar.append(predicted_ar)

    print(list_val)
    print(list_ar)
    """

    sum_val = 0
    sum_ar = 0

    expr_list = np.array(expr_list)
    result = np.where(expr_list == predicted_emotion)

    for elem in result[0]:

        sum_val += val_list[elem]
        sum_ar += arou_list[elem]

    predicted_val = sum_val/max(list)
    predicted_ar = sum_ar/max(list)
    #print(predicted_emotion)
    #print(expr_list)
    #print(val_list)
    #print(arou_list)

    return predicted_emotion,predicted_val,predicted_ar


    
    
if __name__ == "__main__":
    filename = '/home/bee/TFM-MAL/pepper_expression/emotions_data.csv'
    dataframe = pd.read_csv(filename)
    index = 47
    predicted_exp,valence, arousal = predict_emotion(dataframe,index)
    print("Emotion:", predicted_exp)
    print("Valence:", valence)
    print("Arousal:", arousal)

    
