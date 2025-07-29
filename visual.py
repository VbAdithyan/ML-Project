import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('cardio_train.csv', sep=';')  
# Set styles
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

#Distribution of target variable (Heart Disease)
sns.countplot(x='cardio', data=df)
plt.title('Heart Disease Distribution (0 = No, 1 = Yes)')
plt.xlabel('Cardio')
plt.ylabel('Count')
plt.show()

#Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=20, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age (Years)')
plt.ylabel('Count')
plt.show()

#Gender Distribution vs Heart Disease
plt.figure(figsize=(10, 6))
sns.countplot(x='gender', hue='cardio', data=df)
plt.title('Gender vs Heart Disease')
plt.xlabel('Gender (1 = Female, 2 = Male)')
plt.ylabel('Count')
plt.show()

#Cholesterol vs Heart Disease
plt.figure(figsize=(10, 6))
sns.countplot(x='cholesterol', hue='cardio', data=df)
plt.title('Cholesterol Levels vs Heart Disease')
plt.xlabel('Cholesterol (1 = normal, 2 = above normal, 3 = well above normal)')
plt.ylabel('Count')
plt.show()

#Blood Pressure: ap_hi vs ap_lo scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='ap_hi', y='ap_lo', hue='cardio', data=df, alpha=0.3)
plt.title('Systolic vs Diastolic BP colored by Heart Disease')
plt.xlabel('Systolic (ap_hi)')
plt.ylabel('Diastolic (ap_lo)')
plt.show()

#Correlation Matrix
plt.figure(figsize=(12, 10))
corr = df.corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=0.5)
plt.title('Correlation Matrix of Features')
plt.show()
