from pyrogram import Client, filters
import os


API_ID = os.getenv("21684037")
API_HASH = os.getenv("cc4dda353688d66c94af69ca48a87bdb")
BOT_TOKEN = os.getenv("8164925669:AAFrDltyWMahWLEtvnVbdx8-s1PjC-DpL8E")

app = Client("hello_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Welcome to the bot.")

if __name__ == "__main__":
    app.run()
