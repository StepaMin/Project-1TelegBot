import telebot
import create_db as db

bot = telebot.TeleBot('-')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Привет, ' + message.from_user.first_name
                     + '. Я умею запоминать и отправлять твоё последнее сообщение.')
    bot.send_message(message.from_user.id, '/replay - для получения сообщения')

@bot.message_handler(commands=['replay'])
def PrintNote(message):
    id_user = message.from_user.id
    result = db.PrintText(id_user)
    bot.send_message(message.from_user.id, result)


@bot.message_handler(content_types=['text'])
def start(message):
    text = message.text
    id_users = message.from_user.id
    db.AddText(id_users, text)
    #print("Успешно сохранено")
    bot.send_message(message.from_user.id, 'Успешно сохранено')



bot.polling(none_stop=True)

