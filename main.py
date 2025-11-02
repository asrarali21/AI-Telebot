import logging
from aiogram import Bot , Dispatcher , executor , types
import os
import asyncio
from dotenv import load_dotenv
from google import genai

load_dotenv()

class prevRefrence :
    def __init__(self):
        self.response = ""
    
    def store_memory(self, text: str) -> None:  # ✅ Accept text parameter
        self.response = text  # ✅ Store the text




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
async def send_messages(message: types.Message):
      


    user_text = message.text
    
    response = chat.send_message(message=user_text)
    
    answer = response.text
    reference.store_memory(answer)
    print(f"AI Response: {reference.response}")

    await message.reply(reference.response)




if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        executor.start_polling(dp, skip_updates=True)
    finally:
        loop.close()
    





