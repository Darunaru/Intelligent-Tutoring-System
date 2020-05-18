import tensorflow as tf
from tensorflow import *
import pandas as pd
from sklearn.model_selection import train_test_split

census = pd.read_csv("dataset.csv")
#print(census.head())
x_data = census.drop('RESULT',axis=1)
y_labels = census['RESULT']
X_train, X_test, y_train, y_test = train_test_split(x_data,y_labels,test_size=0.3,random_state=101)

attentive = tf.feature_column.categorical_column_with_vocabulary_list("ATTENTIVE", ["yes", "no"])
embedded_attentive = tf.feature_column.embedding_column(attentive, dimension=2)
nlp = tf.feature_column.numeric_column('NLP')
session_time = tf.feature_column.numeric_column('SESSION_TIME')
