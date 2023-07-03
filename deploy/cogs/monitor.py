import discord
from discord.ext import commands
import calendar
import time

member_details = {'aristotle' : [0.0, 0.0, 0.0], 'Ash5Man' : [0.0, 0.0, 0.0], 'avaraana' : [0.0, 0.0, 0.0], 'elsecaller24' : [0.0, 0.0, 0.0], 'Fray' : [0.0, 0.0, 0.0], 'ganeshhere' : [0.0, 0.0, 0.0], 'IAmGroot' : [0.0, 0.0, 0.0], 'Ina' : [0.0, 0.0, 0.0], 'lageyraho21' : [0.0, 0.0, 0.0], 'Meredith' : [0.0, 0.0, 0.0], 'Mikhael' : [0.0, 0.0, 0.0], 'mimir' : [0.0, 0.0, 0.0], 'MrX' : [0.0, 0.0, 0.0], 'mynamejeff' : [0.0, 0.0, 0.0], 'Neha' : [0.0, 0.0, 0.0], 'omega_blackstar1391' : [0.0, 0.0, 0.0], 'Pradeep Reddy | CSE \'21' : [0.0, 0.0, 0.0], 'Rathustra' : [0.0, 0.0, 0.0], 'Rex Buckingham' : [0.0, 0.0, 0.0], 'SaswatiS' : [0.0, 0.0, 0.0], 'Shamshana' : [0.0, 0.0, 0.0], 'shibam114' : [0.0, 0.0, 0.0], 'shreya' : [0.0, 0.0, 0.0], 'stoned monkey' : [0.0, 0.0, 0.0], 'thepolicydreamer' : [0.0, 0.0, 0.0], 'Vriti' : [0.0, 0.0, 0.0], 'Zumit | UPSC' : [0.0, 0.0, 0.0]}

class Monitor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.bot:
            return

        if not before.channel:
            '''if(after.channel.name == "Break/Games"):
              return'''
            print("in monitoring...")
            print(f'{member.name} joined {after.channel.name}')
            member_details[member.name][0] = time.time()
            print(member_details)

        if before.channel and not after.channel:
            '''if(before.channel.name == "Break/Games"):
              return'''
            print("in monitoring...")
            print(f'{member.name} left {before.channel.name}')
            if(member_details[member.name][0] == 0.0):
              member_details[member.name][0] = 0.0
              member_details[member.name][1] = 0.0
              print(member_details)
            else:
              member_details[member.name][1] = time.time()
              member_details[member.name][2] += member_details[member.name][1] - member_details[member.name][0]
              member_details[member.name][0] = 0.0
              member_details[member.name][1] = 0.0
              print(member_details)

        if before.channel and after.channel:
            '''if(before.channel.name == "Break/Games"):
              member_details[member.name][0] = time.time()
            elif(after.channel.name == "Break/Games"):
              member_details[member.name][1] = time.time()
              member_details[member.name][2] += member_details[member.name][1] - member_details[member.name][0]
              member_details[member.name][0] = 0.0
              member_details[member.name][1] = 0.0'''
            print("in monitoring...")
            if before.channel.id != after.channel.id:
                print(f'{member.name} switched from {before.channel.name} to {after.channel.name}')
            else:
                print("something else happened")

def setup(bot):
    bot.add_cog(Monitor(bot))
