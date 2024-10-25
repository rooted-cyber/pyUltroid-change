from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from os import listdir as ls, remove as rm, mkdir, chdir as cd, rmdir, removedirs as rmd
from ..fns.helper import bash, inline_mention
from ..fns.tools import get_paste
from time import strftime as aj
from ..startup.utils import load_addons
#import akenoai as ak
import json
from .. import *
from .. import bot
import requests

async def tag(event):
  reply = await event.get_reply_message()
  if reply:
    await event.respond(inline_mention(reply.sender))
  else:
    await event.respond(inline_mention(event.sender))
async def sp(e):
    a, b = await bash(f"""
sh -c "$(curl -fsSl https://gist.githubusercontent.com/rooted-cyber/6f47f4d7b3455dbe10556008515e0c9f/raw/speed)"
""")
    await e.reply(f"""
**Your speedtest result:**

`{a}`
""")

async def msg(e,ab):
    await e.client.send_message(e.chat_id,f"{ab}")

async def dl(e):
    if "plugins-file":
        bb = ""
    else:
        mkdir("plugins-file")
    reply = await e.get_reply_message()
    name = reply.file.name
    g = "plugins-file"
    await reply.download_media()
    await msg(e,f"**Download in** \n`plugins-file/{name}`")
    

async def photo(e):
    if "pic":
      h = ""
    else:
      mkdir("pic")
    d = "pic"
    r = await e.get_reply_message()
    if r:
      path = await e.client.download_profile_photo(r.sender_id)
      await e.reply(f"**Your profile pic**",file=path)
    else:
      path = await e.client.download_profile_photo("me")
      await e.reply(f"**My profile pic**",file=path)


async def cpp(e):
  c = await e.eor(f"`processing`")
  a,b = await bash(f"curl -L https://gist.githubusercontent.com/rooted-cyber/1bd2b7d3eb4d66ab06ab5e83098395e3/raw/cpp | bash")
  await msg(e,f"{a}")
    
    
async def pyc():
    load_addons(f"pyUltroid/_my/my.py")

async def tm(e,ab):
    await msg(e,aj(ab))

async def op(e):
    r = await e.get_reply_message()
    m = await r.download_media()
    with open(m) as b:
        d = b.read()
        await e.reply(f"""
        ```{d}```""",parse_mode="html")

async def join(pp):
    from telethon.tl.functions.channels import JoinChannelRequest
    i = f"pp"
    await bot(JoinChannelRequest(f"{i}"))


async def fm(e):
  reply = await e.get_reply_message()
  #ty = e.pattern_match.group(1).strip()
  if not reply:
    return await e.eor("not reply...", time=5)
  a = reply.sender  # await event.client.get_entity(rep)
  b = a.first_name
  l = a.last_name or ""
  u = ("@" + a.username) if a.username else "???"
  ph = a.phone
  fr = "First_name: ", "`",a.first_name,"`"
  las = "Last Name: ", "`",a.last_name,"`"
  pic = file=await photo(e)
  await reply.respond(f"{pic}\nFirst Name: `{b}`\nLast Name: `{l}`\nnUsername: `{u}`\nPhone: `+{ph}`\n\n{fr}\n{las}")
