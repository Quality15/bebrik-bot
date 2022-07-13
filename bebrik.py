import discord
from discord.ext import commands
import random
import psutil
import platform
import sys
import time
import datetime

from cfg import *

client = commands.Bot(command_prefix=prefix)

client.remove_command('help')

@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('я вернулся'))

@client.event
async def on_message(message):
    channel = message.channel
    random_color = random.choice(color_list)

    # On mention
    if client.user.mention in message.content.lower():
        await channel.send(f'Да-да, это я')

    # On other mentions
    for word in mentions:
        if word == message.content.lower():
            await channel.send(f'Ну так, це я, а шо таке?')
            print(f'{message.author}: {message.content}')

    # On Slava Ukraine message
    for word in ua_slava:
        if word in message.content.lower():
            await channel.send(embed = discord.Embed(description=f'Героям слава', color = 0xf9ff45).set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/197/197572.png'))
            print(f'{message.author}: {message.content}')

    # On other messages
    for word in n_slava:
        if word in message.content.lower():
            await channel.send(embed = discord.Embed(description=f'Пиздець росіській федерації!', color = 0xf9ff45).set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/197/197572.png'))
            print(f'{message.author}: {message.content}')

    # On hello messages
    for word in hello_words:
        if word in message.content.lower():
            await channel.send(embed = discord.Embed(description = f'Ну привіт, {message.author.mention} :heartpulse:', color = random_color))

    # On Osnova messages
    for word in o_words:
        if word in message.content.lower():
            await channel.send(f'Я')


    # On HowAreU messages
    for word in howareu:
        if word in message.content.lower():
            r = random.randint(1,2)
            if r == 1:
                await channel.send(f'Ай нормуль усе')
            else:
                await channel.send(f'Усе круто!')

    await client.process_commands(message)

@client.command(pass_context=True)
async def w(ctx):
    await ctx.send(embed = discord.Embed(description=f'Усім привіт!'))

@client.command(pass_context=True)
async def say(ctx):
    await ctx.message.delete()
    msg = input('Here: ')
    await ctx.send(msg)

@client.command(pass_context=True)
async def help(ctx, arg=None):
    emb = discord.Embed(title=f'Навігація по командам', description=f'*Префікс бота - **`***', color = 0x9059ff)

    # Commands list
    emb.add_field(name='**{}help**'.format(prefix), value='Побачити це вікно')
    emb.add_field(name='**{}bebra**'.format(prefix), value='Випадкова ГІФка про бебру :heart_eyes:')
    emb.add_field(name='**{}ping**'.format(prefix), value='Дізнатися пінг та іншу інформацію про бота (CPU, Mem, OS)')

    await ctx.send(embed = emb)

@client.command(pass_context=True, aliases = ['бебра', 'бєбра'])
async def bebra(ctx):
    try:
        await ctx.send(random.choice(gifs_list))
    except Exception as e:
        await ctx.send(f'{e}')

@client.command(pass_context=True, aliases = ['os', 'mem', 'memory', 'cpu'])
async def ping(ctx):
    battery = psutil.sensors_battery()
    percentbat = int(battery.percent)
    os_system = platform.system()
    os_release = platform.release()
    CPU = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    percentmem = int(mem.percent)
    date_time = datetime.timedelta(seconds = 10000)

    emb=discord.Embed(title=f'Ping | CPU | Mem | OS', color = random.choice(color_list))
    #emb.add_field(name="автономный заряд", value=f"{percentbat}%")
    emb.add_field(name="OS", value=f"{os_system}-{os_release}")
    emb.add_field(name="CPU", value=f"{CPU}%", inline=False)
    emb.add_field(name="Memory", value=f"{percentmem}%", inline=False)
    emb.add_field(name="Ping", value=f"{round(client.latency * 1000)}ms", inline=False)

    await ctx.send(embed=emb)

token = open('token.txt', 'r').read()
client.run(token)
