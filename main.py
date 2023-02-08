from aiogram import Bot, Dispatcher, types, executor
import logging
import time

logging.basicConfig(filename="sample.log", level=logging.INFO)
API_TOKEN = '6131336099:AAFjWhsFH-FpQNoz8uzEQf1BuNf36YN7TL8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!")
    logging.info(f'id: {message.from_user.id}; '
                 f'full_name: {message.from_user.full_name}; '
                 f'time: {time.asctime()} {message.text}')


@dp.message_handler(commands=['help'])
async def adding_shards(message: types.Message):
    await message.answer('''разделы:
    башня: легкая, трудная;
    арена: обычная, групповая;
    КБ: 4, 5, 6;
    события, турниры;
    клан: тк, сундук, шоп;
    другое: подземелья, рынок, вход, миссии, задания, магазин''')


@dp.message_handler(commands=['add'])
async def adding_shards(message: types.Message):
    await message.answer(message.text.split(' ')[1:])

if __name__ == "__main__":
    executor.start_polling(dp)
