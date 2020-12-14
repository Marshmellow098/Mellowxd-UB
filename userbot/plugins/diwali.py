# Plugin Made BY @Anonymous_Machinee 
# Use With Or Without Credit
# Originally Made for Phantom Userbot
# HAPPY DIWALI TO ALL

import random
import asyncio
from telethon import events
from userbot.utils import admin_cmd
from telethon import events
from userbot import ALIVE_NAME


## IMAGE COLLECTION
img1="https://telegra.ph/file/ad21507bf9f6a176f2b19.mp4"
img2="https://telegra.ph/file/1d909440538a24696cca8.mp4"
img3="https://telegra.ph/file/844e5d2d933272aacc056.mp4"
img4="https://telegra.ph/file/eacbe48ec708c78caee13.mp4"
img5="https://telegra.ph/file/5af205f8e0fa2bf0b7cf2.mp4"
img6="https://telegra.ph/file/babbe598589014e94f133.mp4"
img7="https://telegra.ph/file/4f11dca7f02392ce14c43.mp4"
img8="https://telegra.ph/file/c7b5ce2c4f1f0d089a6b1.mp4"
img9="https://telegra.ph/file/4267c3dfbc333892286c5.mp4"
img10="https://telegra.ph/file/a6ce36f1777cbf3ecb88a.jpg"
img11="https://telegra.ph/file/11d69e6677bae30b76b7f.jpg"
img12="https://telegra.ph/file/dcf1e8f60c2762c6374b2.jpg"
img13="https://telegra.ph/file/6255a356590855cd34186.jpg"
img14="https://telegra.ph/file/c0a60bde542f12000bfe0.jpg"
img15="https://telegra.ph/file/853187f53fddc15817aca.jpg"
img16="https://telegra.ph/file/eeae39166bff551c0cce0.jpg"
img17="https://telegra.ph/file/8c812f9212a7e12038f1a.jpg"
img18="https://telegra.ph/file/ecf39ad8bf915c32c4474.jpg"
img19="https://telegra.ph/file/0e8d6f8168f0984b4721c.jpg"
img20="https://telegra.ph/file/05a419bc6ef5d47a06f78.jpg"
img21="https://telegra.ph/file/c68c9b093f44389bcc9dc.jpg"
img21="https://telegra.ph/file/91ef6c3a2283982f239ee.jpg"
img22="https://telegra.ph/file/e9a8a17f88c5d39640053.jpg"
img23="https://telegra.ph/file/743fd959d013b5b38fc6f.jpg"
img24="https://telegra.ph/file/8dffcae0126279bac028a.jpg"
img25="https://i7.fnp.com/assets/images/custom/quotes/diwali/diwali-greetings.jpg"
img26="https://telegra.ph/file/83ca3250b076e68e9ebb8.jpg"
img27="https://telegra.ph/file/d6cc1f10694b26ba73dbe.jpg"
img28="https://telegra.ph/file/b64482b55a8011d296673.jpg"
img29="https://telegra.ph/file/5de159c63a7a2de962a01.jpg"
img30="https://telegra.ph/file/353d27597ddb8e21d3679.jpg"
img31="https://telegra.ph/file/fa96e6c4815b3772330f0.jpg"
img32="https://telegra.ph/file/8d7ace0417c6837865cd4.jpg"
img33="https://telegra.ph/file/f1ce784104db3d03422a4.jpg"
img34="https://telegra.ph/file/a845e24a11e39169dd323.jpg"
img35="https://telegra.ph/file/5527d218cc76c0603ee78.jpg"
img36="https://telegra.ph/file/96bfacdb9db24a8682cc1.jpg"
img37="https://telegra.ph/file/bc7b766eb321e409d4bc5.jpg"
img38="https://telegra.ph/file/fde0870325e0ac48a131e.jpg"
img39="https://telegra.ph/file/c40a3de3538ca186de05b.jpg"
img40="https://telegra.ph/file/9a23660f94779ed25bd1c.jpg"
img41="https://telegra.ph/file/505a2b74bda2e5adb8c8f.jpg"
img42="https://telegra.ph/file/d3fda2122b19edd90c847.jpg"
img43="https://telegra.ph/file/ff204c70291aa571fd123.jpg"
img44="https://telegra.ph/file/e22f2fe82d2b3a77eb4d0.jpg"
img45="https://telegra.ph/file/13522910629341b28a0fc.jpg"
img46="https://telegra.ph/file/40e8ad8246a0e2f43edfd.jpg"
img47="https://telegra.ph/file/20a82ea3f4241062fccd5.jpg"
img48="https://telegra.ph/file/4193fcf9ee25b6dc242c2.jpg"
img49="https://telegra.ph/file/e93f9f38efee5cb06375d.jpg"
img50="https://telegra.ph/file/cce22da529e5c3f7c683a.jpg"
img51="https://telegra.ph/file/96998cc2e5350444dfce0.jpg"
img52="https://telegra.ph/file/741542b31383f5d4af9cb.jpg"
img53="https://telegra.ph/file/31913a7c61fdbdb2f29e4.jpg"
img54="https://telegra.ph/file/13d133fe6b097908510d2.jpg"
img55="https://telegra.ph/file/76c359e93f652e57cd30a.jpg"
img56="https://telegra.ph/file/36d22f6278252ba87049f.jpg"
img57="https://telegra.ph/file/735cc74229aa9a0523a00.jpg"
img58="https://telegra.ph/file/470e96225096021ffa60c.jpg"
img59="https://telegra.ph/file/95715b15d18b8b33163ee.jpg"
img60="https://telegra.ph/file/efd418360d5319a828508.jpg"

