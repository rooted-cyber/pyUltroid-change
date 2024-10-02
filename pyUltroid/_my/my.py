from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from os import listdir as ls, remove as rm, mkdir, chdir as cd, rmdir
from ..fns.helper import bash
from ..startup.utils import load_addons

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
    rmdir("plugins-file")
    mkdir("plugins-file")
    d = "plugins-file"
    reply = await e.get_reply_message()
    na = reply.flile.name
    await e.client.download_media(reply.media,d)
    await msg(e,f"Download in `plugins-file/{na}`")


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
    rmdir("pic")
    mkdir("pic")
    d = "pic"
    r = await e.get_reply_message()
    if r:
      path = await e.client.download_profile_photo(r.sender_id,d)
      await e.reply(f"**Your profile pic**",file=path)
    else:
      path = await e.client.download_profile_photo("me",d)
      await e.reply(f"**My profile pic**",file=path)


