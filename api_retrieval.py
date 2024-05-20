import requests

# prototyping

#requests.post()   # sends a post HTTP request to GET data WITH something
'''
we should be able to choose either openAI api or huggingface api, code shouldnt need to be refactored based on this

hmmm

'''
API_KEY = ""
#return = requests.post(url=API_KEY, )

class HuggingFaceAPIClient:
    def __init__(self, api_key, model):
        self.key = api_key
        self.model_url = model
    
    def ask_server():
        pass