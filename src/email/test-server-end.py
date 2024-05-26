import requests

customer = {'August': 35, 'September': 98, 'account': 'aab43a27-48b2-4249-954e-a2629220ff11', 'credit': 57.64, 'debit': -51.27, 'email': 'anielvillegas@gmail.com', 'total': -558.54}

url = "http://localhost:5000/send-email"

response = requests.post(url, json=customer, timeout=30).json()
print(response)
