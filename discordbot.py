from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.commands
async def otupi(ctx):
    await ctx.send('ドラゴンフラッグ')

@bot.commands
async def test(ctx):
    await ctx.send('tttt')
    
bot.run(token)
