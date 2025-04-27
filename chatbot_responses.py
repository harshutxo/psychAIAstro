import requests
import os

def get_response_from_huggingface(user_input):
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

    payload = {
        "inputs": user_input,
        "parameters": {
            "max_length": 150,
        },
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return "I apologize, but I'm having trouble right now."

    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"].strip()
    else:
        raise Exception(f"Hugging Face API error: {response.status_code} - {response.text}")

