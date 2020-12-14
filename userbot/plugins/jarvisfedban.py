

import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd
import time
from userbot import ALIVE_NAME

naam = str(ALIVE_NAME)

bot = "@jarvisofficialsecuritybot"

@mellow.on(admin_cmd("fedban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return    
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
      async with @mellow.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/fban")
              audio = await conv.get_response()
              final = ("If you would like to know more about fban, use visit @jarvisofficialsecuritybot." , "")
              await @mellow.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @jarvisofficialsecuritybot `and retry!")
    elif "@" in sysarg:
      async with @mellow.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/fban " + sysarg)
              audio = await conv.get_response()
              final = ("If you would like to know more about fban, please visit @jarvisofficialsecuritybot." , "")
              await @mellow.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @jarvisofficialsecuritybot `and try again!")
    elif "" in sysarg:
      async with @mellow.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/fban " + sysarg)
              audio = await conv.get_response()
              final = ("If you would like to know more about fban, please visit @jarvisofficialsecuritybot." , "")
              await @mellow.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @jarvisofficialsecuritybot `and try again!")







@mellow.on(admin_cmd("unfedban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return    
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
      async with @mellow.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/unfban")
              audio = await conv.get_response()
              final = ("If you would like to know more about fban, use visit @jarvisofficialsecuritybot." , "")
              await @mellow.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @jarvisofficialsecuritybot `and retry!")
    elif "@" in sysarg:
      async with @mellow.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/unfban " + sysarg)
              audio = await conv.get_response()
              final = ("If you would like to know more about fban, please visit @jarvisofficialsecuritybot." , "")
              await @mellow.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @jarvisofficialsecuritybot `and try again!")
    elif "" in sysarg:
      async with @mellow.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/unfban " + sysarg)
              audio = await conv.get_response()
              final = ("If you would like to know more about fban, please visit @jarvisofficialsecuritybot." , "")
              await @mellow.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @jarvisofficialsecuritybot `and try again!")


