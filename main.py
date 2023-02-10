from aiogram import Bot, Dispatcher, types, executor
import logging
import gspread
import datetime

logging.basicConfig(filename="sample.log", level=logging.INFO)
API_TOKEN = '6131336099:AAFjWhsFH-FpQNoz8uzEQf1BuNf36YN7TL8'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
sa = gspread.service_account(filename="serv_acc.json")
sh = sa.open("Осколки Е&Е")
wks = sh.worksheet("Аркуш4")
loc = ''
det = ''
menu_but = types.InlineKeyboardButton(text="меню", callback_data="menu")
close_but = types.InlineKeyboardButton(text="❌ закрыть", callback_data="close")
blue_but = types.InlineKeyboardButton(text="💙 cиний", callback_data="add_blue")
void_but = types.InlineKeyboardButton(text="💜 войд", callback_data="add_void")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!")


@dp.message_handler(commands=['help'])
async def adding_shards(message: types.Message):
    pass


@dp.message_handler(commands=['add'])
async def adding_shards(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="башня", callback_data="tower"),
        types.InlineKeyboardButton(text="кб", callback_data="cb"),
        types.InlineKeyboardButton(text="арена", callback_data="arena"),
        types.InlineKeyboardButton(text="события и турниры", callback_data="events_tournament"),
        types.InlineKeyboardButton(text="клан", callback_data="clan"),
        types.InlineKeyboardButton(text="другое", callback_data="other"),
        close_but
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await message.answer("выбери раздел:", reply_markup=keyboard)


@dp.callback_query_handler(text='menu')
async def menu_shards(callback: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="башня", callback_data="tower"),
        types.InlineKeyboardButton(text="кб", callback_data="cb"),
        types.InlineKeyboardButton(text="арена", callback_data="arena"),
        types.InlineKeyboardButton(text="события и турниры", callback_data="events_tournament"),
        types.InlineKeyboardButton(text="клан", callback_data="clan"),
        types.InlineKeyboardButton(text="другое", callback_data="other"),
        close_but
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text='close')
async def close(callback: types.CallbackQuery):
    await callback.message.edit_text(text='вы ничего не добавили, до встречи.')


@dp.callback_query_handler(text='tower')
async def tower_shards(callback: types.CallbackQuery):
    global loc
    loc = 'tower'
    buttons = [
        types.InlineKeyboardButton(text="легкая", callback_data="normal"),
        types.InlineKeyboardButton(text="трудная", callback_data="hard"),
        close_but, menu_but
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await callback.message.edit_text(text='выберите башню: ', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text='arena')
async def arena_shards(callback: types.CallbackQuery):
    global loc
    loc = 'arena'
    buttons = [
        types.InlineKeyboardButton(text="обычная", callback_data="classic"),
        types.InlineKeyboardButton(text="групповая", callback_data="group"),
        close_but, menu_but
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await callback.message.edit_text(text='выберите арену: ', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text='cb')
async def cb_shards(callback: types.CallbackQuery):
    global loc
    loc = 'cb'
    buttons = [
        types.InlineKeyboardButton(text="4", callback_data="4cb"),
        types.InlineKeyboardButton(text="5", callback_data="5cb"),
        types.InlineKeyboardButton(text="6", callback_data="6cb"),
        close_but, menu_but
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    await callback.message.edit_text(text='выберите КБ: ', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text='clan')
async def clan_shards(callback: types.CallbackQuery):
    global loc
    loc = 'clan'
    buttons = [
        types.InlineKeyboardButton(text="ТК", callback_data="tc"),
        types.InlineKeyboardButton(text="сундук", callback_data="chest"),
        types.InlineKeyboardButton(text="шоп", callback_data="shop"),
        close_but, menu_but
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    await callback.message.edit_text(text='выберите активность клана: ', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text='other')
async def other_shards(callback: types.CallbackQuery):
    global loc
    loc = 'other'
    buttons = [
        types.InlineKeyboardButton(text="подземелья", callback_data="dange"),
        types.InlineKeyboardButton(text="рынок", callback_data="market"),
        types.InlineKeyboardButton(text="вход", callback_data="entrance"),
        types.InlineKeyboardButton(text="миссии", callback_data="missions"),
        types.InlineKeyboardButton(text="задания", callback_data="tasks"),
        types.InlineKeyboardButton(text="магазин", callback_data="store"),
        close_but, menu_but
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    await callback.message.edit_text(text='выберите другие активности: ', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text='events_tournament')
async def events_tournament_shards(callback: types.CallbackQuery):
    global loc
    loc = 'events_tournament'
    buttons = [
        types.InlineKeyboardButton(text="события", callback_data="event"),
        types.InlineKeyboardButton(text="турниры", callback_data="tournament"),
        close_but, menu_but
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await callback.message.edit_text(text='выберите турнир или событие: ', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text=['chest', 'dange', 'market'])
async def blue(callback: types.CallbackQuery):
    global det
    det = callback.data
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(blue_but)
    keyboard.row(close_but, menu_but)
    await callback.message.edit_text(text='выберите осколок: ', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text=['normal', '4cb', 'entrance'])
async def blue_void(callback: types.CallbackQuery):
    global det
    det = callback.data
    buttons = [
        blue_but, void_but,
        close_but, menu_but
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await callback.message.edit_text(text='выберите осколок: ', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text=['hard', 'classic', 'group', '5cb', '6cb', 'tc',
                                 'missions', 'tasks', 'store', 'event', 'tournament'])
async def blue_void_sacral(callback: types.CallbackQuery):
    global det
    det = callback.data
    buttons = [
        blue_but, void_but,
        types.InlineKeyboardButton(text="💛 сакрал", callback_data="add_sacral"),
        close_but, menu_but
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    await callback.message.edit_text(text='выберите осколок: ', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text='shop')
async def void(callback: types.CallbackQuery):
    global det
    det = callback.data
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.row(void_but)
    keyboard.row(close_but, menu_but)
    await callback.message.edit_text(text='выберите осколок: ', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text=['add_blue', 'add_sacral', 'add_void'])
async def add_shard(callback: types.CallbackQuery):
    shard = callback.data.split('_')
    d = datetime.date.today()
    wks.append_row([f'{d.day}.{d.month}.{d.year}', callback.from_user.id, shard[1], loc, det])
    await callback.message.edit_text(text=f'вы добавили {shard[1]} шард, {loc}, {det}')



if __name__ == "__main__":
    executor.start_polling(dp)
