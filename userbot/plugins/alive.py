"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# IMG CREDITS: @WhySooSerious
import asyncio

from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd

from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/fb10fea3d152e1524ef93.png"
pm_caption = "`E.D.I.T.H. IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `piro`\n"
pm_caption += "**Edith OS** : `3.14`\n"
pm_caption += "**Current Sat** : `TeamAtulSat-2.25`\n"
pm_caption += f"**My Master** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "**License** : [MIT Licence](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"
pm_caption += "Copyright : By [TeamAtul@Github](GitHub.com/TeamAtul)\n"
pm_caption += " [Deploy EdithUserbot](https://telegra.ph/FRIDAY-06-15)"


# @command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
