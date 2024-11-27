from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from  aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
@dp.message_handler(commands=['Calories'])
async  def set_age(message):
    await  message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(fir_age = message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(fir_growth = message.text)
    data = await state.get_data()
    await  message.answer('Введите свой вес:')
    await  UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(fir_weight = message.text)
    data = await state.get_data()
    callori = (10 * float(data['fir_weight'])) + (6.25 * float(data['fir_growth'])) - (4.92 * float(data['fir_age'])) - 161
    await message.answer(f'Ваша норма калорий составляет: {callori}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)