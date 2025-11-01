import logging
from aiogram import Bot , Dispatcher , executor , types
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()


logging.basicConfig(level=logging.INFO)
TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")





bot  = Bot(token=TELEGRAM_BOT_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=["start" , "help"])

async def command_Start_handler(messages : types.Message):
    await messages.reply("yo boi ")



if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        executor.start_polling(dp, skip_updates=True)
    finally:
        loop.close()


