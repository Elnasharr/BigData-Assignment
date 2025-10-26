import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import subprocess
import sys

df = pd.read_csv('results/data_preprocessed.csv')

plt.scatter(df['Previous Scores'],df['Hours Studied'],c=df['Performance_Bin'],cmap='viridis')
plt.xlabel('Previous Scores')
plt.ylabel('Hours Studied')
plt.title('Scatter Plot of Previous Scores vs Hours Studied')
plt.colorbar(label='Performance_Bin')
plt.savefig('results/summary_plot.png', bbox_inches='tight')
# plt.show()

try:
    print(f"[visualize] Chaining -> cluster.py data_preprocessed.csv")
    subprocess.run([sys.executable, "cluster.py", "data_preprocessed.csv"], check=True)
except Exception as e:
    print(f"[visualize] WARNING: Failed to run cluster.py: {e}")
