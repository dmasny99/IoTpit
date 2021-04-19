import telebot
from telebot import types
import requests
import time
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import sqlite3




url = "https://sandbox.rightech.io/api/v1/objects/607d8d0ef03e460011b2e258/packets?begin=1618840870138&end=1618840910139"
token_RIC = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2MDdkMzIwYWYwM2U0NjAwMTFiMmRhNWUiLCJzdWIiOiI2MDQ5MGVjOTUzMDcyZWZjNGJmZDIyNjgiLCJncnAiOiI2MDQ5MGVjOTUzMDcyZWZjNGJmZDIyNjciLCJsaWMiOmZhbHNlLCJ1c2ciOiJhcGkiLCJmdWxsIjpmYWxzZSwicmlnaHRzIjoxLjUsImlhdCI6MTYxODgxNzU0NiwiZXhwIjoxNjIxMzcxNjAwfQ.MN77XEwaN7wrzkE0ZrYL-0LbsBqaQjMHpzYhxHVdUaY"
bot = telebot.TeleBot("1600352952:AAHLJS-qXvIs6-PmE-e1G8E7zZcTdSj_jlI")

@bot.message_handler(commands=['help'])
def get_text_messages(message):
        bot.send_message(message.from_user.id, "Я бот управления системой мониторинга здоровья.\nЯ умею строить графики физического состояния рабочего.\nНапишите мне /start" )

@bot.message_handler(commands=['start'])
def startup_menu(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('/get_stat','Отправить сообщение')
    bot.send_message(message.from_user.id,"Выберите действие",reply_markup=keyboard)

@bot.message_handler(commands=['get_stat'])
def stat_gatherer(message):
    conn = sqlite3.connect('health_data.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM health_monitor;")
    data = cur.fetchall()
    health_stat_array = np.array(data)
    pulse = np.asarray(health_stat_array[:,1]).reshape(-1,1)
    plt.plot(pulse)
    plt.savefig("pulse.png")
    blood_pressure = np.array(health_stat_array[:,2]).reshape(-1,1)
    print(blood_pressure)
    plt.plot(blood_pressure)
    plt.savefig("blood_pressure.png")
    saturation = np.array(health_stat_array[:,3]).reshape(-1,1)
    plt.plot(saturation)
    plt.savefig("saturation.png")
    bot.send_photo(message.from_user.id,photo=open("pulse.png","rb"))
    bot.send_photo(message.from_user.id,photo=open("blood_pressure.png","rb"))
    bot.send_photo(message.from_user.id,photo=open("saturation.png","rb"))

bot.polling(none_stop=True, interval=0)
    