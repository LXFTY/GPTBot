import g4f
import telebot

g4f.debug.logging = True

token = 'BOT_TOKEN'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я бот работающий на базе G4Free.')

@bot.message_handler(content_types=['text'])
def message_handler(message):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": message.text}],
    )
    bot.reply_to(message, response)

if __name__ == '__main__':
    bot.polling(none_stop=True)