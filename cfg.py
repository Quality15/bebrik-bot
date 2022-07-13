import discord
from discord.ext import commands

# Command prefix
prefix = '`'

# Slava Ukraine array
ua_slava = ['слава украине', 'слава україні']

# Heroyam Slava array
h_slava = ['героям слава']

# Slava Nacii
n_slava = ['слава нации', 'слава нації', 'слава націі']

# Bebrik Mention
mentions = ['бебрик', 'бебрік', 'бєбрік', 'бєбрик']

# Hello Hords
hello_words = ['привет', 'привіт', 'здарова', 'доброе утро', 'приф']

# HowAreU Words
howareu = ['как дела', 'як справи', 'как вы', 'як ви']

# GIFs list
gifs_list = ['https://tenor.com/view/%D0%B1%D0%B5%D0%B1%D1%80%D0%B0-%D0%B1%D0%B5%D0%B1%D1%80%D0%B0%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA-%D0%B1%D1%8D%D0%B1%D1%80%D0%B0-%D0%BD%D1%8E%D1%85%D0%B0%D0%B9%D0%B1%D0%B5%D0%B1%D1%80%D1%83-gif-21235573',
        'https://tenor.com/view/%D0%B1%D0%B5%D0%B1%D1%80%D0%B0-%D0%B1%D0%B5%D0%B1%D1%80%D0%B0%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA-%D0%B1%D1%8D%D0%B1%D1%80%D0%B0-%D0%BD%D1%8E%D1%85%D0%B0%D0%B9%D0%B1%D0%B5%D0%B1%D1%80%D1%83-gif-21235573',
        'https://tenor.com/view/%D1%88%D1%80%D0%B5%D0%BA-%D0%BE%D1%81%D0%B5%D0%BB-%D0%B1%D0%B5%D0%B1%D1%80%D0%B0-%D0%BD%D1%8E%D1%85%D0%B0%D0%B9%D0%B1%D0%B5%D0%B1%D1%80%D1%83-bebra-gif-22648873',
        'https://tenor.com/view/bebra-morgenstern-gif-21970383',
        'https://tenor.com/view/%D0%B1%D0%B5%D0%B1%D1%80%D0%B0-%D0%BE%D1%85%D0%BE%D1%82%D0%B0%D0%BD%D0%B0%D0%B1%D0%B5%D0%B1%D1%80%D1%83-%D0%B4%D0%BC%D0%B8%D1%82%D1%80%D0%B8%D0%B9%D0%BA%D0%BE%D0%BC%D0%B0%D1%80%D0%BE%D0%B2-gif-23384124',
        'https://tenor.com/view/%D0%B1%D0%B5%D0%B1%D1%80%D0%B0-bebra-bebrinki-%D0%B1%D0%B5%D0%B1%D1%80%D0%B8%D0%BD%D0%BA%D0%B8-gif-22958722']

# Color list
color_list = [0xB22222,0xF08080,0xFFA500,0xF0E68C,0x7FFF00,0x00FA9A,0x2F4F4F,0x40E0D0,0x6495ED,
        0x8A2BE2,0xD8BFD8,0xDB7093]

# Osnova Words
o_words = ['основа', 'основу', 'войс']

# Chicken GIF
chicken_gif = ['https://media.discordapp.net/attachments/625774709778415617/662016115580469248/0041.gif?comment=NIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIGGERNIG', 'https://tenor.com/view/brick-eating-mukbang-gif-22115496']