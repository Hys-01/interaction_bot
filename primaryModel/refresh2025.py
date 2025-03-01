from transformers import pipeline, Conversation, AutoModelForCausalLM, AutoTokenizer, AutoModelForSeq2SeqLM, TextStreamer
import torch
import gradio as gr

model_name = "NousResearch/Hermes-2-Pro-Llama-3-8B"

# trying to use GPU via CUDA since cpu performance is unable to handle 8b models
print(torch.cuda.is_available())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(torch.cuda.current_device()))

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name,
        torch_dtype=torch.float16, load_in_8bit=True) 
        # torch.float16 and load_in_8bit both meant to save memory in exchange for precision downgrade

# streaming setup
streamer = TextStreamer(tokenizer)


#pipeline(conv) built for convo history and input-output series. 
# autoModelforCausalLM is not built for conversational, so pass in a Conversation() object to it.
generator = pipeline("conversational", model=model, tokenizer=tokenizer, streamer=streamer)  
convo = Conversation("Hi, what's your name?")
print(generator(convo))

# user input app interface
# inputs and responses could be combined to form a 'memory' of sorts
# how to implement backstory/key memories? need to research
inputs = []
responses = []
def inputOutput(input, chat_history):
    global inputs, responses
    convo = Conversation(text=input, past_user_inputs=inputs, generated_responses=responses)
    response = generator(convo)

    response_text = response.generated_responses[-1]
    
    # UPDATE MEMORY
    #   WITHOUT APPENDING TO INPUT AND RESPONSES, IT CANNOT REMEMBER MY NAME
    #   AFTER APPENDING, IT DOES. CONFIRMED MEMORY IS FUNCTIONAL.
    inputs.append(input)
    responses.append(response_text)
    # FIN UPDATE MEMORY
    if len(inputs) > 25:
        inputs.pop(0)
        responses.pop(0)
        
    return response_text

demo = gr.ChatInterface(fn=inputOutput, title="Vanilla Chatbot", description="...") #, multimodel=True is not working???
demo.launch()
