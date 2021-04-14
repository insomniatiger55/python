# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06  09:38:35 2021

@author: jacob
"""
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

words=[]
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open('intents.json').read()
#intents = json.loads(data_file)
print('load success')
intents = json.loads(open('intents.json').read())
print(intents['intents'].keys())


