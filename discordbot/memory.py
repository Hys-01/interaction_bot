# for multiple users we want individual memory for each
from model import generator
from transformers import Conversation
from collections import defaultdict

Conversation()
conversation_history = defaultdict(Conversation())
# conversation objects are prebuilt input/output history storage object


