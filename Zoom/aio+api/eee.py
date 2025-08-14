from aiogram import Bot, Dispatcher ,F
from aiogram.filters import Command
from aiogram.types import Message , ContentType
from tokens import plc
bot=Bot(token=plc)
dp=Dispatcher()
@dp.message(Command(commands="start"))
async def start(message: Message):
    await message.answer('Bla bla bla ')

@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )
if __name__ == '__main__':
    dp.run_polling(bot)