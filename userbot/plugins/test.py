from telethon import events
import asyncio
import os
import sys
from uni@mellow.util import mellow_cmd

@mellow.on(mellow_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("Test Successfull. Boss !")      
