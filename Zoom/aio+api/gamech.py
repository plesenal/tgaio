import random

from aiogram import F,Bot,Dispatcher
from aiogram.filters import Command
from aiogram.types import Message,ContentType

from tokens import plc

bot = Bot(token=plc)
dp = Dispatcher()

lives = 5
def random_number() -> int:
    return random.randint(1,100)
@dp.message(Command(commands="start"))
async def start(message: Message):
    await message.answer('Теперь ты должен сыграть со мной в игру.\n'
                         'Если ты все таки хочешь узнать правила вызови /help'
                         ' , хотя тебе уже ничего не поможет.')
@dp.message(Command(commands="help"))
async def help(message: Message):
    await message.answer('Раз ты так хочешь узнать правила , расскажу: '
                         'Я загадаю тебе некое число (нак уж и быть ограничимся числами от 1 до 100)'
                         'А ты попытаешься его отгадать . У тебя есть ХЪ попыток , но ты конечно не сможешь его ')

if __name__ == '__main__':
    dp.run_polling(bot)