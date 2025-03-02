'''
HELPER FUNCTIONS FOR DISCORDBOT 
'''

# for multiple users we want individual memory for each
from transformers import Conversation
from collections import defaultdict

Conversation()
conversation_history = defaultdict(Conversation)
# conversation objects are prebuilt input/output history storage object

def get_conversation(user_id):
    return conversation_history[user_id]

def update_conversation(user_id, context: Conversation):
    
    conversation_history[user_id] = context

    if len(conversation_history.past_user_inputs)>25:
        conversation_history = conversation_history.past_user_inputs.pop(0)
        conversation_history = conversation_history.generated_responses.pop(0)

