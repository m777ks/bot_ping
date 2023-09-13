import os
import telebot

hostname = "http://127.0.0.1:8000/"
bot = telebot.TeleBot('')


# response = os.system('ping ' + hostname)
# bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
  mess = f'Hello, <b>{message.from_user.first_name}</b>'
  com = f'Введите сайт для пинга'
  bot.send_message(message.chat.id, mess, parse_mode='html')
  bot.send_message(message.chat.id, com, parse_mode='html')

@bot.message_handler()
def website(message):

  response = os.system('ping ' + message.text)
  bot.send_message(message.chat.id, response)
  if response == 0:
    bot.send_message(message.chat.id, f'{message.text} -- GOOD')
  else:
    bot.send_message(message.chat.id, f'{message.text} -- NOO')


# response = os.system('ping ' + hostname)
# bot = telebot.TeleBot(token)
# if response == 0:
#   print(hostname + ' is up!')
# else:
#   print(hostname + ' is down!')
#   bot.send_message(message.chat.id, hostname + ' is down!')
bot.polling(none_stop=True)
