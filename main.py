from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

def keep_alive():
    t = Thread(target=run)
    t.start()

# يشغل الخادم على المدى الطويل
keep_alive()

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot("-", intents=intents)

manager_role_id = 1195475452417036439 # ايدي رتبة المانجر

event_user_role_id = 1162417027697344585 # ايدي الرتبه اللي هتضاف

@bot.event
async def on_message(message):
    if (manager_role := message.guild.get_role(manager_role_id)) in message.author.roles:
        if message.content.startswith(('-add ', '-add ')) or message.content.startswith(('-remove ', '-remove ')):
            action = "add" if message.content.startswith(('-add ', '-add ')) else "remove"
            try:
                try:
                    user_id = int(message.content.strip().split(f"-{action}")[-1])
                except:
                    user_id = int(message.content.strip().split(f"-{action}")[-1].strip("< > @"))

                user = await message.guild.fetch_member(user_id)

                role = message.guild.get_role(event_user_role_id)

                if role and user:
                    if action == "add" and role in user.roles:
                        await message.channel.send(f'**__<@{user.id}>__ لديه الرتبة بالفعل**')
                    elif action == "add":
                        await user.add_roles(role, atomic=True)
                        await message.channel.send(f'**تم إضافة الرتبة لـ __<@{user.id}>__**')
                    elif action == "remove" and role in user.roles:
                        await user.remove_roles(role)
                        await message.channel.send(f'**تم إزالة الرتبة من __<@{user.id}>__**')
                    elif action == "remove":
                        await message.channel.send(f'**__<@{user.id}>__ ليس لديه الرتبة**')

            except:
                pass


bot.run("MTE5NjQ5NTE0MTA2Njc4MDc0Mw.GaYaZc.nTnfB8wM4g0fW8icnK7NqVXUV6uZdp-7qQldOk") # امسح الكلام ده واكتب التوكين بداله يعني امسح ال GHDFG