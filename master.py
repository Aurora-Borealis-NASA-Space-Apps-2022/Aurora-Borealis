# %%
# ombining CSV files BW[nT] & B[nT] to a single CSV file
# %%
# importing the necessary modules
import csv
import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
# merge the two files together BW[nT] & B[nT]
# create a list of all the CSV files in the current working directory
os.chdir('C:\\Users\\Muhammed Inaamullah\\Desktop\\Aurora-Borealis\\combined_files')
csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]
print(csv_files)

# %%
# the main dataframe
df = pd.DataFrame()
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# %%
# copying the data from CSV files to a single CSV file
location = 'C:\\Users\\Muhammed Inaamullah\\Desktop\\Aurora-Borealis\\combined_files\\*.csv'
all_files = glob.glob(location)
for file in all_files:
    df1 = pd.read_csv(file, on_bad_lines='skip', low_memory=False)
    df = pd.concat([df, df1], axis=0, ignore_index=True)
    df.to_csv('C:\\Users\\Muhammed Inaamullah\\Desktop\\Aurora-Borealis\\combined_files\\all_BW[nT]_B[nT].csv', mode='a', header=False, index=False)

# %%
print(df)

# %%
# creating a simple Neural Network using tensorflow
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

# %%
training_data = df.sample(frac=0.8, random_state=0)
testing_data = df.drop(training_data.index)

# %%
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(training_data.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])

# %%
model.compile(loss='mean_absolute_error',
                optimizer=tf.keras.optimizers.Adam(0.001))

# %%
# training the model
history = model.fit( training_data, epochs=1000, verbose=0, validation_split=0.2)

# %%
# plotting the loss
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()

# %%
# plotting the data
def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Error [BW[nT]]')
    plt.legend()
    plt.grid(True)


# %%
# plotting the data of the combined CSV file
df.plot(x='Time', y='BW[nT]', kind='line', figsize=(20, 10), color='red')
df.plot(x='Time', y='B[nT]', kind='line', figsize=(20, 10), color='blue')
plt.legend
plt.savefig('C:\\Users\\Muhammed Inaamullah\\Desktop\\Aurora-Borealis\\combined_files\\all_BW[nT]_B[nT].png')
plt.title('BW[nT] & B[nT]')
plt.xlabel('Time')
plt.ylabel('BW[nT] & B[nT]')
plt.show()

# %%
