import telebot
from telebot.types import InputMediaPhoto
from telebot import types
import requests
import time
import datetime
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
import sqlite3

object_id = "607de42bf03e460011b2ee2c"
token_RIC = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2MDdkMzIwYWYwM2U0NjAwMTFiMmRhNWUiLCJzdWIiOiI2MDQ5MGVjOTUzMDcyZWZjNGJmZDIyNjgiLCJncnAiOiI2MDQ5MGVjOTUzMDcyZWZjNGJmZDIyNjciLCJsaWMiOmZhbHNlLCJ1c2ciOiJhcGkiLCJmdWxsIjpmYWxzZSwicmlnaHRzIjoxLjUsImlhdCI6MTYxODgxNzU0NiwiZXhwIjoxNjIxMzcxNjAwfQ.MN77XEwaN7wrzkE0ZrYL-0LbsBqaQjMHpzYhxHVdUaY"
bot = telebot.TeleBot("1600352952:AAHLJS-qXvIs6-PmE-e1G8E7zZcTdSj_jlI")

def poster(object_id):
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer {}'.format(token_RIC)}
    url = "https://sandbox.rightech.io/api/v1/objects/{}/commands/visit_doctor".format(object_id)
    response = requests.post(url,params={"topic": "health/state/visit_doctor", "payload": "Посетите врача"},headers=headers)
    return response.text
def plotter(data,time,name):
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    plt.xticks( rotation=25 )
    ax=plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    ax.grid()
    if name == "pulse":
        color = 'green'
        title = "График изменения пульса"
        ylab = "Пульс"
        min_allowed = 50
        max_allowed = 200
        del_max = 10
        del_min = 10
    elif name == "blood_pressure":
        color = 'purple'
        title = "График изменения давления"
        ylab = "Давление"
        min_allowed = 90
        max_allowed = 160
        del_max = 10
        del_min = 10
    else:
        color = 'blue'
        title = "График изменения сатурации"
        ylab = "Сатурация"
        min_allowed = 75
        max_allowed = 100
        del_max = 10
        del_min = 10
    ax.hlines(max_allowed,time[0],time[-1],color = 'red')
    ax.hlines(min_allowed,time[0],time[-1],color = 'red')
    ax.set_title(title)
    plt.plot(time,data,color = color)
    plt.xlim([time[0],time[-1]])
    plt.ylim([min_allowed-del_min,max_allowed+del_max])
    plt.xlabel("Время")
    plt.ylabel(ylab)
    plt.savefig('{}.png'.format(name))
    plt.close(fig)

@bot.message_handler(commands=['help'])
def get_text_messages(message):
        bot.send_message(message.from_user.id, "Я бот управления системой мониторинга здоровья.\nЯ умею строить графики физического состояния рабочего.\nНапишите мне /start" )

@bot.message_handler(commands=['start'])
def startup_menu(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('Получить данные','Срочно посетить врача')
    bot.send_message(message.from_user.id,"Выберите действие",reply_markup=keyboard)

def stat_gatherer(message):
    conn = sqlite3.connect('health_data.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM health_monitor;")
    data = cur.fetchall()
    health_stat_array = np.array(data)
    health_stat_array = np.delete(health_stat_array,[0,1], axis = 0) # удаляю первые две строчки вне указанного временноего диапазона, они почему-то фантомно появлялись всегда
    pulse = np.asarray(health_stat_array[:,1])
    blood_pressure = np.array(health_stat_array[:,2])
    saturation = np.array(health_stat_array[:,3])
    dates=[datetime.datetime.fromtimestamp(ts) for ts in np.asarray(health_stat_array[:,4])]
    plotter(pulse,dates,"pulse")
    plotter(blood_pressure,dates,"blood_pressure")
    plotter(saturation,dates,"saturation")
    bot.send_media_group(message.from_user.id,[InputMediaPhoto(open("pulse.png","rb"),caption="Время отчета: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))),
                                          InputMediaPhoto(open("blood_pressure.png","rb")),
                                          InputMediaPhoto(open("saturation.png","rb"))])
@bot.message_handler(content_types=['text'])
def message_recieved(message):
    if message.text == "Получить данные":
        stat_gatherer(message)
    elif message.text == "Срочно посетить врача":
       bot.send_message(message.from_user.id,poster(object_id))
    else:
        bot.send_message(message.from_user.id,"Я Вас не понимаю")
bot.polling(none_stop=True, interval=0)
    