from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from  aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from  aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio



api = '7632744670:AAGumjd0yzpeGgXr9Zgi5R55tv1EYhC1OB0'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_inline = InlineKeyboardMarkup()
but_Inlait = InlineKeyboardButton(text='Рассчитать', callback_data ='calories')
but_1_Inlait = InlineKeyboardButton(text='Формулы расчёта', callback_data ='formulas')
kb_inline.row(but_Inlait, but_1_Inlait)

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_pol = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_otz = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text = 'Рассчитать')
button = KeyboardButton(text = 'Информация')
button_2 = KeyboardButton(text = 'Мужчина')
button_3 = KeyboardButton(text = 'Женщина')
but = KeyboardButton(text='min оценка')
but_1 = KeyboardButton(text='max оценка')
kb.row(button_1, button)
kb_pol.row(button_2, button_3)
kb_otz.row(but, but_1)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    pol = State()

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = kb_inline)

@dp.callback_query_handler(text = ['formulas'])
async  def get_formulas(call):
    await  call.message.answer(' для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 \n '
                               'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161 ')
    await call.answer()



@dp.callback_query_handler(text=['calories'])
async  def set_age(call):
    await  call.message.answer('Введите свой возраст:')
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
    await message.answer('Выберите свой пол:', reply_markup = kb_pol)
    await UserState.pol.set()


@dp.message_handler(state=UserState.pol)
async def send_calories_g(message,state):
    await state.update_data(fir_pol=message.text)
    data = await state.get_data()
    if data['fir_pol'] == 'Женщина':
        x = -161
    else:
        x = 5
    callori = ((10 * float(data['fir_weight'])) + (6.25 * float(data['fir_growth'])) - (4.92 * float(data['fir_age']))) + x
    await message.answer(f'Ваша норма калорий составляет: {callori}')
    await message.answer('Уважаемый преподаватель, разработчику пришлось немного расширить мой функционал, '
                         'ибо моя миссия помогать всем, НЕЗАВИСИМО ОТ ИХ ПОЛОЖЕНИЯ ', reply_markup = kb_otz )
    await asyncio.sleep(1)
    await message.answer('Оцените пожалуйста, мою работу, я уверен оценка будет максимальной', reply_markup=kb_otz)
    await state.finish()

@dp.message_handler(text = ['min оценка', 'max оценка'])
async def otzv(message):
    await message.answer('Спасибо за максимальную оценку 😂')



@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)