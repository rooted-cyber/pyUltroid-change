from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from os import listdir as ls, remove as rm, mkdir, chdir as cd
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

async def dla(e):
    mkdir("plugins-file")
    cd("plugins-file")
    reply = await e.get_reply_message()
    await e.client.download_media(reply.media)
    await msg(e,f"Download in `plugins-file/{reply.file.name}`")


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
    mkdir("pic")
    cd("pic")
    r = await e.get_reply_message()
    if r:
      path = await e.client.download_profile_photo(r.sender_id)
      await e.reply(f"**Your profile pic**",file=path)
    else:
      path = await e.client.download_profile_photo("me")
      await e.reply(f"**My profile pic**",file=path)


async def await dl():
    await dla(e)

