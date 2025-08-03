import requests
import json
import webbrowser
from telebot import TeleBot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,KeyboardButton
import datetime
token="7401970632:AAFPtN3K39ifOX17kgHNP9MXNyAFO20GKWA"
bot = TeleBot(token)
API='83503319d9ca4a74e210b37889c8758d'


res=' '
data=' '
city = ' '
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,f'Привет {message.from_user.first_name}!В каком ты городе ?')

@bot.message_handler(content_types=['text'])
def get_wheather(message):
    global data,res,city
    
    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data=json.loads(res.text)
    city = message.text.strip()
    if res.status_code == 200:
        
        print(data)
        temp=data['main']['temp']
        templ=data['main']['feels_like']
        desription=data['weather'][0]['main']
        markup  = types.InlineKeyboardMarkup()
        b1=types.InlineKeyboardButton("Минималная температура",callback_data='min')
        b2=types.InlineKeyboardButton("Максмальная температура",callback_data='max')
        b3=types.InlineKeyboardButton("Убрать",callback_data='delite')
        markup.row(b3)
        markup.row(b1,b2)
        bot.reply_to(message,f"Сейчас в городе {city}:\n{temp}градусов\n ощущается как:{templ} \n {desription}")
        bot.send_message(message.chat.id,f'Хочешь узнать что то еще?',reply_markup=markup)
        
    else:
        bot.reply_to(message,f"Не знаю такого города")


@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    global data,city,res
    temp_min=data['main']['temp_min']
    temp_max=data['main']['temp_max']
    if callback.data == 'delite':
        bot.delete_message(callback.message.chat.id,callback.message.message_id-1)
        bot.delete_message(callback.message.chat.id,callback.message.message_id-2)
        bot.delete_message(callback.message.chat.id,callback.message.message_id-3)
    elif callback.data  ==  'min':
        bot.edit_message_text(f'Минимальная температура в городе {city}:{temp_min}',callback.message.chat.id, callback.message.message_id)
    elif callback.data =='max':
        bot.answer_callback_query(callback_query_id=callback.id,text='hi', show_alert=True)
        bot.send_message(callback.message.chat.id,f'Максимальная температура:{temp_max}')        


bot.infinity_polling()