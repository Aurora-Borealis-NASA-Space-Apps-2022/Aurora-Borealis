# %%
# write a code that automates the process of copying multiple CSV files and 
# writing them to a single CSV file
# for Wind mission magnetic field dataset (BW[nT]) - solar-wind-ion

# %%
# importing the necessary modules
import csv
import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%
# create a list of all the CSV files in the current working directory
os.chdir('C:\\Users\\Muhammed Inaamullah\\Desktop\\Aurora-Borealis\\2021\\solar-wind-ions')
csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]
print(csv_files)

# %%
# the main dataframe
df = pd.DataFrame()
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# %%
# copying the data from CSV files to a single CSV file
location = 'C:\\Users\\Muhammed Inaamullah\\Desktop\\Aurora-Borealis\\2021\\solar-wind-ions\\*.csv'
all_files = glob.glob(location)
for file in all_files:
    df1 = pd.read_csv(file, on_bad_lines='skip', low_memory=False)
    df = pd.concat([df, df1], axis=0, ignore_index=True)
    df.to_csv('C:\\Users\\Muhammed Inaamullah\\Desktop\\Aurora-Borealis\\combined_files\\all_BW[nT].csv', mode='a', header=False, index=False)

# %%
print(df)