# TEXT COLLECTION
txt1="`Don’t Act Mean, Go Green. Celebrate An Eco Friendly Diwali This Year.`"
txt2="`Let This Diwali Burn All Your Bad Times, Celebrate An Eco-Friendly Diwali!`"
txt3="`Paying respects to the gods, and decorating for them the Thali, this is what the occasion is all about, this is the spirit of Deepavali.`"
txt4="`Light a lamp of love! Blast a chain of sorrow! Shoot a rocket of prosperity! Fire a flowerpot of happiness! Wish you and your family SPARKLING DIWALI`"
txt5="`May the joy, cheer, mirth and merriment of this divine festival surround you forever. May the happiness, which this Deepavali season brings lasts forever.`"
txt6="`Doubt is like darkness, Trust is like light, There is no way to destroy light by throwing darkness in to it. So come together and enjoy the festival of lights.`"
txt7="`May the warmth and splendor, that are a part of this auspicious occasion, fill your life with happiness and bright cheer, and bring to you joy and prosperity, for the whole year.`"
txt8="`May this Diwali bring you the utmost in peace and prosperity. May lights triumph over darkness. May peace transcend the earth. May the spirit of light illuminate the world. May the light that we celebrate at Diwali show us the way and lead us together on the path of peace and social harmony. Wishing everyone a very Happy Diwali.`"
txt9="`All the lights of the world cannot be compared even to a ray of the inner light of the self. Merge yourself in this light and enjoy the festival of lights.`"
txt10="`May the supreme light illumine your minds, enlighten your hearts and strengthen the human bonds in your homes and communities.`"
txt11="`A warm Diwali wish for every happiness. May the warmth and splendour, that are a part of this auspicious occasion, fill your life with happiness and bright cheer, and bring to you joy and prosperity, for the whole year.`"
txt12="`May this Diwali bring universal compassion, the Inner joy of peace and love and the awareness of oneness to all.`"
txt13="`May this Diwali Endow you with opulence and prosperity Happiness comes at your steps Wishing you a bright future in your life`"
txt14="`An occasion to celebrate victory over defeat, light over darkness, awareness over ignorance, an occasion to celebrate life. May this auspicious occasion light up your life with happiness, joy and peace this Diwali.`"
txt15="`Candles to enjoy life; Decorations to light life; Presents to share success; Fire Crackers to burn evils; Sweets to sweeten success, And worship to thank god! Wish you a joyous and prosperous Diwali!`"
txt16=f"`May this festival of lights bring peace, prosperity and happiness to all. HAPPY DEEPAVALI.🎁🎇🎉🎆🎊✨`\n\n By {ALIVE_NAME}"
txt17="`May The Beauty Of Deepavali Season Fill Your Home With Happiness, And May The Coming Year Provide You With All That Bring You Joy!`"
txt18="`Have a wonderful Diwali and enjoy the festival of lights.May God bless you all and keep you in good health and spirits always.`"
txt19="`Happy Diwali to all people around the world. Be safe and have a environmental friendly Diwali.`"
txt20="`Let's make this Diwali joyous and bright,\nLet's celebrate in true sense this festival of light.\nHappy Diwali`"
txt21="`Wishing you a happy Diwali`"
txt22="`Let's celebrate the festival in the true sense by spreading joy and light up the world of others. Have a happy, safe and blessed Diwali!!`"
txt23="`Happy DIWALI to Everyone`"
txt24="`Happy DEEPAWALI to ALL My Friends and Family`"
txt25="`May This DIWALI bring Lots of Happiness and Joy in Your Life`"
txt26="`Sending love and light this Diwali and every single day.\nHope you’re having a bright and wonderful celebration.`"
txt27="`May this Diwali, come up with Fresh hopes, bright days and new dreams,\nWishing you and your family a very happy Diwali!`"
txt28="``","`May your life be filled with colours of happiness.\nHave a happy and safe Diwali!`"
txt29="`Let each diya you light bring a glow of happiness on your face and enlighten your soul.`\n**Happy Diwali!**"
txt30="`May every candle that will be lit on the evening of Diwali bring joys and prosperity for everyone.`"
txt31="`May you get prosperity and fortune on this auspicious and precious occasion of Diwali.`"
txt32="`Wishing the goodness of this festive season dwells within you and stays throughout the year. Happy Diwali!!`"
txt33="`May you make beautiful moments this Diwali which will be treasured by you and family forever. Have a blessed Diwali!!`"
txt34="`On this auspicious occasion,\nMay joy, prosperity, and happiness\nIlluminate your life and your home.\nWishing you a Happy Diwali`"
txt35=f"`Happiness is in the air\nIts Diwali everywhere\nLets show some love and care\nAnd wish everyone out there\n`**Happy Diwali!! by {ALIVE_NAME}"
txt36="Peace, prosperity and good fortune, May all this be with you in the coming years.\n\nHappy Diwali!"
txt37="आप सभी को दिवाली की ढेरो बधाई!","प्रेम की फुलझड़ी से आपका घर आँगन रोशन हो\nआपको दिवाली की हार्दिक शुभकामनाए"
txt38="दिवाली के शुभ अवसर पर आप सबको हार्दिक शुभकामनाए"
txt39="आपके घर में सदा सुख संमृद्धि बनी रहे!\nशुभ दीपावली!"

