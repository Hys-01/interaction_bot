from dotenv import load_dotenv
import os
import discord
from memory import * # memory helper funcs
from model import generator
import asyncio

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
        history.add_user_input(user_input, overwrite=True)  # getting some overwrite error with user input so set True

        # console check with stringmatch
        if user_input.lower() == "testing":
            await message.reply("confirmed")
            return 

        # generate bot response via AI model
        # BRAIN THINKING USING MEMORY
        try:
            loop = asyncio.get_event_loop()

            response = await loop.run_in_executor(
                None,
                lambda: generator(history)
            ) 
            botreply = response.generated_responses[-1]
        except Exception as e:
            print("Error", e)
            botreply = "RESPONSE iSSuE"

        # UPDATE NOTEBOOK
        update_conversation(user_id, history)

        # reply to my message with its llm generated response
        await message.reply(botreply)


client.run(os.getenv('DISCORD_TOKEN'))