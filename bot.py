import telebot
from telebot import types
import config

bot = telebot.TeleBot("5935619902:AAGhYmz-dGcnTme7syYQaDpF9w5LbbCHUHk")

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
	bot.reply_to(message, "Привіт друже, ти придбав курс ІТ на хлопський розум, в цьому боті ти будеш отримувати завдання від нас. Чекай на перше завдання ;)" '/n' "Якщо у тебе виникли питаня напиши в чат (Потрібна допомога)")

##################################  Показуєтся при вході в бота  ################################################

@bot.message_handler(content_types=['text'])
def helps_btn(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Потрібна допомога")
    markup.add(btn1)
    
    if(message.text == "Потрібна допомога"):
        bot.send_message(message.chat.id, text="Привіт, якщо потребуєш допомоги напиши до @e_serhii ")
    elif(message.text == "Головне меню"):
        bot.send_message(message.chat.id, text="Ти в головному меню, що будемо робити: ")
    else:
        bot.send_message(message.chat.id, text="Я такої команди не знаю, спробуй щось інне ;) ")

#################################################################################################################

def helped(message):
    if(message.text == "Потрібна допомога"):
        bot.send_message(message.chat.id, text="Привіт, якщо потребуєш допомоги напиши до @e_serhii ")
    elif(message.text == "Головне меню"):
        bot.send_message(message.chat.id, text="Ти в головному меню, що будемо робити: ")
    else:
        bot.send_message(message.chat.id, text="Я такої команди не знаю, спробуй щось інне ;) ")

#################################################################################################################

bot.infinity_polling()