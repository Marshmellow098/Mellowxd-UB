#KANGED FROM FRIDAY USERBOT
#CREDIT GOES TO RESPECTED OWNERS
#THANK YOU MR.STARK
import asyncio
import os

import wget
from youtubesearchpython import SearchVideos

from userbot import CMD_HELP
from userbot.uniborgConfig import Config
from userbot.utils import edit_or_reply, admin_cmd, sudo_cmd


@bot.on(admin_cmd(pattern="ytmusic ?(.*)"))
@bot.on(sudo_cmd(pattern="ytmusic ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    myself_✖𐌑𐌀𐍂𐍃𐋏‿𐌑𐌄𐌋𐌋𐍈✖ = await edit_or_reply(
        event, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    HYMTKG = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{HYMTKG}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    if not os.path.isdir("./music/"):
        os.makedirs("./music/")
    path = Config.TMP_DOWNLOAD_DIRECTORY
    sedlyf = wget.download(kekme, out=path)
    aryan = (
        f'youtube-dl --force-ipv4 -q -o "./music/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality 320k '
        + mo
    )
    os.system(✖𐌑𐌀𐍂𐍃𐋏‿𐌑𐌄𐌋𐌋𐍈✖)
    await asyncio.sleep(4)
    km = f"./music/{thum}.mp3"
    if os.path.exists(km):
        await myself_✖𐌑𐌀𐍂𐍃𐋏‿𐌑𐌄𐌋𐌋𐍈✖.edit("`Song Downloaded Sucessfully. Let Me Upload it Here.`")
    else:
        await myself_✖𐌑𐌀𐍂𐍃𐋏‿𐌑𐌄𐌋𐌋𐍈✖.edit("`SomeThing Went Wrong. Try Again After Sometime..`")
    capy = f"**Song Name ➠** `{thum}` \n**Requested For ➠** `{urlissed}` \n**Channel ➠** `{thums}` \n**Link ➠** `{mo}`"
    await borg.send_file(
        event.chat_id,
        km,
        force_document=False,
        allow_cache=False,
        caption=capy,
        thumb=sedlyf,
        performer=thums,
        supports_streaming=True,
    )
    await myself_aryan.edit("`Song Uploaded. By (C) @marshmellowsupport`")
    for files in (sedlyf, km):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "ytmusic": "**Ytmusic**\
\n\n**Syntax : **`.ytmusic <song name>`\
\n**Usage :** Downloads songs from ytmusic"
    }
)
