from transformers import pipeline
from huggingface_hub import snapshot_download
from timeit import default_timer as timer

#doc had:
#{"role": "system", "content": "You are a chatbot who always responds in a happy tone"},
# as first item in messages, but model seems to only want user/assistant/user/assitant... format. 
messages = [

    {"role": "user", "content": "You are a chatbot who always responds in a happy tone"},
    {"role": "assistant", "content": "Understood! Nice to meet you."},
]
start = timer() 
chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3",max_new_tokens=30)
end=timer()
response = chatbot(messages)
end2 = timer()

print(response)
print("pipeline time: " , (end-start)/60, " minutes")

print("overall time: " , (end2-start)/60, " minutes")