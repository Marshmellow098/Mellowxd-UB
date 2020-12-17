"""
Took from @HellBot_Offical made by @Kraken_The_BadASS
"""

from userbot.utils import mellow_cmd,edit_or_reply
from var import Var

@borg.on(mellow_cmd(pattern="xogame$"))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    mellow = "play"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, mellow) 
    await tap[0].click(event.chat_id)
    await event.delete()
