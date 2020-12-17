from telethon import events
import asyncio
import os
import sys
from userbot.utils import mellow_cmd
import random

img1="https://telegra.ph/file/a448826301fe63a96684f.jpg"
img2="https://telegra.ph/file/5f4c585b924f62428cca3.jpg"
img3="https://telegra.ph/file/4bd1c7c5753d4ed0c8375.jpg"
img4="https://telegra.ph/file/14cce3615b07141f94918.jpg"
img5="https://telegra.ph/file/b02006e54549aa2a84a18.jpg"
img6="https://telegra.ph/file/6483530fffe7d5bb1d16b.jpg"
img7="https://telegra.ph/file/5ed9ecc0f8bcd4f4ebea0.jpg"
img8="https://telegra.ph/file/35d3c84098cf56897418c.jpg"
img9="https://telegra.ph/file/3f20d84c3c682fe24ff97.jpg"
img10="https://telegra.ph/file/09e017a1898fa1f46294c.jpg"
img11="https://telegra.ph/file/46e7596fcc5e42b150e68.jpg"
img12="https://telegra.ph/file/a7113b4b047d18dca9793.jpg"
img13="https://telegra.ph/file/012bcdfeae8029337642b.jpg"
img14="https://telegra.ph/file/3b671ab3b4f07025b6f01.jpg"
img15="https://telegra.ph/file/34ba55eb1543578a1fc92.jpg"







@borg.on(mellow_cmd(outgoing=True, pattern="mmh"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("SENDING...:-)")
    await asyncio.sleep(0.9)
    x=(random.randrange(1,15))
    if x==1:
        await borg.send_file(event.chat_id,img1)
        await event.delete()
    if x==2:
        await borg.send_file(event.chat_id,img2)
        await event.delete()
    if x==3:
        await borg.send_file(event.chat_id,img3)
        await event.delete()
    if x==4:
        await borg.send_file(event.chat_id,img3)
        await event.delete()        
    if x==5:
        await borg.send_file(event.chat_id,img4)
        await event.delete()
    if x==6:
        await borg.send_file(event.chat_id,img5)
        await event.delete()
    if x==7:
        await borg.send_file(event.chat_id,img6)
        await event.delete()
    if x==8:
        await borg.send_file(event.chat_id,img7)
        await event.delete()        
    if x==9:
        await borg.send_file(event.chat_id,img9)
        await event.delete()        
    if x==10:
        await borg.send_file(event.chat_id,img10)
        await event.delete()
    if x==11:
        await borg.send_file(event.chat_id,img11)
        await event.delete()
    if x==12:
        await borg.send_file(event.chat_id,img12)
        await event.delete()
    if x==13:
        await borg.send_file(event.chat_id,img13)
        await event.delete()         
    if x==14:
        await borg.send_file(event.chat_id,img14)
        await event.delete()
    if x==15:
        await borg.send_file(event.chat_id,img15)
        await event.delete()