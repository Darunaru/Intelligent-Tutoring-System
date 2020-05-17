import tensorflow as tf
from tensorflow import *
import pandas as pd
from sklearn.model_selection import train_test_split

census = pd.read_csv("dataset.csv")
#print(census.head())
x_data = census.drop('RESULT',axis=1)
y_labels = census['RESULT']
X_train, X_test, y_train, y_test = train_test_split(x_data,y_labels,test_size=0.3,random_state=101)
