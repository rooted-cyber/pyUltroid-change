from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
import asyncio
async def leave_group(group_username):
    try:
        channel = await client.get_entity(group_username)
        await client(LeaveChannelRequest(channel))
        print(f"Successfully left the group: {group_username}")
    except Exception as e:
        print(f"Failed to leave the group: {e}")


async def msg(e,ab):
    await e.respond(ab)

async def downl(e):
    reply = await e.get_reply_message()
    await e.client.download_media(reply.media)


async def rp(e):
    reply = await e.get_reply_message()
