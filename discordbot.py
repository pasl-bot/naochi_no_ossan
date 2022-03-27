import discord
from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')

emoji_list = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣", "🔟"]
recruit_channel = int(getenv('RECRUIT_CHANNEL'))

isConnection = False

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def recruit(ctx, title, message, *select):
    if len(select) > 10:
        await ctx.send("選択肢が多すぎるで。ワレェ")
        return

    channel = bot.get_channel(recruit_channel)

    value = ""
    for num in range(len(select)):
        value += emoji_list[num] + " " + select[num] + "\n"
    
    embed = discord.Embed(title = message, color = discord.Colour.blue())
    msg = await channel.send("**" + title+ "**", embed = embed)

    for i in range(len(select)):
        await msg.add_reaction(emoji_list[i])

    await channel.send('選び始めてええで')
    return


@bot.command()
async def connect(ctx):
    if isConnection != True:
        vc = ctx.author.voice.channel
        await ctx.send('来たで。ワレェ')
        isConnection = True
        return
    else:
        await ctx.send('他で呼ばれとるで。ワレェ')


@bot.command()
async def disconnect(ctx):
    if isConnection == True:
        await ctx.voice_client.disconnect()
        await ctx.send('ほなまた～。ワレェ')
        isConnection = False
        return


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
