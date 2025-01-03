import requests

data_url = "https://opentdb.com/api.php?amount=10&type=boolean"
response = requests.get(data_url)
response.raise_for_status()

question_data = response.json()["results"]
