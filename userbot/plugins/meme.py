"""
Memes Plugin for Userbot
usage = .meme 
made by @Mellowxd

"""
from telethon import events
import asyncio
import os
import sys
from uniborg.util import mellow_cmd

@borg.on(mellow_cmd(pattern=r"meme"))

async def meme(event):

    if event.fwd_from:

        return   

    mellowVar = event.text

    sleepValue = 3

    mellowVar = mellowVar[2:] 

           

    await event.edit("×××××××××××××"+mellowVar)

    await asyncio.sleep(sleepValue)

    await event.edit("××××××××××××"+mellowVar+"×")

    await asyncio.sleep(sleepValue)

    await event.edit("×××××××××××"+mellowVar+"××")

    await asyncio.sleep(sleepValue)

    await event.edit("××××××××××"+mellowVar+"×××")

    await asyncio.sleep(sleepValue)

    await event.edit("×××××××××"+mellowVar+"××××")   

    await asyncio.sleep(sleepValue) 

    await event.edit("××××××××"+mellowVar+"×××××")

    await asyncio.sleep(sleepValue)

    await event.edit("×××××××"+mellowVar+"××××××")

    await asyncio.sleep(sleepValue)

    await event.edit("××××××"+mellowVar+"×××××××")

    await asyncio.sleep(sleepValue)

    await event.edit("×××××"+mellowVar+"××××××××")

    await asyncio.sleep(sleepValue)

    await event.edit("××××"+mellowVar+"×××××××××")

    await asyncio.sleep(sleepValue)

    await event.edit("×××"+mellowVar+"××××××××××")

    await asyncio.sleep(sleepValue)

    await event.edit("××"+mellowVar+"×××××××××××")

    await asyncio.sleep(sleepValue)

    await event.edit("×"+mellowVar+"××××××××××××")

    await asyncio.sleep(sleepValue)

    await event.edit(mellowVar+"×××××××××××××")

    await asyncio.sleep(sleepValue)

    await event.edit(mellowVar)

    await asyncio.sleep(sleepValue)

"""
Bonus : Flower Boquee Generater
usage:- .flower

made by @Zello_cool7870

"""
@borg.on(mellow_cmd(pattern=r"flower"))
async def meme(event):
    if event.fwd_from:
        return   
    flower =" 🌹"
    sleepValue = 5
           
    await event.edit(flower+"        ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+"       ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+"      ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+"     ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+"    ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+"   ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+"   ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+"  ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+" ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+flower)
    await asyncio.sleep(sleepValue)
        
    
