import webbrowser
from telebot import TeleBot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,KeyboardButton
token="6832627417:AAE-9VLTn5o-HGU4YFIGt1JG_P6mq9NNTPc"
bot = TeleBot(token)

#  @bot.message_handler(func=lambda message:)

#     bot.reply_to(message,text=f"Привет, {message.from_user.first_name}")


# bot.infinity_polling()#программа рвботает постоянно 
# @bot.message_handler(commands=["start"])
# def main(message):
#     print(message)
#     print(type(message))
#     bot.send_message(message.chat.id,text=f"Привет,{message.from_user.first_name} ")

@bot.message_handler(commands=["site"])
def site(message):
    webbrowser.open("https://www.youtube.com")

@bot.message_handler(commands=["start"])
def send_welcome(message):  
    print(message)
    markup = ReplyKeyboardMarkup(row_width=3)
    bt1,bt2,bt3=KeyboardButton('🖼️'),KeyboardButton('🎵'),KeyboardButton('📽️')
    markup.row(bt1,bt2,bt3)
    bot.send_message(message.chat.id,text=f"Привет,  {message.from_user.first_name}",reply_markup=markup)
    bot.register_next_step_handler(message,on_click)
def on_click(message):
    if message.text =='🖼️':
        photo=open('./1/number1.png','rb')
        bot.send_photo(message.chat.id,photo)
        #bot.send_message(message.chat.id,text=f"1")
    elif message.text =='🎵':
        sound=open('./1/2z.mp3','rb')
        bot.send_audio(message.chat.id,sound)
        # bot.send_message(message.chat.id,text=f"2")
    elif message.text =='📽️':
        video=open('./1/SampleVideo.mp4','rb')
        bot.send_video(message.chat.id,video)
        # bot.send_message(message.chat.id,text=f"3")

@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(message.chat.id,text=f"i can't help you")


@bot.message_handler(content_types=['photo','video', 'audio', 'document'])
def get_file(message):
    markup  = types.InlineKeyboardMarkup()
    b1=types.InlineKeyboardButton("Ют",url="https://www.youtube.com")
    b2=types.InlineKeyboardButton("Убрать",callback_data='delite')
    b3=types.InlineKeyboardButton("Изменить",callback_data='edit')
    markup.row(b1)
    markup.row(b2,b3)
    bot.reply_to(message,"Зачем...",reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    if callback.data == 'delite':
        bot.delete_message(callback.message.chat.id,callback.message.message_id-1)
    elif callback.data  ==  'edit':
        bot.edit_message_text('///',callback.message.chat.id, callback.message.message_id)


@bot.message_handler()
def info(message):
    if message.text.lower()=='привет':
        bot.send_message(message.chat.id,text=f"Привет,{message.from_user.first_name} ")
    elif message.text.lower()=='id':
        bot.reply_to(message=message,text=f"ID:{message.from_user.id}")
bot.infinity_polling()