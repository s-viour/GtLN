import os
import secrets
from discord.ext import commands


bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    bot.the_number = secrets.randbits(32)

@bot.event
async def on_message(message):
    if message.author.bot == True:
        return
    
    try:
        n = int(message.content)
        if n == bot.the_number:
            await message.reply('correct')
            await bot.close()
        else:
            await message.reply('incorrect')
    except ValueError:
        pass


if __name__ == '__main__':
    tk = os.getenv('GUESSLARGENUMBER_TOKEN')
    if tk:
        bot.run(tk)
    else:
        print('GUESSLARGENUMBER_TOKEN not set. quitting...')