import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib import rcParams
from sklearn.cluster import KMeans

df = pd.read_csv('results/data_preprocessed.csv')

data = list(zip(df['Hours Studied'],df['Performance_Bin']))
k = KMeans(n_clusters=20)
k.fit(data)
label = k.predict(data)

u_labels = np.unique(label)
f = open("results/clusters.txt","w")
for i in u_labels:
  cur = df[label==i]
  print(f"class {i} has : {cur['Hours Studied'].count()} points")
  f.write(f"class {i} has : {cur['Hours Studied'].count()} points\n")
f.close()

print("Pipeline completed successfully!!")