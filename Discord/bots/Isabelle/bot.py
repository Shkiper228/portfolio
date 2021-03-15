import discord
import datetime
from discord.ext import commands
from datetime import datetime
from datetime import date
from time import sleep

client = commands.Bot( command_prefix = "$", intents = discord.Intents.all())

burndays = dict(
	Flurbis	=	'02.02.2007',
	Katrylka=	'04.04.2006',
	Nemi	=	'13.09.2005',
	Nechest	= 	'08.09.2004',
	Polly	= 	'04.02.2006',
	Prizrak	= 	'22.06.2002',
	Skumpi	= 	'04.01.2004',
	Kepler	= 	'07.04.2020',
	Annif	= 	'23.02.2007',
	якийсь_глек228 = '16.03.2002'
	)

@client.event
#індикація запуску
async def on_ready():
	while True:
		channel = client.get_channel(716207219422658590)
		print('Connect success!!!')
		current_datetime = datetime.now()
		names = list(burndays.keys())
		i = 0
		for been in burndays.values():
			been_date = datetime.strptime(been, '%d.%m.%Y')
			if current_datetime.day == been_date.day and current_datetime.month == been_date.month:
				years = current_datetime.year - been_date.year
				print(years)
				print(names[i])
				await channel.send(f'Сьогодні в учасника @{names[i]} День народження, тому не забудьте привітати іменинника! Йому уже виповнилось {years}')
			i += 1
		sleep(23*60*60)

@client.command(pass_context = True)

async def Isabelle(ctx):
	await ctx.send('Та в мене голова болить. Відстань')

token = open ('token.txt', 'r').readline()
client.run(token)