import numpy as np
import pandas as pd
import subprocess
import sys

df = pd.read_csv('results/data_preprocessed.csv')

corr = df.corr(numeric_only=True)
corr_with_perf = corr['Performance_Bin'].sort_values(ascending=False)
print(corr_with_perf)

# df.groupby('Performance_Bin')[['Previous Scores', 'Hours Studied', 'Sleep Hours','Sample Question Papers Practiced','Extracurricular Activities_Yes']].mean()

with open("results/insight1.txt", "w") as file:
    file.write("It is clear that if a student has good previous score he will perform good again")

with open("results/insight2.txt", "w") as file:
    file.write("studying more hours is linked to better performance")

with open("results/insight3.txt", "w") as file:
    file.write("While sample questions and sleep affect less than the 2 above they still have a positive direct correlation")

try:
    print(f"[analytics] Chaining -> visualize.py data_preprocessed.csv")
    subprocess.run([sys.executable, "visualize.py", "data_preprocessed.csv"], check=True)
except Exception as e:
    print(f"[analytics] WARNING: Failed to run visualize.py: {e}")