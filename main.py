
from pyrogram import Client, filters
import os
import asyncio
from pyrogram.enums import ChatMembersFilter

API_ID = "8012239"
API_HASH = "171e6f1bf66ed8dcc5140fbe827b6b08"
BOT_TOKEN = "8164925669:AAFrDltyWMahWLEtvnVbdx8-s1PjC-DpL8E"

CHANNEL_IDS = [-1002206045192]
GROUP_IDS = [-1002068352969, -1001930038276]

app = Client("ansh_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Welcome to the bot.")

@app.on_message(filters.chat(CHANNEL_IDS))
async def delete_channel_messages(client, message):
    try:
        await asyncio.sleep(5)  
        await message.delete()
        print(f"Deleted message from channel: {message.text}") 
    except Exception as e:
        print(f"Error deleting message from channel: {e}")

@app.on_message(filters.chat(GROUP_IDS))
async def delete_group_messages(client, message):
    try:
        await asyncio.sleep(6)
        await message.delete()
        print(f"Deleted message from group: {message.text}")
    except Exception as e:
        print(f"Error deleting message from group: {e}")
        


@app.on_message(filters.command("accept_requests"))
async def accept_requests(client, message):
    chat_id = message.chat.id
    user = message.from_user

    # Check if the user is an admin
    admin_ids = []
    
    async for admin in client.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS):
        admin_ids.append(admin.user.id)

    if user.id in admin_ids:
        # Fetch the pending requests (if your bot is an admin)
        pending_requests = await client.get_chat_members(chat_id, filter=ChatMembersFilter.RESTRICTED)

        for member in pending_requests:
            # Accept the request by promoting the member
            await client.promote_chat_member(
                chat_id=chat_id,
                user_id=member.user.id,
                can_change_info=True,
                can_post_messages=True,
                can_edit_messages=True,
                can_delete_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_video_chats=True,
            )
            print(f"Accepted request from {member.user.username} in chat {chat_id}")

        await message.reply("All pending requests have been accepted.")
    else:
        await message.reply("You are not an admin in this group.")


if __name__ == "__main__":
    app.run()
