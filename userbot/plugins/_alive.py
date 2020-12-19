"""
@Mellowxd is the creator of this alive 
"""
import os
import asyncio
import random
from telethon import events
from userbot.utils import mellow_cmd
from userbot import ALIVE_NAME, ALIVE_PIC
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "✖𐌑𐌀𐍂𐍃𐋏‿𐌑𐌄𐌋𐌋𐍈✖"

MARSHMALLOW_PIC="https://telegra.ph/file/815e018dc949131ed9118.jpg"

if ALIVE_PIC is None:
    ALIVE_PIC=MARSHMALLOW_PIC
else:
    ALIVE_PIC=ALIVE_PIC

pm_caption = "**✖𐌑𐌀𐍂𐍃𐋏‿𐌑𐌄𐌋𐌋𐍈✖ IS ONLINE**\n"
pm_caption += f"**My Master** => **{DEFAULTUSER}**\n\n"
pm_caption += "🤖вσт ѕуѕтєм🤖🤖 \n\n"
pm_caption += "🐍Ⓟⓨⓣⓗⓞⓝ🐍 ==> 3.9.1\n"
pm_caption += "💻𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍💻 ==> 1.15.0\n"
pm_caption += "📜🄻🄸🄲🄴🄽🅂🄴📜 ==> 𝙰𝙶𝙿𝙻-𝟹.𝟶 𝙻𝚒𝚌𝚎𝚗𝚜𝚎\n\n"
pm_caption += "🧑‍💻 ₵ⱤɆ₳₮ɆⱤ ==> @Mellowxd\n\n"
pm_caption += "🌏S͓̽u͓̽p͓̽p͓̽o͓̽r͓̽t͓̽ ͓͓̽̽g͓̽r͓̽o͓̽u͓̽p͓̽🌏 ==> @marshmellowsupport\n\n"

@mellow.on(mellow_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id,file=ALIVE_PIC,caption=pm_caption)
    await alive.delete()
