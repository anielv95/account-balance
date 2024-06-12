import os
import pandas as pd
import functions as f
import requests


files = os.listdir("data/")
results = {}

df = pd.read_csv("data/" + files[0]).to_json(orient="records")

account, email = f.get_email(files[0])

customer = {"account": account, "email": email, "df": df}

url = "http://localhost:3002/processing"

response = requests.post(url, json=customer, timeout=30).json()
print(response)
