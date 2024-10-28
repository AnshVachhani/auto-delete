from pyrogram import Client, filters
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

API_ID = os.getenv("API_ID")  # Ensure your .env file has this value
API_HASH = os.getenv("API_HASH")  # Ensure your .env file has this value
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Ensure your .env file has this value
CHANNEL_ID = -1002206045192  # Update with your channel ID

app = Client("hello_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

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
