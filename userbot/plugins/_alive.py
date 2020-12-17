# Thanks to prothinkergang 
# Thanks to @YOU_ARE_UNDER_ARREST for alive pic




import os
import asyncio
import random
from telethon import events
from userbot.utils import mellow_cmd
from userbot import ALIVE_NAME, ALIVE_PIC
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MARSHMELLOW USER"

MARSHMALLOW_PIC="https://telegra.ph/file/815e018dc949131ed9118.jpg"

if ALIVE_PIC is None:
    ALIVE_PIC=MARSHMALLOW_PIC
else:
    ALIVE_PIC=ALIVE_PIC

pm_caption = "**MARSHMELLOW USERBOT IS ONLINE**\n"
pm_caption += f"**My Master** => **{DEFAULTUSER}**\n\n"
pm_caption += f"**{DEFAULTUSER} is alive 😁😁😋😋**\n\n"
pm_caption +=f"**MADE WITH LOVE AND CARE 😉**\n\n"
pm_caption +=f"**{DEFAULTUSER} IS PRO😎😎**\n\n"
pm_caption +=f"**Python Version => 3.9.1**\n\n"
pm_caption +=f"**Telethon Version => 1.15.0**\n\n"
pm_caption +=f"**[Support Group](https://t.me/marshmellowsupport)**\n\n"
pm_caption +=f"**[Channel for Updates](https://t.me/marshmellowuserbot)**\n\n"
pm_caption +=f"**Wanna deploy your owm Marshmellow pay me 10000 dollar**\n\n"
pm_caption += "[REPO](https://github.com/Marshmellow098/MARSHMELLOW-USERBOT)"
@borg.on(mellow_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id,file=ALIVE_PIC,caption=pm_caption)
    await alive.delete()
