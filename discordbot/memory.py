'''
HELPER FUNCTIONS FOR DISCORDBOT 
'''

# for multiple users we want individual memory for each
from transformers import Conversation
from collections import defaultdict


conversation_history = defaultdict(Conversation)
# conversation objects are prebuilt input/output history storage object

def get_conversation(user_id):
    return conversation_history[user_id]

def update_conversation(user_id, context: Conversation):
    #???????
    global conversation_history
    # Also, use the global keyword if you want to change a global variable inside a function. 
    # https://www.w3schools.com/python/python_variables_global.asp

    # global history update for this user
    conversation_history[user_id] = context

    # https://huggingface.co/transformers/v4.10.1/main_classes/pipelines.html
    if len(context.past_user_inputs)>25:
        context.past_user_inputs.pop(0)
        context.generated_responses.pop(0)

