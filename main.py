from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    asyncio.create_task(business)
    await asyncio.sleep(240)
    asyncio.create_task(compsci())


async def compsci():
    print('Successfully Ran compsci function ')
    while True:
        channel = bot.get_channel(967182330181615656)
        messages = await channel.history(limit=1000).flatten()

        compsci = []

        for msg in messages:
            compsci.append(msg.content)

        randomFact = random.choice(compsci)
        channel = bot.get_channel(967182409500094484)
        await channel.send(f'<@!779984843823906827> {randomFact}')
        await asyncio.sleep(random.randint(600, 1200))


async def business():
    print('Successfully Ran business function ')
    while True:
        channel = bot.get_channel(967182540676923462)
        messages = await channel.history(limit=1000).flatten()

        business = []

        for msg in messages:
            business.append(msg.content)

        randomFact = random.choice(business)
        channel = bot.get_channel(967182576278188102)
        await channel.send(f'<@!779984843823906827> {randomFact}')
        await asyncio.sleep(random.randint(600, 1200))
