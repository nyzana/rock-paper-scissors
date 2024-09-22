import random
import telebot
from telebot import types 

bot = telebot.TeleBot("7639527173:AAF-LRPxWhuQriQ6eE89FBUcbjYblkWWmi8")
game = ["камень","ножницы","бумага"]

@bot.message_handler(commands=['start'])
def handle_start(message):
  
  keyboard = types.ReplyKeyboardMarkup(True)
  button1 = types.KeyboardButton("камень")
  button2 = types.KeyboardButton("ножницы")
  button3 = types.KeyboardButton("бумага")

  keyboard.add(button1, button2, button3)


  
  bot.send_message(message.chat.id, "Давай сыграем?", reply_markup=keyboard)
  

@bot.message_handler(func=lambda message: True)
def handle_message(message):
  random_object = random.choice(game)
  

  
  if random_object == "камень" and message.text == "ножницы":
    result = "Проигрыш"  # Камень бьёт ножницы
  elif random_object == "камень" and message.text == "бумага":
    result = "Победа"    # Бумага оборачивает камень
  elif random_object == "камень" and message.text == "камень":
    result = "Ничья"     # Оба выбрали камень

  elif random_object == "бумага" and message.text == "ножницы":
    result = "Победа"    # Ножницы режут бумагу
  elif random_object == "бумага" and message.text == "камень":
    result = "Проигрыш"  # Бумага оборачивает камень
  elif random_object == "бумага" and message.text == "бумага":
    result = "Ничья"     # Оба выбрали бумагу

  elif random_object == "ножницы" and message.text == "камень":
    result = "Победа"    # Камень бьёт ножницы
  elif random_object == "ножницы" and message.text == "бумага":
    result = "Проигрыш"  # Ножницы режут бумагу
  elif random_object == "ножницы" and message.text == "ножницы":
    result = "Ничья"     # Оба выбрали ножницы

  bot.send_message(message.chat.id, random_object)
  bot.reply_to(message, result)


bot.polling(none_stop=True)
