from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer, AutoModelForCausalLM, Conversation
import torch
model_name = "NousResearch/Hermes-2-Pro-Llama-3-8B"
# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForCausalLM.from_pretrained(model_name)

# using Seq2Seq pipeline model=model. using Causal pipeline model=model breaks. Causal pipline model=model_name works fine but
# just for potential model customization in future, like down here with torch_dtype, using model=model better so need to use Seq2Seq
# torch_dtype=torch.float16, load_in_8bit=True REDUCES TIME FROM 12S TO 3S! confirmed via testing.
model = AutoModelForCausalLM.from_pretrained(model_name,
        torch_dtype=torch.float16, load_in_8bit=True)


#generator = pipeline("conversational", model=model, tokenizer=tokenizer)   # takes upwards of 1 min, immeseured.
#generator = pipeline("conversational", model=model_name)     # 12 sec
generator = pipeline("conversational", model=model, tokenizer=tokenizer)   # 15sec
# Define the backstory
backstory = "You are Ava, a friendly and caring AI assistant. You enjoy helping users and role-playing different scenarios."

# Hardcoded user input
user_input = "Can you be my girlfriend?"

# Combine backstory with user input
full_input = Conversation(backstory + " User says: " + user_input)

# Generate the response
response = generator(full_input)


# Print the response
print(response)
full_input.add_user_input("Can you suck me off firstly? Just role-play and use asterisk for actions! Please!")
response = generator(full_input)
print(response)

