from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest

async def leave_group(group_username):
    try:
        channel = await client.get_entity(group_username)
        await client(LeaveChannelRequest(channel))
        print(f"Successfully left the group: {group_username}")
    except Exception as e:
        print(f"Failed to leave the group: {e}")


async def msg(ab):
    await event.reply(ab)


def msg(ab):
    print(f"""
    {ab}
    """)


