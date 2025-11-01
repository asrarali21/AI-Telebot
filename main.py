import logging
from aiogram import Bot , Dispatcher , executor , types
import os
import asyncio
from dotenv import load_dotenv
from google import genai

load_dotenv()

class prevRefrence :
    def storememory(self) -> None:
        self.reference  = ""




logging.basicConfig(level=logging.INFO)
TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")

bot  = Bot(token=TELEGRAM_BOT_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])

async def Start_message(messages: types.Message):
   
    await messages.reply("Hi How can i assist You")


GOOGLE_API_KEY= os.getenv("GOOGLE_AI_APIKEY")

client = genai.Client(api_key=GOOGLE_API_KEY)

chat = client.chats.create(model="gemini-2.5-flash")





reference = prevRefrence()

@dp.message_handler()
async def send_messages(messages : types.Message):
    await messages.answer("hi helllo boi")










if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        executor.start_polling(dp, skip_updates=True)
    finally:
        loop.close()
    





