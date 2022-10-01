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
