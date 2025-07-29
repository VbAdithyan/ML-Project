import pandas as pd
import numpy as np

# Load the dataset 
df = pd.read_csv('cardio_train.csv', sep=';')  

#Drop unnecessary columns
df.drop(columns=['id'], inplace=True)

#Convert age from days to years
df['age'] = (df['age'] / 365).astype(int)

#Remove duplicate records
df.drop_duplicates(inplace=True)

#Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

#Check the shape after preprocessing
print("Dataset shape after cleaning:", df.shape)


print("\nData Types:\n")
print(df.dtypes)

#Display first few rows
print("\nFirst 5 Rows:\n")
print(df.head())
