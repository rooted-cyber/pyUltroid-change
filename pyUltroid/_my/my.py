from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from os import listdir as ls, remove as rm, mkdir, chdir as cd, rmdir, removedirs as rmd
from ..fns.helper import bash
from time import strftime as aj
from ..startup.utils import load_addons
#import akenoai as ak
import json
import requests

def rq(url):
    requests.get(url)
async def msg(e,ab):
    await e.client.send_message(e.chat_id,f"{ab}")

async def rif(e,ac):
    r = await e.get_reply_message()
    if r:
        print(f"{ac}")
async def relse(e,ad):
    r = await e.get_reply_message()
    if not r:
        print(f"{ad}")

async def leave_group(group_username):
    try:
        channel = await client.get_entity(group_username)
        await client(LeaveChannelRequest(channel))
        print(f"Successfully left the group: {group_username}")
    except Exception as e:
        print(f"Failed to leave the group: {e}")

async def dl(e):
    await rif(e,"hi")
    await relse(e,"ni")
    if "plugins-file":
        bb = ""
    else:
        mkdir("plugins-file")
    reply = await e.get_reply_message()
    name = reply.file.name
    g = "plugins_file"
    await e.client.download_media(reply.media,g)
    await msg(e,f"Download in \n`plugins-file/{name}")
    

async def photo(e):
    if "pic":
      h = ""
    else:
      mkdir("pic")
    d = "pic"
    r = await e.get_reply_message()
    if r:
      path = await e.client.download_profile_photo(r.sender_id,d)
      await e.reply(f"**Your profile pic**",file=path)
    else:
      path = await e.client.download_profile_photo("me",d)
      await e.reply(f"**My profile pic**",file=path)


async def cpp(e):
  c = await e.eor(f"`processing`")
  a,b = await bash(f"curl -L https://gist.githubusercontent.com/rooted-cyber/1bd2b7d3eb4d66ab06ab5e83098395e3/raw/cpp | bash")
  await msg(e,f"{a}")
    
    
async def pyc():
    load_addons(f"pyUltroid/_my/my.py")

async def tm(e,ab):
    await msg(e,aj(ab))

async def open(e):
    r = await e.get_reply_message()
    with open(r) as b:
        d = b.read()
        await e.reply(<pre>d</pre>,parse_mode="html")
