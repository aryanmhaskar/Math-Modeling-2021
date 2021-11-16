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
model.add(LSTM(100, input_shape=(None, seq_size)))
model.add(Dense(500))
model.add(Dense(250))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(25))
model.add(Dense(5))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(learning_rate=0.1, beta_1=0.)), verbose=1, mode='auto', restore_best_weights=True)
model.summary()
