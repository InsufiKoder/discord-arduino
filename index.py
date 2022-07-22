import discord
import serial as s
import time as t

ser = s.Serial('/dev/ttyUSB0', 9600, timeout=0)
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!help':
        await message.channel.send("Commands: !blue-on, !blue-off, !red-on, !red-off, !yellow-on, !yellow-off")

    if message.content == '!blue-on':
        await message.channel.send("Blue led is turned on.")
        ser.write(b'1')

    if message.content == '!blue-off':
        await message.channel.send("Blue led is turned off.")
        ser.write(b'0')

    if message.content == '!red-on':
        await message.channel.send("Red led is turned on.")
        ser.write(b'2')

    if message.content == '!red-off':
        await message.channel.send("Red led is turned off.")
        ser.write(b'3')

    if message.content == '!yellow-on':
        await message.channel.send("Yellow led is turned on.")
        ser.write(b'4')

    if message.content == '!yellow-off':
        await message.channel.send("Yellow led is turned off.")
        ser.write(b'5')

client.run("YOUR_OWN_BOT_TOKEN_HERE")
