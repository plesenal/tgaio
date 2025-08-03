import sqlite3 
import tokens as tk
from telebot import TeleBot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,KeyboardButton     # или в переменной markup=telebot.types.InlineKeyboardMarkup(markup=None)                                  
token= tk.nfq
bot = TeleBot(token)
name =None


@bot.message_handler(commands=['start'])
def start(message):
    conn=sqlite3.connect('prog.sql')           #покючение к указанному файлу
    cur =conn.cursor()                         #курсор


    cur.execute('CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50),pass varchar(50))') #Выполяемая команда
    conn.commit()  #синхронизация таблицы
    cur.close() # закрытие
    conn.close()
    bot.send_message(message.chat.id,'Регистрация (Введи имя)')
    bot.register_next_step_handler(message,user_name)
def user_name(message):
    global name #указываем на глобальную переменную а не внутренюю
    name= message.text.strip()
    bot.send_message(message.chat.id,'Введите пароль')
    bot.register_next_step_handler(message,user_pass)

def user_pass(message):
    passw= message.text.strip()

    conn=sqlite3.connect('prog.sql')
    cur =conn.cursor()
    cur.execute("INSERT INTO users(name,pass) VALUES('%s','%s')" %(name,passw)) #Передаём в таблицу имя и пороль пользователя (id - auto_increment(сам добавляется)) , %s-будет строка 
    conn.commit()
    cur.close()
    conn.close()


    markup=types.InlineKeyboardMarkup() 
    markup.add(types.InlineKeyboardButton('Пользователи', callback_data='list'))
    bot.send_message(message.chat.id,f'Регисрация закончена',reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    conn=sqlite3.connect('prog.sql')
    cur =conn.cursor()
    cur.execute('SELECT * FROM users')
    users=cur.fetchall()#Получаем данные из таблицы  / получаем все найденые записи 
    
    info= ''
    for el in users:
        info+=  f'Имя:{el[1]},Пароль:{el[2]}\n'
    
    
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)






bot.infinity_polling()