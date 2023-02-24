import requests

question_data = []
count = 0

try:
    url = "https://opentdb.com/api.php"
    params = {
        'amount': 12,
        'type': 'boolean'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
except requests.RequestException:
    print(f'There was an error: {response.status_code}')

    # Parse response
try:
    data = response.json()
    for item in data["results"]:
        question = data["results"][count]["question"]
        answer = data["results"][count]["correct_answer"]
        count += 1
        question_data.append({"question":question, "correct_answer":answer})
except (KeyError, TypeError, ValueError):
    print("There was an error. Please rerun.")
