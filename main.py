from telethon import TelegramClient, events, sync
from time import gmtime, strftime
from emoji import emojize
import asyncio
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio, aiocron, datetime
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, User
import phoenix.client, phoenix.konspekt, phoenix.lovelyrun, phoenix.scan, phoenix.bombs, phoenix.help, phoenix.loading, phoenix.emoji, phoenix.dump, phoenix.sexy, phoenix.type, phoenix.magicrun, phoenix.animation, phoenix.animation2, phoenix.mute, phoenix.nq, phoenix.fuck, phoenix.rev, phoenix.tr, phoenix.userinfo, phoenix.base64, phoenix.react, phoenix.snow, phoenix.ar, phoenix.smsbomb, phoenix.qrc, phoenix.rename, phoenix.iptrace, phoenix.spam, phoenix.alive, phoenix.tagall, phoenix.afk, phoenix.timer, phoenix.ping
import os, sys
#Developer: @programmer_www

#Modules
client = phoenix.client.client
client.add_event_handler(phoenix.help.help)
client.add_event_handler(phoenix.bombs.bombs)
client.add_event_handler(phoenix.loading.loading)
client.add_event_handler(phoenix.emoji.itachi) 
client.add_event_handler(phoenix.dump.dump)
client.add_event_handler(phoenix.sexy.sexy)
client.add_event_handler(phoenix.type.type)
client.add_event_handler(phoenix.magicrun.magicrun)
client.add_event_handler(phoenix.animation.lul)
client.add_event_handler(phoenix.animation.snake)
client.add_event_handler(phoenix.animation.nothappy)
client.add_event_handler(phoenix.animation.clock)
client.add_event_handler(phoenix.animation.muah)
client.add_event_handler(phoenix.animation.heart)
client.add_event_handler(phoenix.animation.hearts)
client.add_event_handler(phoenix.animation.gym)
client.add_event_handler(phoenix.animation.earth)
client.add_event_handler(phoenix.animation.moon)
client.add_event_handler(phoenix.animation.candy)
client.add_event_handler(phoenix.animation.smoon)
client.add_event_handler(phoenix.animation.tmoon)
client.add_event_handler(phoenix.animation.clown)
client.add_event_handler(phoenix.animation2.star)
client.add_event_handler(phoenix.animation2.boxs)		
client.add_event_handler(phoenix.animation2.rain)
client.add_event_handler(phoenix.animation2.clol)
client.add_event_handler(phoenix.animation2.odra)
client.add_event_handler(phoenix.animation2.fleaveme)		
client.add_event_handler(phoenix.animation2.loveu)
client.add_event_handler(phoenix.animation2.plane)
client.add_event_handler(phoenix.animation2.police)
client.add_event_handler(phoenix.animation2.jio)		
client.add_event_handler(phoenix.animation2.solarsystem)
client.add_event_handler(phoenix.mute.mute)
client.add_event_handler(phoenix.nq.nq)
client.add_event_handler(phoenix.fuck.fuck)
client.add_event_handler(phoenix.rev.rev)
client.add_event_handler(phoenix.tr.tr)
client.add_event_handler(phoenix.userinfo.userinfo)
client.add_event_handler(phoenix.base64.runb64)				
client.add_event_handler(phoenix.react.react)
client.add_event_handler(phoenix.snow.snow)
client.add_event_handler(phoenix.ar.runar)
client.add_event_handler(phoenix.qrc.runqrc)
client.add_event_handler(phoenix.rename.rename)	
client.add_event_handler(phoenix.iptrace.iptrace)
client.add_event_handler(phoenix.spam.delayspam)
client.add_event_handler(phoenix.smsbomb.runj)	
client.add_event_handler(phoenix.alive.alive)
client.add_event_handler(phoenix.tagall.tagall)
client.add_event_handler(phoenix.afk.runafkon)
client.add_event_handler(phoenix.afk.runafkoff)
client.add_event_handler(phoenix.afk.runafkstatus)
client.add_event_handler(phoenix.afk.runmcfafk)
client.add_event_handler(phoenix.afk.runafk)
client.add_event_handler(phoenix.timer.timer)
client.add_event_handler(phoenix.timer.numbers)
client.add_event_handler(phoenix.timer.setclock)
client.add_event_handler(phoenix.timer.runsda)
client.add_event_handler(phoenix.timer.runrda)
client.add_event_handler(phoenix.timer.rundrc)
client.add_event_handler(phoenix.timer.runrts)
client.add_event_handler(phoenix.timer.runrgm)
client.add_event_handler(phoenix.timer.setbioclock)
client.add_event_handler(phoenix.scan.chatscan)
client.add_event_handler(phoenix.ping.ping)
client.add_event_handler(phoenix.lovelyrun.lovelyrun)
client.add_event_handler(phoenix.konspekt.tconv)
client.add_event_handler(phoenix.scan.loginhack)



	
client.start()

os.system("clear")
print("""\033[031m
   ___  __ ______  _____  _______  __   __  _____________  ___  ____  ______
  / _ \/ // / __ \/ __/ |/ /  _/ |/_/  / / / / __/ __/ _ \/ _ )/ __ \/_  __/
 / ___/ _  / /_/ / _//    // /_>  <   / /_/ /\ \/ _// , _/ _  / /_/ / / /   
/_/  /_//_/\____/___/_/|_/___/_/|_|   \____/___/___/_/|_/____/\____/ /_/    
      
Developer: @programmer_www
Telegram channel: @phoenix_userbot
""")
print("\033[032mStarted")

client.run_until_disconnected()
