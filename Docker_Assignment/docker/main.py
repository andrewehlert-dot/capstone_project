import requests
import numpy as np

print("Hello from inside the Docker container!")
print(f"Numpy version: {np.__version__}")

# Quick test of the requests library
response = requests.get("https://api.github.com")
print(f"GitHub API Status: {response.status_code}")