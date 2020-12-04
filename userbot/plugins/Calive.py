# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...

import os
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, ALIVE_PIC
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MARSHMELLOW USER"

MARSHMELLOW_VID="https://telegra.ph/file/432b2b4eb57fa7c50c12b.mp4"

if ALIVE_PIC is None:
    ALIVE_PIC=MARSHMELLOW_VID
else:
    ALIVE_PIC=ALIVE_PIC

pm_caption = "**✮ MY BOT IS RUNNING SUCCESFULLY 👩‍💻 CHECK YOURS  ✮**\n\n"

pm_caption += "**✧ IF YOU ARE BAD:** `THIS  IS YOUR DAD`\n\n"

pm_caption += "**✧ ALIVE:** `110% ALIVE SIR`\n\n"

pm_caption += "**✧ MASTER NAME :** `MARSHMELLOW\n\n"

pm_caption += "जली को आग🔥 और बूझी को राख🌫 कहते है और जिसका तुम👉 Status पढ़ रहे हो उसे Status_King👑 कहते हैं  \n`"

        
@borg.on(admin_cmd(pattern=r"calive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id,file=ALIVE_PIC,caption=pm_caption)
    await alive.delete()
