"""Check if userbot awake or not . 
"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname


   ALIVE_PIC = "https://telegra.ph/file/fb10fea3d152e1524ef93.png"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "**🔱E.D.I.T.H. IS Awake🔱 \n\n\n**"
   ALIVE_MESSAGE += "`Program Status \n\n\n`"
   ALIVE_MESSAGE += f"`TELETHON VERSION: 6.0.9 \n\n`"
   ALIVE_MESSAGE += f"`Python: 3.7.4\n\n`"
   ALIVE_MESSAGE += f"`Edith OS : 3.14\n\n`"
   ALIVE_MESSAGE += "`I'll Be With my Master Till My Dyno Ends!!☠ \n\n`" 
   ALIVE_MESSAGE += f"`MY MASTER👑`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
