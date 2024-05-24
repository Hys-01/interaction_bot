from api_retrieval import HuggingFaceAPIClient
import os

HF_api_key = os.getenv('HF_API_KEY')
HF_model = "microsoft/DialoGPT-medium"
HF_Client = HuggingFaceAPIClient(HF_api_key, HF_model)

# plans to use a loop, plans to print out JUST the value from each [{'generated_text': '.response.'}]

print("Press 0 to exit")
user_input = input(">> User: ")

while user_input!="0":
    r = HF_Client.ask_server(user_input)
    print(">> bot: " + r[0].get('generated_text'))


    user_input = input(">> User: ")


