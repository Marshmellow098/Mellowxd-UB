"""
custom riddle questions...
Syntax: .rdl
  inspired by : conversationqt.py
  made by : @Hacker_The_Unknown | Noob
  edited by : @Hacker_The_Unknown | Noob
  
  # KANG wITH CREDIT
"""


from telethon import events
import asyncio
import os
import sys
import random
from userbot.utils import admin_cmd



@borg.on(admin_cmd(pattern=r"rdl"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Selecting the best riddle for you...")
    await asyncio.sleep(2)
    x = random.randrange(1, 60)
    if x == 1:
        await event.edit(
            '`"What has hands but can not clap?"`')
    if x == 2:
        await event.edit(
            '`"If an electric train is traveling south, which way is the smoke going?"`')
    if x == 3:
        await event.edit(
            '`"A monkey, a squirrel, and a bird are racing to the top of a coconut tree. Who will get the banana first, the monkey, the squirrel, or the bird?"`')
    if x == 4:
        await event.edit('`"What can you hear but not touch or see?"`')
    if x == 5:
        await event.edit(
            '`"Sheets of paper that tell new stories each day.What is it?"`')
    if x == 6:
        await event.edit('`"I am milky white and scares people. What am I?"`')
    if x == 7:
        await event.edit(
            '`"What is the only chain we can eat?"`')
    if x == 8:
        await event.edit(
            '`"I am beautiful, up in the sky. I am magical, yet I cannot fly. To people I bring luck, to some people, riches. The boy at my end does whatever he wishes. What am I?"`')
    if x == 9:
        await event.edit('`"I can whistle, I can howl, I can scream, And I can whisper, But I do not speak. What am I?"`')
    if x == 10:
        await event.edit(
            '`"What does someone else have to take before you can get?"`')
    if x == 11:
        await event.edit(
            '`"What number do you get when you multiply all of the numbers on a telephone’s number pad?"`')
    if x == 12:
        await event.edit(
            '`"What do you call a witch that lives in the sand?"`')
    if x == 13:
        await event.edit(
            '`"I come in many shapes, sizes, and colors. I stick to many surfaces but I am, in fact, not sticky at all. What am I?"`')
    if x == 14:
        await event.edit('`"What kind of table has no legs?"`')
    if x == 15:
        await event.edit(
            '`"This type of food, which is a fungus, is often served on supreme pizza, in spaghetti and in a particular "cream of" style soup. What is it?"`')
    if x == 16:
      await event.edit('`"If you drop me I am sure to crack. But give me a smile and I will always smile back. What is it?"`')
    if x == 17:
        await event.edit(
            '`"I weaken all men for hours each day. I show you strange visions while you are away. I take you by night, by day take you back. None suffer to have me, but do from my lack."`')
    if x == 18:
        await event.edit('`"What is between heaven and earth?"`')
    if x == 19:
        await event.edit('`"A white horned symbol of purity and grace. What is it?"`')
    if x == 20:
        await event.edit('`"It speaks without a tongue, and listens without ears. What is it?"`')
    if x == 21:
        await event.edit(
            '`"I belong in the month of December, but not in any other month. What am I?"`')
    if x == 22:
        await event.edit(
            '`"What kind of men are always above board?"`')
    if x == 23:
        await event.edit(
            '`"Three men are on a boat. The boat sinks but only two people get their hair wet. Why?"`')
    if x == 24:
        await event.edit(
            '`"What has 13 hearts but no organs?"`')
    if x == 25:
        await event.edit(
            '`"Where can you find success before work?"`')
    if x == 26:
        await event.edit('`"Live-in relation or marriage, what do you prefer?"`')
    if x == 27:
        await event.edit('`"I am deaf, dumb and blind. But I am very shiny and always speak the truth. Who am I?"`')
    if x == 28:
        await event.edit(
            '`"I am transparent. You can see and feel me, but you cannot hold me. I always take the shape of my container. Who am I?"`')
    if x == 29:
        await event.edit('`"Adam is 13 years old in 1980. In 1985 he is 8 years old. How?"`')
    if x == 30:
        await event.edit('`"I am a six letter word. Subtract one letter and twelve will remain. Who am I?"`')
    if x == 31:
        await event.edit('`"I am a part of your body. You can hold me in your left hand but not in your right hand. Who am I?"`')
    if x == 32:
        await event.edit('`"I go around the world, but always stay in a corner."`')
    if x == 33:
        await event.edit(
            '`"When I am opened, I am U-shaped but when I am closed I am V-shaped. Who am I?"`')
    if x == 34:
        await event.edit(
            '`"Which room has no doors or windows?"`')
    if x == 35:
        await event.edit('`"How many times is the alphabet "a" used while writing the spelling of each number from 1 to 500?"`')
    if x == 36:
        await event.edit('`"I have a mouth but I can’t speak, I can run but I can’t walk. Who am I?"`')
    if x == 37:
        await event.edit('`"6   15   18   20   ?   =   FORTY. What number relplaces the question mark?"`')
    if x == 38:
        await event.edit(
            '`"We are 3 friends. Our product and our sum always give the same answer. Who are we?"`')
    if x == 39:
        await event.edit('`"When I get multiplied by any number the sum of the figures in the product is always me. Who I am?"`')
    if x == 40:
        await event.edit(
            '`"Find out the difference between 18°C and 64.4°F."`')
    if x == 41:
        await event.edit('`"I have one letter but my name is spelled with eight. What am I?"`')
    if x == 42:
        await event.edit('`"Swap one letter from each of the words "Right" and "Blight" to make two related words."`')
    if x == 43:
        await event.edit('`"I am a four letter word. I am an animal. You use me to call your dear ones. Who am I?"`')
    if x == 44:
        await event.edit(
            '`"You need to spend a night in a building where there is no power. There are three rooms in this building. On the door of each room there are three different signs. One says "Lions Inside - anyone goes inside becomes their supper", the second one says "Open the door and a machine gun starts firing" and the third one says "Electric Room - touch anything and you will die". Which room would you choose?"`')
    if x == 45:
        await event.edit('`"I am pronounced with only one letter but written with three letters. Two different letters are used to write me. My color varies from black, blue, green, brown, grey etc. Who am I?"`')
    if x == 46:
        await event.edit('`"I am in the beginning of sorrow and sadness. You will find me in happiness also. You will find me in sun and stars but not in moon. I am in summer and spring but not in fall or winter. Who am I?"`')
    if x == 47:
        await event.edit(
            '`"What can be imagine  but can’t be touched ??"`')
    if x == 48:
        await event.edit('`"What smells bad when living but smells good when dead ?"`')
    if x == 49:
        await event.edit('`"Which time of a day when written in capital letters reads the same from all the four sides?"`')
    if x == 50:
        await event.edit(
            '`"You can catch me but cannot throw me. Who am I?"`')
    if x == 51:
        await event.edit('`"When I get multiplied by any number, the sum of the figures in the product is always me. What am I?"`')
    if x == 52:
        await event.edit(
            '`"I can fill up an entire room and still not take up any space. Who am I?"`')
    if x == 53:
        await event.edit('`"I help you in fixing your appointments and important schedules. You use me everyday several times. Still you keep on changing me every month. Who am I?"`')
    if x == 54:
        await event.edit('`"I look like a pearl. Clouds are my grandparents. I am very delicate. I die as soon as anybody touches me. Who am I?"`')
    if x == 55:
        await event.edit(
            '`"I am an eight letter standard word used by almost everybody. If you take away two alphabets from me I will make a logical sequence. Who am I?"`')
    if x == 56:
        await event.edit('`"I am a two digit even number. I am a square of a number, and also a cube of another number. Who am I?"`')
    if x == 57:
        await event.edit(
          '`"I am a seven letter word. I am very heavy. Take away two letters from me and you will get 8. Take away one letter from me and you will get 80. Who am I?"`')

    if x == 58:
        await event.edit(
          '`"I am soft and transparent. I am so small that you can keep me on your fingers. I have no light but I help you to see the beautiful world. I improve your vision only when I come in contact with you. Who am I?"`')
    if x == 59:
        await event.edit('`"I have three wings. At times I have 4 wings but still I cannot fly. I can rotate but I can’t move from one place to other. People always relax in my company. Who am I?"`')
    if x == 60:
        await event.edit(
            '`"What can touch someone once and last them a lifetime?"`')
