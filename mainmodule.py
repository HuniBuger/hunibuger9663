import discord
from discord.ext import commands
import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
new_work_time = {}  # 신규근무시간 딕셔너리
cumulative_work_time = {}  # 누적근무시간 딕셔너리

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def start(ctx):
    if ctx.author.id in new_work_time:
        await ctx.send(f"{ctx.author.mention}님, 이미 근무 시작하셨습니다. / You already started working")
    else:
        new_work_time[ctx.author.id] = datetime.datetime.now()
        await ctx.send(f"{ctx.author.mention}님, 근무 시작하셨습니다. / You started working")

@bot.command()
async def end(ctx):
    if ctx.author.id in new_work_time:
        work_minutes = (datetime.datetime.now() - new_work_time[ctx.author.id]).total_seconds() // 60
        await ctx.send(f"{ctx.author.mention}님, 근무 종료하셨습니다.\n"
                       f"근무 시간은 {work_minutes}분입니다. / You end working, \n"
                       f"Working time is {work_minutes}m.")
        cumulative_work_time[ctx.author.id] = cumulative_work_time.get(ctx.author.id, 0) + work_minutes
        del new_work_time[ctx.author.id]
    else:
        await ctx.send(f"{ctx.author.mention}님, 근무 시작 명령어를 먼저 입력해주세요.")

@bot.command()
async def log(ctx):
    if ctx.author.id in new_work_time:
        work_minutes = (datetime.datetime.now() - new_work_time[ctx.author.id]).total_seconds() // 60
        await ctx.send(f"{ctx.author.mention}님, 현재까지의 근무 시간은 {work_minutes}분입니다.")
    else:
        total_work_minutes = cumulative_work_time.get(ctx.author.id, 0)
        await ctx.send(f"{ctx.author.mention}님, 누적 근무 시간은 {total_work_minutes}분입니다. / Your cumulative work time is {total_work_minutes}m.")

@bot.command()
async def ranking(ctx):
    await ctx.send(cumulative_work_time)

@bot.command()
async def clear19721121(ctx):
    if ctx.author.id == 711596520004124742:  # 해당 사용자 ID에 맞게 수정하세요.
        new_work_time.clear()
        cumulative_work_time.clear()
        await ctx.send("모든 딕셔너리를 초기화했습니다. / All dictionaries have been cleared.")
    else:
        await ctx.send("권한이 없습니다. / You don't have the permission to do this.")

bot.run("MTEzNjIxOTM3MzM0NzAyOTAzMg.GrrArB.-rC3hTNW8ulNt6bFx2NKPul3Uebqea24Q-1uto")
