#   https://discord.com/api/oauth2/authorize?client_id=1035734043511242822&permissions=8&scope=bot%20applications.commands
#   discord.py | python-dotenv | 
from email.mime import message
import discord as dc
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

load_dotenv()
intents = dc.Intents.all()
bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print('O bot está ON!'.format(bot))
    try:
        synced = await bot.tree.sync()
        print(f'sync {len(synced)} comandos')
    except Exception as ex:
        print(ex)

@bot.event
async def on_mesage(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('oi'):
        await message.channel.send('oi!')

    if message.content.startswith('stop'):
        await message.channel.send('bot desligando...')
        await bot.close()

@bot.tree.command(name='teste')
async def cmd(interaction: dc.Interaction):  
    await interaction.response.send_message(f'nossa {interaction.user.name}, mas que pau grande e esse?')

@bot.tree.command(name='off')
@commands.has_permissions(manage_roles=True, ban_members=True)
async def cmd(interaction: dc.Interaction):  
    await interaction.response.send_message('adeus...')
    await bot.close()

bot.run(os.getenv('TOKEN'))