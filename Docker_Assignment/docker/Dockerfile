# Step 1: Use an official Python runtime as a parent image
# 'slim' variants are smaller and great for standard applications
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt .

# Step 4: Install the specified packages
# --no-cache-dir keeps the image size small and clean
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your local code into the container
COPY . .

# Step 6: Define the command to run your app
CMD ["python", "main.py"]