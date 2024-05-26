from transformers import pipeline

chatbot = pipeline("text-generation", model="distilgpt2", max_new_tokens=30)

# Example usage
messages = [
    "User: You are a chatbot who always responds in a happy tone.",
    "Assistant: Understood! Nice to meet you.",
]

response = chatbot(messages)
print(response)