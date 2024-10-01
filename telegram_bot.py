import asyncio
from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command

bot = Bot(token='8041950880:AAFXWTHO6MLZIp3Dm2XbmooH1RkFncSGJiU')
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message):
    await bot.send_message(message.chat.id, "Hello! Send Matrix in this chat and I can advise what to do with it!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
