from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


token = getenv('OTQ5NjYxMTk5NzA3MDE3MzA2.YiNm6Q.wjGEykeIgOI3cBigo3Z7F4kbd0E')
bot.run(token)