
"""
.autobio"""

# EVERY IDEA WORTHS
# Kang Them with Credit
# (C) phantom Userbot

import asyncio
import random
import time
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME


RANDOM_BIO =(
  "Happiness never goes out of style",
  "Always be yourself",
  "Scratch here ▒▒▒▒▒▒ to Reveal my secret bio",
  "Sprinkling a bit of magic",
  "Simple but significant",
  "One day, I’m gonna make the onions cry"
  "Trying My Best !!",
  "Happy In Myself",
  "I AM UNIQUE",
)
PLANE=random.choice(RANDOM_BIO)

BIO_MSG = Config.BIO_MSG

if BIO_MSG is None:
  BIO_MSG = PLANE

DEL_TIME_OUT = 60

@borg.on(admin_cmd(pattern="autobio"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅{DMY} 🔥{BIO_MSG}🔥 ⌚️{HM}"
        logger.info(bio)
        try:
            await event.edit("**Autobio Enabled**")
            await asyncio.sleep(8)
            await event.delete()
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await borg.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Bio"
            # )
        await asyncio.sleep(DEL_TIME_OUT)
