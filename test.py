from transformers import pipeline, Conversation

# Initialize the conversational pipeline
generator = pipeline('conversational', model='microsoft/DialoGPT-medium')

# Create a conversation
convo = Conversation("Hi, what's your name?")
response = generator(convo)

# Print the updated conversation
print(response)


# copied from test.ipynb
