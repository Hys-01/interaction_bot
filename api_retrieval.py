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

        format_payload = {"inputs": payload}


        response = requests.post(self.model_url, headers=headers, json=format_payload)  # 1 second tiemeout for TimeoutError
        response.raise_for_status()  # check for HTTPError
        # normal response is 200
        
        return response.json()
    
class OpenAIApiClient():
    def __init__(self):
        pass
    
    def ask_server(self, payload):
        pass


'''
very uncomfrotable to use, theres a timeout or http request error every second message. And messaeg quality is also... not the best compared to local demo.


'''
