from pyrogram import Client
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize Pyrogram bot
app = Client("multi_channel_bot", bot_token=BOT_TOKEN)

# Load channels
with open("channels.txt", "r") as f:
    channels = [line.strip() for line in f if line.strip()]

# Load messages
with open("messages.txt", "r") as f:
    messages = [line.strip() for line in f if line.strip()]

# Auto-post function
def auto_post():
    with app:
        while True:
            for channel in channels:
                for msg in messages:
                    try:
                        app.send_message(chat_id=channel, text=msg)
                        print(f"Posted to {channel}: {msg}")
                        time.sleep(5)  # wait between messages
                    except Exception as e:
                        print(f"Failed to post to {channel}: {e}")
            print("Cycle complete. Waiting 1 hour...")
            time.sleep(3600)  # Wait 1 hour before next cycle

if __name__ == "__main__":
    auto_post()
