from pyrogram import Client, filters
import os
import asyncio


API_ID = "8012239"
API_HASH = "171e6f1bf66ed8dcc5140fbe827b6b08"
BOT_TOKEN = "8164925669:AAFrDltyWMahWLEtvnVbdx8-s1PjC-DpL8E"
CHANNEL_ID = -1002206045192

app = Client("ansh_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Welcome to the bot.")

@app.on_message(filters.chat(CHANNEL_ID))
async def delete_channel_messages(client, message):
    try:
        await asyncio.sleep(5)  
        await message.delete()
        print(f"Deleted message: {message.text}") 
    except Exception as e:
        print(f"Error deleting message: {e}")
        
if __name__ == "__main__":
    app.run()
    print("Bot started...")
