import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
TOKEN= 'OTk4OTg1NTg3Nzc0MTk3ODIx.GErhNk.BY4bXU_jj8vzt_1dzae3qdHyBnxeAgDxfOxzvg'
ban_words = ['пиздец','блять','ахуеть','ахуел','ебали','пизда','хуйня','бля','Пиздец', 'нихуя', 'Блять','Ахуеть','Ахуел','Ебали','Пизда','Хуйня','Бля','Нихуя']

def simplify_word(word):
    last_letter = ''
    result = ''
    for letter in word:
        if letter != last_letter:
            last_letter = letter
            result += letter
    
    return result

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    msg_words = [simplify_word(word) for word in message.content.split()]

    for word in msg_words:
        if word in ban_words:
            try:
                await message.delete()
            except:
                print('Ошибка при удалении сообщения')
            await message.channel.send(f'{message.author.mention} **фуу...матершиник!:** *{word}*')

bot.run(TOKEN)