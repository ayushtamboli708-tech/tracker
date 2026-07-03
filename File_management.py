import numpy as np
import pandas as pd
import csv
try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

titles = df.columns.tolist()
print(titles)
lst = df['title'].tolist()
print(df['title'].head())
fil = df[df['title'].str.contains("Florida DJs May Face Felony for April Fools' W...", case=False, na=False)]
print(fil)