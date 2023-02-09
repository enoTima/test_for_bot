from aiogram import Bot, Dispatcher, types, executor
import logging
import time
import gspread
import datetime

logging.basicConfig(filename="sample.log", level=logging.INFO)
API_TOKEN = '6131336099:AAFjWhsFH-FpQNoz8uzEQf1BuNf36YN7TL8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
sa = gspread.service_account(filename="serv_acc.json")
sh = sa.open("Осколки Е&Е")
wks = sh.worksheet("Аркуш4")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!")


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
    answer_list = message.text.split(' ')[1:]
    d = datetime.date.today()
    wks.append_row([f'{d.day}.{d.month}.{d.year}', message.from_user.id,
                    answer_list[2], answer_list[0], answer_list[1]])


if __name__ == "__main__":
    executor.start_polling(dp)
