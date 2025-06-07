# extract_data.py
import requests
import pandas as pd
import json

# -- Step 1: Fetch from API
url = "https://api.thecatapi.com/v1/images/0XYvRd7oD"
headers = {"x-api-key": "YOUR_API_KEY"}  # optional if not required

response = requests.get(url, headers=headers)
data = response.json()

# -- Step 2: Convert to DataFrame
df = pd.DataFrame([data])
df.drop(columns=['breeds'], inplace=True)  # drop complex JSON columns

# -- Step 3: Save locally
df.to_csv("cat_data.csv", index=False)
print("✅ Data saved to cat_data.csv")





