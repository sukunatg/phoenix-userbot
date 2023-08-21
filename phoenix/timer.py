from telethon import TelegramClient, events, sync
from time import sleep
from datetime import datetime
import asyncio, aiocron, datetime
import asyncio
from telethon import TelegramClient, events, sync, functions, types, Button
import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".timer"))
async def timer(event):
        msg=event.message.raw_text.split()
        t=int(msg[1])
        mins=0
        while t>0:
                secs=t
                if(secs>=60):
                        mins=secs//60
                        secs-=mins*60
                else: mins=0
                timer=f"{mins}:{secs}"
                await event.edit(timer)
                await asyncio.sleep(1)
                t-=1
        await event.edit("time out i!!!")
        await asyncio.sleep(3)
        await event.delete()


@events.register(events.NewMessage(outgoing=True, pattern=".numbers"))
async def numbers(event):
        msg=event.message.raw_text.split()
        t=int(msg[1])
        await event.delete()
        while t>0:
                sleep(1)
                await client.send_message(event.message.to_id,str(t))
                t-=1

@events.register(events.NewMessage(outgoing=True, pattern=".setclock"))
async def setclock(event):
    await event.edit('Setting clock...')
    from telethon.tl.functions.account import UpdateProfileRequest
    msg=event.message.raw_text.split()
    t=int(msg[1])
    t*=60
    while t>0:
            from datetime import datetime
            today = datetime.today()
            time= today.strftime("| %H:%M |")
            await client(UpdateProfileRequest(last_name=str(time)))
            await asyncio.sleep(60)
            t-=1
            await event.edit('Clock setted succesfully')
            sleep(2)
            await event.delete()
    await client(UpdateProfileRequest(last_name="Vaqt nisbiy tushuncha !!"))
 



from telethon import events
from time import sleep

@events.register(events.NewMessage(outgoing=True, pattern=r'\.sda'))
async def runsda(event):
    await event.edit("Qidirilmoqda...")
    sleep(1)
    await event.delete()
    messagelocation = event.to_id
    deletedid = []
    try:
        chatname = event.chat.title
        async for users in event.client.iter_participants(messagelocation):
            if users.deleted:
                deletedid.append(users.id)
        countdeletedid = len(deletedid)
        if countdeletedid == 1:
            await event.client.send_message(messagelocation, f"{countdeletedid} O'chirilgan hisoblar topildi \nGuruh nomi: {chatname}")
        elif countdeletedid == 0:
            await event.client.send_message(messagelocation, f"O'chirilgan hizoblar topilmadi\nGuruh nomi: {chatname}")
        else:
            await event.client.send_message(messagelocation, f"{countdeletedid} O'chirilgan hisoblar topildi \nGuruh nomi: {chatname}")
    except:
        await event.client.send_message(messagelocation, "Something Went Wrong")

@events.register(events.NewMessage(outgoing=True, pattern=r'\.rda'))
async def runrda(event):
    await event.edit("waiting...")
    sleep(1)
    await event.delete()
    messagelocation = event.to_id
    deletedid = []
    try:
        chatname = event.chat.title
        async for users in event.client.iter_participants(messagelocation):
            if users.deleted:
                deletedid.append(users.id)
                await event.client.kick_participant(messagelocation, users.id)
        countdeletedid = len(deletedid)
        if countdeletedid == 1:
            await event.client.send_message(messagelocation, f"{countdeletedid} O'chirilgan hisoblar guruhdan o'chirib tashlandi\n guruh nomi:  {chatname}")
        elif countdeletedid == 0:
            await event.client.send_message(messagelocation, f"O'chirilgan hizoblar topilmadi\nGuruh nomi: {chatname}")
        else:
         await event.client.send_message(messagelocation, f"{countdeletedid} O'chirilgan hisoblar chiqarib tashlandi' {chatname}")
    except:
        await event.client.send_message(messagelocation, "Some eror")
 

from os import remove

@events.register(events.NewMessage(outgoing=True, pattern=r'\.rcd'))
async def rundrc(event):
    await event.delete()
    try:
        getrestrictedcontent = await event.get_reply_message()
        downloadrestrictedcontent = await getrestrictedcontent.download_media()
        await event.client.send_file("me", downloadrestrictedcontent)
        remove(downloadrestrictedcontent)
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.rts'))
async def runrts(event):
    await event.delete()
    try:
        foundrestrictedcontent = await event.get_reply_message()
        restricteddata = foundrestrictedcontent.message
        await event.client.send_message("@string_session_sender_bot", restricteddata)
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.rgm'))
async def runrgm(event):
    await event.edit("recovery...")
    sleep(1)
    await event.delete()
    try:
        targetgroup = event.to_id
        recoveredplace = "me"
        grouplog = await event.client.get_admin_log(targetgroup, edit=False, delete=True)
        for restore in grouplog:
            await event.client.send_message(recoveredplace, restore.original.action.message, silent=True)
    except:
        pass
        
@events.register(events.NewMessage(outgoing=True, pattern=".setbioclock"))
async def setbioclock(event):
        from telethon.tl.functions.account import UpdateProfileRequest
        await event.edit('Clock setting...')
        msg=event.message.raw_text.split()
        t=int(msg[1])
        t*=60
        await event.delete()
        while t>0:
                from datetime import datetime
                today = datetime.today()
                time= today.strftime("%H:%M | %A | %d | %B | %Y")
                await client(UpdateProfileRequest(about=str(time)))
                await asyncio.sleep(60)
                t-=1
                await event.client.send_message('Clock setted succesfully')
                sleep(2)
                await event.delete()
        await client(UpdateProfileRequest("Vaqt nisbiy tushuncha !!"))
 
