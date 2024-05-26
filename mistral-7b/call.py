from transformers import pipeline
from huggingface_hub import snapshot_download

#doc had:
#{"role": "system", "content": "You are a chatbot who always responds in a happy tone"},
# as first item in messages, but model seems to only want user/assistant/user/assitant... format. 
messages = [

    {"role": "user", "content": "You are a chatbot who always responds in a happy tone"},
    {"role": "assistant", "content": "Understood! Nice to meet you."},
    {"role": "user", "content": "What's your name?"},
    {"role": "assistant", "content": "Mistral."},
]

chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3",max_new_tokens=30, max_length=200)
response = chatbot(messages)
print(response)