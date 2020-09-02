import asyncio

from telethon import events

from userbot.utils import admin_cmd


@borg.on(admin_cmd("edithin"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "Read This Telegraph Whole info here":
    await event.edit("Hello ")
    animation_chars = [
        "`Verifying user...`",
        "`Connecting to TeamAtulsat...`",
        "Data Downloaded sucessfuly...`\n\n `Userbot :` **E.D.I.T.H.**\n `About Userbot:`Even Dead, I'm The Hero (E.D.I.T.H.) is an augmented reality security, defense and artificial tactical intelligence system created by TeamAtul` __Based upon Spider man's A.I.__ \n\n `Connected to sat : TeamAtulsat`\n`TeamAtulsat version : v.2.2.5` \n `Edith OS : 3.1.4`\n Creator : **©ᴛᴇᴀᴍᴀᴛᴜʟ™**\n",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
