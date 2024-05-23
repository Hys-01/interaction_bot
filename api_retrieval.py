import requests

import os 
from dotenv import load_dotenv
# prototyping

#requests.post()   # sends a post HTTP request to GET data WITH something
'''
we should be able to choose either openAI api or huggingface api, code shouldnt need to be refactored based on this

hmmm

'''
load_dotenv()


#return = requests.post(url=API_KEY, )

class HuggingFaceAPIClient:
    def __init__(self, api_key, model):
        self.key = api_key
        self.model_url = f"https://api-inference.huggingface.co/models/{model}"
    
    def ask_server(self, payload):
        headers = {"Authorization": f"Bearer {self.key}"}
        response = requests.post(self.model_url, headers=headers, json=payload)
        return response.json()
    
payload_1 = "Hello, World!"
HF_api_key = os.getenv('HF_API_KEY')
print(HF_api_key)
HF_model = "mistralai/Mixtral-8x7B-Instruct-v0.1"
HF_Client = HuggingFaceAPIClient(HF_api_key, HF_model)

print(HF_Client.ask_server(payload_1))