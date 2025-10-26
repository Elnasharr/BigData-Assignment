#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Input dataset path (argument)
DATASET_PATH="$1"

# Check if dataset path is provided
if [ -z "$DATASET_PATH" ]; then
  echo "Usage: bash summary.sh <dataset.csv>"
  exit 1
fi

echo "=== Starting Big Data Pipeline ==="

# Step 1: Run the Docker container
# echo "[0/4] Starting Docker container..."
# docker run --rm --name assi1 -v "${PWD}:/app/pipeline" customer-analytics:latest &
# Wait for a moment to allow the container to start
# sleep 2

# Step 2: Run the data ingestion pipeline
echo "[1/3] Running ingest.py..."
# Create results folder on host if it doesn't exist
mkdir -p results/
python ingest.py "$DATASET_PATH"

echo "=== Pipeline completed successfully! ==="

CONTAINER_ID=$(docker ps -q --filter "name=assi1")

# Step 3: Copy results from container to host
# echo "[2/3] Copying generated results..."
# Adjust container and host paths if needed

# if [ -z "$CONTAINER_ID" ]; then
#   echo "No running container found for image 'customer-analytics'."
#   echo "Please make sure the container is running."
#   exit 1
# fi

#Copy files to host and remove from container (using absolute paths)
# docker cp "${CONTAINER_ID}:/app/pipeline/data_raw.csv" "./results/" 
# docker exec "${CONTAINER_ID}" rm -f "/app/pipeline/data_raw.csv" || true

# docker cp "${CONTAINER_ID}:/app/pipeline/data_preprocessed.csv" "./results/" 
# docker exec "${CONTAINER_ID}" rm -f "/app/pipeline/data_preprocessed.csv" || true

# docker cp "${CONTAINER_ID}:/app/pipeline/summary_plot.png" "./results/" 
# docker exec "${CONTAINER_ID}" rm -f "/app/pipeline/summary_plot.png" || true

# docker cp "${CONTAINER_ID}:/app/pipeline/clusters.txt" "./results/" 
# docker exec "${CONTAINER_ID}" rm -f "/app/pipeline/clusters.txt" || true

# docker cp "${CONTAINER_ID}:/app/pipeline/insight1.txt" "./results/" 
# docker exec "${CONTAINER_ID}" rm -f "/app/pipeline/insight1.txt" || true

# docker cp "${CONTAINER_ID}:/app/pipeline/insight2.txt" "./results/" 
# docker exec "${CONTAINER_ID}" rm -f "/app/pipeline/insight2.txt" || true

# docker cp "${CONTAINER_ID}:/app/pipeline/insight3.txt" "./results/" 
# docker exec "${CONTAINER_ID}" rm -f "/app/pipeline/insight3.txt" || true

# echo "[2/3] Files copied successfully!"

# Step 4: Stop and remove container
echo "[3/3] Stopping container..."
docker stop "$CONTAINER_ID" >/dev/null

echo "Container stopped."
echo "Container removed."

echo "=== All done! Results are saved in results/ ==="


