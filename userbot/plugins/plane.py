#By STARKTM1
from telethon import events
import asyncio
import os
import sys
from uniborg.util import mellow_cmd

@borg.on(mellow_cmd(pattern=r"plane"))
async def _(event):
    if event.fwd_from:
        return
        
        
    await event.edit("✈-------------")
    await asyncio.sleep(1)
    await event.edit("-✈------------")
    await asyncio.sleep(1)
    await event.edit("--✈-----------")
    await asyncio.sleep(1)
    await event.edit("---✈----------")
    await asyncio.sleep(1)
    await event.edit("----✈---------")
    await asyncio.sleep(1)
    await event.edit("-----✈--------")
    await asyncio.sleep(1)
    await event.edit("------✈-------")
    await asyncio.sleep(1)
    await event.edit("-------✈------")
    await asyncio.sleep(1)
    await event.edit("--------✈-----")
    await asyncio.sleep(1)
    await event.edit("---------✈----")
    await asyncio.sleep(1)
    await event.edit("----------✈---")
    await asyncio.sleep(1)
    await event.edit("-----------✈--")
    await asyncio.sleep(1)
    await event.edit("------------✈-")
    await asyncio.sleep(1)
    await event.edit("-------------✈")
    await asyncio.sleep(5)
    await event.delete()

