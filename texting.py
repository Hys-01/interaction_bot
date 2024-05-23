from api_retrieval import HuggingFaceAPIClient
import os

HF_api_key = os.getenv('HF_API_KEY')
HF_model = "microsoft/DialoGPT-medium"
HF_Client = HuggingFaceAPIClient(HF_api_key, HF_model)

payload_1 = "Hi!"

r_1 = HF_Client.ask_server(payload_1)
print(r_1)