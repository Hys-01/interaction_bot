from transformers import pipeline
from huggingface_hub import snapshot_download

#doc had:
#{"role": "system", "content": "You are a chatbot who always responds in a happy tone"},
# as first item in messages, but model seems to only want user/assistant/user/assitant... format. 
messages = [

    {"role": "user", "content": "Who are you?"},
    {"role": "assistant", "content": "I am Mistral!"},
    {"role": "user", "content": "Hi Mistral."},
    {"role": "assistant", "content": "Nice to meet you."},
]

chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3",max_new_tokens=50)
response = chatbot(messages)
print(response)