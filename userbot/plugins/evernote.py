from telethon import events
import asyncio
import os
import sys

@mellow.on(events.NewMessage(pattern=r"^.note (.*)", outgoing=True))
async def test(event):
    if event.fwd_from:
        return
    uwu = event.pattern_match.group(1)
    await event.edit("Added note to Evernote".format(uwu))
    await @mellow.send_message("@ifttt", "#note {}".format(uwu))
