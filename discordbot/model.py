from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer, TextStreamer
import torch

model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    # torch.float16 and load_in_8bit both meant to save memory in exchange for precision downgrade
    torch_dtype=torch.float16, 
    load_in_8bit=True,
    device_map="auto") 

streamer = TextStreamer(tokenizer)
generator = pipeline(
    "conversational", 
    model=model, 
    tokenizer=tokenizer, 
    #streamer=streamer
    device_map="auto"
    )  


