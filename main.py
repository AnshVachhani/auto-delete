from pyrogram import Client, filters
import os


API_ID = "8012239"
API_HASH = "171e6f1bf66ed8dcc5140fbe827b6b08"
BOT_TOKEN = "7877654567:AAFLDysG33pCVLnUqfMwgTfLcKDKBfv_taQ"

app = Client("hellos_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Welcome to the bot.")

if __name__ == "__main__":
    app.run()
