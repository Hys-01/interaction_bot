from dotenv import load_dotenv
import os
import discord

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

@client.event
async def on_message(message):
    # on_message called when received a message


    # ignore user messages
    if message.author == client.user:
        return

    # basic rule-based example
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv("DC_TOKEN"))