stark=random.choice([txt6,txt7,txt8,txt9,txt10])
mac=random.choice([txt11,txt12,txt13,txt14,txt15,txt16])
serve=random.choice([txt17,txt18,txt19,txt20,txt21,txt22])
mental=random.choice([txt23,txt24,txt25,txt26,txt27,txt17])
pm=random.choice([txt28,txt29,txt30,txt23])
opeo=random.choice([txt31,txt32,txt33,txt34,])
hmm=random.choice([txt36,txt37,txt38,txt39,txt1,txt12,txt20])
water=random.choice([mac,serve,opeo,hmm,stark,pm])

@borg.on(admin_cmd(pattern="hdiwali", outgoing=True))
async def hmm(event):
    await event.delete()
    x=random.randrange(1,60)
    if x==1:
        await borg.send_file(event.chat_id,file=img1,caption=txt1)
    if x==2:
        await borg.send_file(event.chat_id,file=img2,caption=txt2)
    if x==3:
        await borg.send_file(event.chat_id,file=img3,caption=txt3)
    if x==4:
        await borg.send_file(event.chat_id,file=img4,caption=txt4)
    if x==5:
        await borg.send_file(event.chat_id,file=img5,caption=txt5)
    if x==6:
        await borg.send_file(event.chat_id,file=img6,caption=stark)
    if x==7:
        await borg.send_file(event.chat_id,file=img7,caption=stark)
    if x==8:
        await borg.send_file(event.chat_id,file=img8,caption=stark)
    if x==9:
        await borg.send_file(event.chat_id,file=img9,caption=stark)
    if x==10:
        await borg.send_file(event.chat_id,file=img10,caption=stark)
    if x==11:
        await borg.send_file(event.chat_id,file=img11,caption=stark)
    if x==12:
        await borg.send_file(event.chat_id,file=img12,caption=mac)
    if x==13:
        await borg.send_file(event.chat_id,file=img13,caption=mac)
    if x==14:
        await borg.send_file(event.chat_id,file=img14,caption=mac)
    if x==15:
        await borg.send_file(event.chat_id,file=img15,caption=mac)
    if x==16:
        await borg.send_file(event.chat_id,file=img16,caption=mac)
    if x==17:
        await borg.send_file(event.chat_id,file=img17,caption=mac)
    if x==18:
        await borg.send_file(event.chat_id,file=img18,caption=mac)
    if x==19:
        await borg.send_file(event.chat_id,file=img19,caption=serve)
    if x==20:
        await borg.send_file(event.chat_id,file=img20,caption=serve)
    if x==21:
        await borg.send_file(event.chat_id,file=img21,caption=serve)
    if x==22:
        await borg.send_file(event.chat_id,file=img22,caption=serve)
    if x==23:
        await borg.send_file(event.chat_id,file=img23,caption=serve)
    if x==24:
        await borg.send_file(event.chat_id,file=img24,caption=serve)
    if x==25:
        await borg.send_file(event.chat_id,file=img25,caption=serve)
    if x==26:
        await borg.send_file(event.chat_id,file=img26,caption=mental)
    if x==27:
        await borg.send_file(event.chat_id,file=img27,caption=mental)
    if x==28:
        await borg.send_file(event.chat_id,file=img28,caption=mental)
    if x==29:
        await borg.send_file(event.chat_id,file=img29,caption=mental)
    if x==30:
        await borg.send_file(event.chat_id,file=img30,caption=mental)
    if x==31:
        await borg.send_file(event.chat_id,file=img31,caption=mental)
    if x==32:
        await borg.send_file(event.chat_id,file=img32,caption=mental)
    if x==33:
        await borg.send_file(event.chat_id,file=img33,caption=mental)
    if x==34:
        await borg.send_file(event.chat_id,file=img34,caption=mental)
    if x==35:
        await borg.send_file(event.chat_id,file=img35,caption=pm)
    if x==36:
        await borg.send_file(event.chat_id,file=img36,caption=pm)
    if x==37:
        await borg.send_file(event.chat_id,file=img37,caption=pm)
    if x==38:
        await borg.send_file(event.chat_id,file=img38,caption=pm)
    if x==39:
        await borg.send_file(event.chat_id,file=img39,caption=pm)
    if x==40:
        await borg.send_file(event.chat_id,file=img40,caption=pm)
    if x==41:
        await borg.send_file(event.chat_id,file=img41,caption=pm)
    if x==42:
        await borg.send_file(event.chat_id,file=img42,caption=pm)
    if x==43:
        await borg.send_file(event.chat_id,file=img43,caption=pm)
    if x==44:
        await borg.send_file(event.chat_id,file=img44,caption=pm)
    if x==45:
        await borg.send_file(event.chat_id,file=img45,caption=opeo)
    if x==46:
        await borg.send_file(event.chat_id,file=img46,caption=opeo)
    if x==47:
        await borg.send_file(event.chat_id,file=img47,caption=opeo)
    if x==48:
        await borg.send_file(event.chat_id,file=img48,caption=opeo)
    if x==49:
        await borg.send_file(event.chat_id,file=img49,caption=opeo)
    if x==50:
        await borg.send_file(event.chat_id,file=img50,caption=opeo)
    if x==51:
        await borg.send_file(event.chat_id,file=img51,caption=opeo)
    if x==52:
        await borg.send_file(event.chat_id,file=img52,caption=opeo)
    if x==53:
        await borg.send_file(event.chat_id,file=img53,caption=opeo)
    if x==54:
        await borg.send_file(event.chat_id,file=img54,caption=hmm)
    if x==55:
        await borg.send_file(event.chat_id,file=img55,caption=hmm)
    if x==56:
        await borg.send_file(event.chat_id,file=img56,caption=hmm)
    if x==57:
        await borg.send_file(event.chat_id,file=img57,caption=hmm)
    if x==58:
        await borg.send_file(event.chat_id,file=img58,caption=water)
    if x==59:
        await borg.send_file(event.chat_id,file=img59,caption=water)
    if x==60:
        await borg.send_file(event.chat_id,file=img60,caption=water)
    
    
