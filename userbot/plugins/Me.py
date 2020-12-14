""" made only for Marshmellow userbot don't kang it our else will make so many report to you that your account will get ban """

from userbot.utils import admin_cmd

@bot.on(admin_cmd(pattern="me", outgoing=True))
async def hello_users(event):
    if event.fwd_from:
        return
    await event.edit("**HELLO AND WELCOME TO MARSHMALLOW USERBOT**\n\n**Its your friend @Mellowxd always at your help**\n\n wanna deploy your own  Marshmellow click on the below make your own\n\n [Make your own](https://dashboard.heroku.com/new?template=https://github.com/Marshmellow098/MARSHMELLOW-USERBOT)")