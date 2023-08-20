from telethon import TelegramClient, events
import phoenix.client
import os
import time
client = phoenix.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.alive'))
async def alive(noob_py):
		client = noob_py.client
		me = await client.get_me()
		username = me.username
		img = await client.download_profile_photo(username)
		await client.edit_message(noob_py.message, "Good day...")
		time.sleep(0.5)
		await noob_py.respond("""**Foydalanuvchi: @{}**
**Phoenix Userbot:** https://t.me/phoenix_userbot

**Developer:** @programmer_www
			
v.1.0.0

📥 INSTALL 

$ pkg update && pkg upgrade

$ apt update && apt upgrade

$ pkg install git

$ pkg install python

$ git clone https://github.com/Hacker-UZ/phoenix-userbot

$ cd phoenix-userbot

$ python setup.py

$ python main.py""".format(username, ' '), file=img)
		await noob_py.message.delete()
