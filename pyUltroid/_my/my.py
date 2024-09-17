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


async def msg(ab):
    await event.client.send_message(event.chat_id,ab)


def msg(ab):
    print(f"""{ab}""")


