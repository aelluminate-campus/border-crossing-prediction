import warnings
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
sns.set_theme(style='whitegrid', font='serif')

DATASET_URL = "Border_Crossing_Entry_Data.csv"

data = pd.read_csv(DATASET_URL)

print("Initial Data Info:")
print(data.info())
print("\nMissing Values:\n", data.isnull().sum())

data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

if 'Point' in data.columns:
    data.drop(columns=['Point'], inplace=True)

data.drop_duplicates(inplace=True)
data.dropna(subset=['Port Name', 'State', 'Border'], inplace=True)
data.columns = data.columns.str.lower().str.replace(' ', '_')
data['value'] = pd.to_numeric(data['value'], errors='coerce')
data = data[data['value'] > 0]
data.reset_index(drop=True, inplace=True)
data = data.sort_values(by='port_name').reset_index(drop=True)

print("\nCleaned Data Info:")
print(data.info())
print(data.head(50))

data.to_csv("processed.csv", index=False)