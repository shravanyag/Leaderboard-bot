from discord.ext import commands
from .monitor import *
import os

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Type '.lb' in to see leaderboard when you are not on a call")
    async def lb(self, ctx):
        print(member_details)
        if ctx.channel.id == 851420686379122719:
            member_stats = []
            for key, value in member_details.items():
                member_stats.append([key, round(value[2]/3600, 2)])
            print("in test")
            
            lb_temp = sorted(member_stats, key=lambda k: k[1], reverse=True)
            print(lb_temp)
            str_lb = ""
            for i in range(len(lb_temp)):
                temp =  ""
                temp = str(i+1) + ". " + str(lb_temp[i][0]) + " : " + str(lb_temp[i][1]) + " hrs\n"
                str_lb = str_lb + temp
            lb_ans = "\n***~All Time Leaderboard~***\n" + str_lb
            await ctx.send(lb_ans)
        else:
            await ctx.send("Leaderboard commands work only in the designated channel!!!")

def setup(bot):
    bot.add_cog(Leaderboard(bot))
