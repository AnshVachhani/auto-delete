
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
       


if __name__ == "__main__":
    app.run()
