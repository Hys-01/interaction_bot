from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer, TextStreamer
import torch

model_name = "NousResearch/Hermes-2-Pro-Llama-3-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    # torch.float16 and load_in_8bit both meant to save memory in exchange for precision downgrade
    torch_dtype=torch.float16, 
    load_in_8bit=True) 

streamer = TextStreamer(tokenizer)
generator = pipeline(
    "conversational", 
    model=model, 
    tokenizer=tokenizer, 
    streamer=streamer)  


