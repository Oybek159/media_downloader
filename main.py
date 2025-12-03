from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import asyncio
import requests
import os

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher()



async def on_start_up(dispatcher: Dispatcher):
    await bot.send_message(chat_id="1125326118", text="Bot ishga tushdi")
    

async def main():
    dp.startup.register(on_start_up)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
