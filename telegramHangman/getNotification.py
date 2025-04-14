from telethon import TelegramClient, events
import asyncio

# import settings
import subprocess
import os

# Replace these with your own values
api_id = "your api id"
api_hash = "your api hash"
keyword = "/play hangman"

# contact = "me"
# Create the client
client = TelegramClient("notif", api_id, api_hash)
# settings.init


@client.on(events.NewMessage)
async def handler(event):
    if event.raw_text == keyword.lower():
        sender = await event.get_sender()
        sender_name = sender.phone
        print(f"Received keyword from {sender_name}: {event.raw_text}")
        os.environ["CONTACT"] = sender_name
        subprocess.run(
            [
                "python",
                "/home/raphael/Documents/code/python/hangman/hangmanTelegram.py",
            ],
            env=os.environ,
        )


async def main():
    print("Listening for messages...")
    await client.start()
    await client.run_until_disconnected()


# Run the client
asyncio.run(main())
