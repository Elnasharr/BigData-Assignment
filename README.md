# 🧠 Customer Analytics (CSCI461 – Assignment 1, Fall 2025)

A Dockerized end-to-end data pipeline for **Customer Analytics** — covering data ingestion, preprocessing, analytics, visualization, and clustering.  
All tasks are executed within a containerized environment for full reproducibility.

---

## 📁 Project Structure

```
customer-analytics/
├── Dockerfile
├── ingest.py
├── preprocess.py
├── analytics.py
├── visualize.py
├── cluster.py
├── summary.sh
├── Student_Performance.csv
└── results/
    ├── data_raw.csv
    ├── data_preprocessed.csv
    ├── summary_plot.png
    └── clusters.txt
```

---

## ⚙️ Prerequisites

- **Docker** installed and running
- **Git Bash** (on Windows) — required for running bash scripts  
- Sufficient disk space (~2GB)

---

## 🚀 How to Run

### 1️⃣ Build the Docker Image
```bash
docker build -t customer-analytics:latest .
```

### 2️⃣ Run the Container
```bash
docker run --rm --name assi1 -it -v "${PWD}:/app/pipeline" customer-analytics:latest
```

> `--rm`: Automatically removes the container after execution.  
> `-v "${PWD}:/app/pipeline"`: Mounts your current directory to `/app/pipeline` inside the container.

### 3️⃣ Execute the Full Pipeline
> ⚠️ Use **Git Bash** on Windows for this step.

```bash
bash summary.sh ./Student_Performance.csv
```

After completion, check your **results/** folder for all generated outputs.

---

## 🧭 Execution Flow (Based on `CSCI461_Assignment_1_Fall25.pdf`)

The project follows a modular and sequential flow as required in the assignment:

### 1. 🏗 Ingest
**File:** `ingest.py`  
**Purpose:** Load and validate input dataset.  
**Output:** `results/data_raw.csv`

### 2. 🧹 Preprocess
**File:** `preprocess.py`  
**Purpose:** Perform cleaning, encoding, scaling, dimensionality reduction, and discretization.  
**Output:** `results/data_preprocessed.csv`

### 3. 🧮 Analytics
**File:** `analytics.py`  
**Purpose:** Generate at least **three textual insights** based on the data.  
**Output:** `results/insight1.txt`, `results/insight2.txt`, `results/insight3.txt`

### 4. 📊 Visualization
**File:** `visualize.py`  
**Purpose:** Create at least one plot summarizing key findings (e.g., correlation heatmap, distribution plot).  
**Output:** `results/summary_plot.png`

### 5. 🔍 Clustering
**File:** `cluster.py`  
**Purpose:** Apply K-Means clustering and display cluster distribution.  
**Output:** `results/clusters.txt`

### 6. 📦 Summary & Cleanup
**File:** `summary.sh`  
**Purpose:**  
- Copy all generated `.csv`, `.txt`, and `.png` files from the container into `results/` on the host.  
- Stop and remove the container after completion.

---

## 📘 Manual Stage Execution (Optional)

If you wish to run each step manually inside the container:

```bash
# Inside the container terminal
python ingest.py ./Student_Performance.csv
python preprocess.py ./results/data_raw.csv
python analytics.py ./results/data_preprocessed.csv
python visualize.py ./results/data_preprocessed.csv
python cluster.py ./results/data_preprocessed.csv
```

---

## 🧩 Example Output Structure

```
results/
├── data_raw.csv
├── data_preprocessed.csv
├── insight1.txt
├── insight2.txt
├── insight3.txt
├── summary_plot.png
└── clusters.txt
```

---

## 🐛 Common Issues

| Issue | Cause | Fix |
|-------|--------|-----|
| `open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified` | Docker Desktop not running | Start Docker Desktop |
| `bash: command not found` | Running from PowerShell instead of Git Bash | Use Git Bash |
| `container not running` | Tried running `summary.sh` before container | Run `docker run` first |
| Volume path errors | Path formatting | Always use `-v "${PWD}:/app/pipeline"` |

---

## 🧮 Grading Checklist

- [x] Dockerfile with correct base image & dependencies  
- [x] `ingest.py` → data_raw.csv  
- [x] `preprocess.py` → data_preprocessed.csv  
- [x] `analytics.py` → 3 text insights  
- [x] `visualize.py` → at least one plot  
- [x] `cluster.py` → KMeans results  
- [x] `summary.sh` → copies results, stops & removes container  
- [x] `README.md` (this file) with commands & flow description

---

## 🏷 License

This project is for **CSCI461 – Big Data** coursework (Fall 2025).  
Use only for academic purposes.

---

**Author:** _Add your name(s)_  
**Instructor:** _Add professor’s name if required_
