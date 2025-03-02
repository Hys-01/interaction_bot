from dotenv import load_dotenv
import os
import discord
from memory import * # memory helper funcs
from model import generator

load_dotenv()

# intents bot persmissions
intents = discord.Intents.default()
intents.message_content = True

# client connection 
client = discord.Client(intents=intents)


@client.event  #callback event register
async def on_ready():
    # on_ready event is called when finish logging in 
    print(f'We have logged in as {client.user}')
    #status
    await client.change_presence(activity = discord.Game(name="online"))

@client.event
async def on_message(message):
    # on_message called when received a message


    # ignore bot's responses
    if message.author == client.user:
        return

    if client.user in message.mentions: # msg contains @bot

        user_id = str(message.author.id)
        # user's id
        # cleans removes the @mention from the msg
        user_input = message.content.replace(f"<@{client.user.id}>", "").strip()

        # MEMORY NOTEBOOK unique to each user_id
        # getting the history of user's interactions with bot
        history = get_conversation(user_id)
        # update history
        history.add_user_input(user_input)


        # generate bot response via AI model
        # BRAIN THINKING USING MEMORY
        try:
            response = generator(history)
            botreply = response.generated_response[-1]
        except Exception as e:
            print("Error", e)
            botreply = "error"

        # UPDATE NOTEBOOK
        update_conversation(user_id, history)

        # reply to my message with its llm generated response
        await message.reply(botreply)


client.run(os.getenv('DISCORD_TOKEN'))