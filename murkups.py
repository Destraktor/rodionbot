from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import callback_data

main = InlineKeyboardMarkup(row_width=2)
upom = InlineKeyboardButton(text='Вызвать', callback_data='upom')
upo = InlineKeyboardButton(text='Вызвать 2', callback_data='upo')
main.insert(upo)
main.insert(upom)


