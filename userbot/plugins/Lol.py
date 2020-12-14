# (c) @UniBorg

from telethon import events
import asyncio
from collections import deque
from uni@mellow.util import mellow_cmd

@mellow.on(mellow_cmd(pattern=r"lol"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("😂🤣😂🤣😂🤣"))
	for _ in range(5):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
