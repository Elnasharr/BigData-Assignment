# Base image
FROM python:3.11-slim

# Install Python packages
RUN pip install --no-cache-dir \
    pandas numpy matplotlib seaborn scikit-learn scipy requests

# Create working directory
RUN mkdir -p /app/pipeline/

# Copy all project scripts into container (we’ll add them next steps)
COPY . /app/pipeline/

# Set working directory
WORKDIR /app/pipeline/

# Start interactive bash when the container runs
CMD ["/bin/bash"]
