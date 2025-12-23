import telebot

bot = telebot.TeleBot("8129717125:AAGU_LOnMWI70DS3gosTdwe3sFdwvkiUbio") # Replace with your token

@bot.message_handler(func=lambda _: True)
def reply(message):
bot.reply_to(message, "I'm alive 24/7! g7")

bot.polling(none_stop=True) # Keeps the bot running
