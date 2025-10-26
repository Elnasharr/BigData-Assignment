import numpy as np
import pandas as pd
import subprocess
import sys

df = pd.read_csv('results/data_raw.csv')

# df.head()
# df.shape

"""# **insuring No Duplicated values**"""

# df[df.duplicated()]
# df.duplicated().sum()

df = df.drop_duplicates()

# df[df.duplicated()]
# df.duplicated().sum()

# df.shape

"""# **Handling missing values**"""

# print("Number of missing values in each column:")
# print(df.isnull().sum())

"""# **Imputations**"""

mean_value = int(df['Performance Index'].mean())
df['Performance Index'].fillna(mean_value, inplace=True)

mean_value = int(df['Sample Question Papers Practiced'].mean())
df['Sample Question Papers Practiced'].fillna(mean_value, inplace=True)

mean_value = df['Sleep Hours'].mean()
df['Sleep Hours'].fillna(mean_value, inplace=True)

mean_value = df['Previous Scores'].mean()
df['Previous Scores'].fillna(mean_value, inplace=True)

mean_value = df['Hours Studied'].mean()
df['Hours Studied'].fillna(mean_value, inplace=True)

# print("Number of missing values in each column:")
# print(df.isnull().sum())

"""# **one-hot encoding and filling nulls with mode**"""

# df['Extracurricular Activities'].unique()

df['Extracurricular Activities'].replace({
    'yes': 'Yes',
    'no': 'No',
}, inplace=True)

# df['Extracurricular Activities'].unique()

mode_value = df['Extracurricular Activities'].mode()[0]
df['Extracurricular Activities'].fillna(mode_value, inplace=True)

# print("Number of missing values in each column:")
# print(df.isnull().sum())

df = pd.get_dummies(df, columns=['Extracurricular Activities'])
df = df.astype(int)

# df.head()

df['Performance_Bin'] = pd.qcut(df['Performance Index'], q=10, labels=False)

# df.head()

"""# **Dropping redundant features**"""

df = df.drop(columns=['Performance Index'])

# df

df.to_csv('results/data_preprocessed.csv', index=False)

try:
    print(f"[preprocess] Chaining -> analytics.py cleaned_data.csv")
    subprocess.run([sys.executable, "analytics.py", "cleaned_data.csv"], check=True)
except Exception as e:
    print(f"[preprocess] WARNING: Failed to run analytics.py: {e}")

