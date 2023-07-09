import discord
from discord.ext import commands

pd = "12345678"#密碼
admin_role_name = 'ADMIN'#需要被保護的身分組權限
command_role = 'ADMIN'#能使用此指令的身分組成員 建議與需要被保護的身分組相同

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name="grant_admin")
@commands.has_role(command_role)
async def grant_admin(ctx, password):
    try:
        if password == pd:
            admin_role = discord.utils.get(ctx.guild.roles, name=admin_role_name)
            permissions = discord.Permissions(administrator=True)
            await admin_role.edit(permissions=permissions)
            await ctx.send("已開啟管理員權限")
        elif password != pd:
            await ctx.send("密碼錯誤")
    except:
        print("指令語法錯誤 正確語法:!grant_admin <password>")
        await ctx.send("指令語法錯誤 正確語法:!grant_admin <password>")
    finally:
        await ctx.message.delete()  # 刪除指令訊息


@bot.command(name='revoke_admin')
@commands.has_role(command_role)
async def revoke_admin(ctx, password):
    try:
        if password == pd:
            admin_role = discord.utils.get(ctx.guild.roles, name=admin_role_name)
            permissions = discord.Permissions(administrator=False)
            await admin_role.edit(permissions=permissions)
            await ctx.send("已關閉管理員權限")
        elif password != pd:
            await ctx.send("密碼錯誤")
    except:
        print("指令語法錯誤 正確語法:!revoke_admin <password>")
        await ctx.send("指令語法錯誤 正確語法:!revoke_admin <password>")
    finally:
        await ctx.message.delete()  # 刪除指令訊息


@bot.command()
async def ping(ctx):
    """測試機器人是否在線上"""
    await ctx.send('Pong! Latency: {}ms'.format(round(bot.latency * 1000)))
    await ctx.message.delete()  # 刪除指令訊息

'''
@bot.command(name="help")
@commands.has_role('Admin')
async def help(ctx):
    await ctx.send("開啟權限: !grant_admin <password>")
    await ctx.send("關閉權限: !revoke_admin <password>")
    await ctx.message.delete()  # 刪除指令訊息
'''


bot.run("MTA5MjE1MDc1OTMxNzA1MzU3MQ.GWJs6B.r10F5USoGQl8CF5h_AkpqLk8Nx37w2vVATKBwc")
