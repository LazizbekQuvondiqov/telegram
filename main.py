# 7766954399:AAFvOWUcZvzR6Bkc1cb283woN8OH8ZGRWo4
from aiogram import Bot, Dispatcher,executor,types
from aiogram.types.web_app_info import WebAppInfo

bot=Bot('7766954399:AAFvOWUcZvzR6Bkc1cb283woN8OH8ZGRWo4')
dp=Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    markup=types.ReplyKeyboardMarkup()
    
    markup.add(types.KeyboardButton('Menu', web_app=WebAppInfo(url='https://134d-188-113-231-220.ngrok-free.app/telegram.html')))

    await message.answer('salom online magazinga xush kelibsiz',reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message:types.Message):
    await message.answer(message.web_app_data.data)





executor.start_polling(dp)