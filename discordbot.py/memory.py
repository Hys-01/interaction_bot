# for multiple users we want individual memory for each
from model import generator
from transformers import Conversation
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