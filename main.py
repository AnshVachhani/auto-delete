
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize the user client (you) and the bot client
user_client = Client("user_account", api_id="28623575", api_hash="38defc75e5be3b8b50821b7faa525e34")
bot_client = Client("bot_account", bot_token="7877654567:AAFLDysG33pCVLnUqfMwgTfLcKDKBfv_taQ")

async def approve_join_requests(chat_id):
    async with user_client, bot_client:
        # Fetch pending join requests
        join_requests = await user_client.get_chat_join_requests(chat_id)
        
        # Approve each request
        for request in join_requests:
            user_id = request.user.id
            print(f"Approving join request for user {user_id}")
            await bot_client.approve_chat_join_request(chat_id, user_id)
            await asyncio.sleep(1)  # Add a small delay to avoid rate limits

# Command handler for the bot
@bot_client.on_message(filters.command("accept") & filters.group)
async def start_approving_requests(client: Client, message: Message):
    chat_id = message.chat.id
    await message.reply("Starting to approve join requests...")
    await approve_join_requests(chat_id)
    await message.reply("All pending join requests approved!")


    
if __name__ == "__main__":
    user_client.start()
    bot_client.run()
