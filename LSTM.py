import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import math

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM, Flatten
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.layers import ConvLSTM2D


#declare model in seq framerork
model = Sequential()
model.add(LSTM(50, input_shape=(None, sequence_size)))
model.add(Dense(50, activation="sigmoid"))
model.add(Dense(25, activation="sigmoid"))
model.add(Dense(5, activation="sigmoid"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(learning_rate=0.1, beta_1=0.)), verbose=1, mode='auto', restore_best_weights=True)
model.summary()
