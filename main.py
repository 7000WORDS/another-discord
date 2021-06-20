import discord


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@client.event
async def 

client.run('ODU2Mjk5MTU1NzY0MjgxNDA0.YM_AvA.0oAGoYIetZiM1UEZqMD7rk9urwQ')
