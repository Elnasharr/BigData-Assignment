import subprocess
import sys
import os
import pandas as pd

def main():
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <dataset_path>")
        sys.exit(1)

    in_path = sys.argv[1]
    out_path = "data_raw.csv"

    #check if in_path exists or not 
    if not os.path.exists(in_path):
        print(f"[ingest] ERROR: Input file not found: {in_path}")
        sys.exit(2)

    #load the csv. file (that what we expected to be loaded)
    try:
        df = pd.read_csv(in_path)
    except Exception as e:
        print(f"[ingest] ERROR: Failed to read CSV: {e}")
        sys.exit(3)

    #save a standardized copy
    try:
        df.to_csv("results/data_raw.csv", index=False)
    except Exception as e:
        print(f"[ingest] ERROR: Failed to write {out_path}: {e}")
        sys.exit(4)

    print(f"[ingest] OK -> Saved copy to {out_path}")

    try:
        print(f"[ingest] Chaining -> preprocess.py data_raw.csv")
        subprocess.run([sys.executable, "preprocess.py", "data_raw.csv"], check=True)
    except Exception as e:
        print(f"[ingest] WARNING: Failed to run preprocess.py: {e}")

if __name__ == "__main__":
    main()