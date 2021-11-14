#imports
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import scipy
import pandas as pd
import seaborn as sns
from tensorflow.keras.layers import Dense, Flatten, LSTM, Dropout
import tensorflow as tf
import math
import ast
import random
import matplotlib

#datasheet class for loading data through objects
class DataSheet(object):
    
    #constructor
    def __init__(self, file_name):
        self.df = pd.DataFrame(pd.read_csv(str(file_name)))
        
    #getter method - return entire csv file as a dataframe object
    def get_df(self): return self.df
    
    #setter method - kill old file and replace with new file for df
    
    #getter method - csv by parts
    def get_df_by_parts(self, row=None, col=None): #2 parameters - row and column for indexing
        if (row): 
            if (col):
                return float(self.df.iloc[row, col]) #column with row
            else:
                return list(self.df.iloc[row, :]) #column without row
        else:
            if (col):
                return list(self.df.iloc[:, col]) #row without column
            else:
                return None #null values for row and column
            
    #getter method - time (some bug in pd dosent register time vals properly, idk why)
    def get_times(self, name="DATE_TIME"):
        return list(self.df[name])
            
    #getter method - retrieve column names
    def get_column_names(self):
        return [str(col) for col in self.df.columns]

def times_to_num(times):
    return [time_to_num(time) for time in times] 

def time_to_num(time):
    time = list(time)
    nums = [str(j) for j in range(0, 9)]
    for character in time:
        if (character not in nums): time[time.index(character)] = ""
    return int("".join(time))
        
            