@borg.on(admin_cmd(pattern="wdiwali",outgoing=True))
async def busy(event):
    trans=random.randrange(1,43)
    if trans==1:
        await event.edit(txt1)
    if trans==2:
        await event.edit(txt2)
    if trans==3:
        await event.edit(txt3)
    if trans==4:
        await event.edit(txt4)
    if trans==5:
        await event.edit(txt5)
    if trans==6:
        await event.edit(txt6)
    if trans==7:
        await event.edit(txt7)
    if trans==8:
        await event.edit(txt8)
    if trans==9:
        await event.edit(txt9)
    if trans==10:
        await event.edit(txt10)
    if trans==11: 
        await event.edit(txt11)
    if trans==12:
        await event.edit(txt12)
    if trans==13:
        await event.edit(txt13)
    if trans==14:
        await event.edit(txt14)
    if trans==15:
        await event.edit(txt15)
    if trans==16:
        await event.edit(txt16)
    if trans==17:
        await event.edit(txt17)
    if trans==18:
        await event.edit(txt18)
    if trans==19:
        await event.edit(txt19)
    if trans==20:
        await event.edit(txt20)
    if trans==21:
        await event.edit(txt21)
    if trans==22:
        await event.edit(txt22)
    if trans==23:
        await event.edit(txt23)
    if trans==24:
        await event.edit(txt24)
    if trans==25:
        await event.edit(txt25)
    if trans==26:
        await event.edit(txt26)
    if trans==27:
        await event.edit(txt27)
    if trans==28:
        await event.edit(txt28)
    if trans==29:
        await event.edit(txt29)
    if trans==30:
        await event.edit(txt30)
    if trans==31:
        await event.edit(txt31)
    if trans==32:
        await event.edit(txt32)
    if trans==33:
        await event.edit(txt33)
    if trans==34:
        await event.edit(txt34)
    if trans==35:
        await event.edit(txt35)
    if trans==36:
        await event.edit(txt36)
    if trans==37:
        await event.edit(txt37)
    if trans==38:
        await event.edit(txt38)
    if trans==39:
        await event.edit(txt39)
    if trans==40:
        await event.edit(f"Hope This Diwali Brings lots of Happiness and Joy in your life.**\n\nHappy Diwali** By **{ALIVE_NAME}**")
    if trans==41:
        await event.edit(f"Hope This Diwali Brings lots of Happiness and Joy in your life.**\n\nHappy Diwali** By **{ALIVE_NAME}**")
    if trans==42:
        await event.edit(f"Hope This Diwali Brings lots of Happiness and Joy in your life.**\n\nHappy Diwali** By **{ALIVE_NAME}**")
    if trans==43:
        await event.edit(f"Hope This Diwali Brings lots of Happiness and Joy in your life.**\n\nHappy Diwali** By **{ALIVE_NAME}**")
