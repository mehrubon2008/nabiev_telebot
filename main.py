'''nabiev mehrubon '''

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
# Устанавливаем уровень логов
logging.basicConfig(level=logging.INFO)
# Создаем бота и диспетчер
bot = Bot(token='5841295660:AAGSAxxH62qF1-aG-vF5-yc4Ccb9qmmg1Qg')
dp = Dispatcher(bot)
# Обрабатываем команду /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Привет! я мехрубон.')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
###############################
