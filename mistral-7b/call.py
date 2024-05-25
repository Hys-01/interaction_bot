from transformers import pipeline
from huggingface_hub import snapshot_download

messages = [
    {"role": "system", "content": "You are a chatbot who always responds in a happy tone"},
    {"role": "user", "content": "Who are you?"},
    {"role": "assistant", "content": "I am Mistral!"},
    {"role": "user", "content": "Hi Mistral."},
    {"role": "assistant", "content": "Nice to meet you."},
]
snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.3", allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"], local_dir=mistral_models_path)
chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")
response = chatbot(messages)
print(response)