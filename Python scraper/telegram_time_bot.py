import time
import asyncio
from telegram import Bot
import config

BOT_TOKEN = config.BOT_TOKEN
CHAT_ID = config.CHAT_ID2

async def send_time(bot):
    current_time = time.strftime("%H:%M:%S")
    await bot.send_message(chat_id=CHAT_ID2, text=f"Current time: {current_time}")

async def main():
    bot = Bot(token=BOT_TOKEN)
    await send_time(bot)

if __name__ == "__main__":
    asyncio.run(main())

