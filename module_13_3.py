from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7632744670:AAGumjd0yzpeGgXr9Zgi5R55tv1EYhC1OB0'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())



@dp.message_handler(text = ['Привет'])
async def urban_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

@dp.message_handler(commands = ['start'])
async  def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
    await message.answer(f'Ошибка, я не такой умный чтобы отвечать на вопрос: "{message.text}"')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)