from aiogram import Dispatcher, Bot, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import murkups as nav
bot = Bot(token='6173994553:AAHwhPmLW0TLMpIkJ9zOHtbkGOFbmHxr_aw')
dp = Dispatcher(bot)


@dp.message_handler(commands=["упомянуть"])
async def start(message: types.Message):
    await message.answer("Тыкните", reply_markup=nav.main)

@dp.callback_query_handler(text='upom')
async def upominanie(call):
    await bot.send_message(call.message.chat.id, text="@zxcblemish\n"
                         "@crezbo\n"
                         "@Ryderif\n"
                         "@Sataxs\n"
                         "@dobroseems\n"
                         "@Imagine_if_i_havent_been_drunk\n"
                         "@pdvsfrt\n"
                         "@dnllbz\n"
                         "@Keyko_Mi\n")

@dp.callback_query_handler(text='upo')
async def upominanie(call):
    await bot.send_message(call.message.chat.id, text="@kh6m1d7l1n\n"
                         "@trxilblazer\n"
                         "@KaLiNkA_77\n"
                         "@krabik14\n"
                         "@diiddoq\n"
                         "@DenisAeges\n"
                         "@Sanek_Burwar\n"
                         "@maxxxikuwu\n"
                         "@PhillGver\n")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, fast=True)
