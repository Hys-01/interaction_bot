import timeit
import torch

import asyncio
from transformers import pipeline, Conversation, AutoModelForSeq2SeqLM, AutoTokenizer
import torch
print(torch.cuda.is_available())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(torch.cuda.current_device()))

model_name = "facebook/blenderbot-1B-distill"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name,
        torch_dtype=torch.float16, load_in_8bit=True)


# Initialize the pipeline
generator = pipeline("conversational", model=model, tokenizer=tokenizer)

# Asynchronous function to generate response
async def generate_response_async(input_text):
    convo = Conversation(input_text)
    response = await asyncio.to_thread(generator, convo)
    return response.generated_responses[-1]

# Main function to test the chatbot
async def main():
    s = timeit.default_timer()
    response = await generate_response_async("Hi, how are you?")
    print(timeit.default_timer()-s)
    print(response)

# Run the main function
asyncio.run(main())
