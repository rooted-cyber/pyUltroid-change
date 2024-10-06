from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from os import listdir as ls, remove as rm, mkdir, chdir as cd, rmdir, removedirs as rmd
from ..fns.helper import bash
from time import strftime as aj
from ..startup.utils import load_addons
import akenoai as ak
import json

def mythumb():
    mythumb = "resources/downloads/a.jpg"


async def leave_group(group_username):
    try:
        channel = await client.get_entity(group_username)
        await client(LeaveChannelRequest(channel))
        print(f"Successfully left the group: {group_username}")
    except Exception as e:
        print(f"Failed to leave the group: {e}")


async def msg(e,ab):
    await e.client.send_message(e.chat_id,f"{ab}")

async def dl(e):
    if "plugins-file":
        bb = ""
    else:
        mkdir("plugins-file")
    d = "plugins-file"
    reply = await e.get_reply_message()
    name = reply.file.name
    await e.client.download_media(reply.media,d)
    await msg(e,f"Download in `plugins-file/{name}`")


async def rp(e):
    await e.get_reply_message()

async def ins(e):
    r = await e.get_reply_message()
    if not r:
        return await msg(e,"`Reply any plugin.....`")
    else:
        await msg(e, "`Installing...`")
    nam = r.file.name
    await dl(e)
    #await e.reply(ls("."))
    await bash(f"cp {nam} ~/Te*d/Ul*/plu*")
    await bash(f"rm {nam}")
    load_addons(f"plugins/{nam}")
    if nam in ls("plugins"):
        await e.reply(f"successfully installed **{nam}**")


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

async def info(e):
    b = files=await dl(e)
    response = await ak.AkenoPlus(e).paal_see(f"{b}")
