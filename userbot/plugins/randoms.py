#Made By Sh1vam Inspired By Friday Donot KANG

import os


import numpy as np
import requests
from PIL import Image
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
import re
from userbot.utils import admin_cmd
from userbot import bot 
from userbot import bot as borg
sedpath = "./shivam/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)





@bot.on(admin_cmd(pattern=r"tig"))

async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/triggered?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.gif", "wb").write(r.content)
    lolbruh = "shivam.gif"
    await borg.send_file(
        event.chat_id, lolbruh, caption="Triggered....😬", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"wst"))

async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/wasted?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="⚰️ Wasted... 😵", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"rmbow"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/gay?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="The Rainbow Efect WOW", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"glass"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/glass?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="You got Into the Glass", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"gry"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/greyscale?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="You got grey coloured", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"invert"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/invert?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="i made u inverted ", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"ig"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/invertgreyscale?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="no reactions found 🙄 ", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"brght"))
async def lolmetrg(event):
    await event.edit("`hmm let me see what i can do to this`")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/brightness?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="brightness.....seems to be exploited ig 😶", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"bow"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/threshold?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="choose your which side", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"sepia"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/sepia?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="See this is called sepia ", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"red"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/red?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="bloody red u r now ", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"green"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/green?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="Go Green....Go Green...😂😂😂 ", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"blue"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/blue?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="blue huh hmm what can i tell about this 🤔 ", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"pixlte"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/pixelate?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="pixelate it is u kno 🤣🤣🤣", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"ytc"))
async def lolmetrg(event):
    givenvar=event.text
    text = givenvar[5:]
    try:
        global username, comment
        username, comment= text.split(".")
    except:
        await event.edit("`.ytc username.comment reply  to image`")
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/youtube-comment?avatar={imglink}&comment={comment}&username={username}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="This is A Youtube Commment 👀", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
'''@bot.on(admin_cmd(pattern=r"clr"))
async def lolmetrg(event):
    givenvar=event.text
    color = givenvar[5:]
    await event.edit("`hmm let me see what i can do to this hope u replied it with hex colour code and also put %23 instead of #`")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/color?avatar={imglink}&color={color}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="Coloured", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)'''
