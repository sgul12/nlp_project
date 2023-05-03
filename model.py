import requests

API_URL = "https://api-inference.huggingface.co/models/sgul12/gpt2-sonnet-generators"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()