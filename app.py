import telebot

# WARNING: Revoke this token in Telegram via @BotFather and get a new one!
bot = telebot.TeleBot("8263985956:AAGC_XOIuLidE72XBhfcC_aBzWwN5IyfFYk") 

@bot.message_handler(func=lambda _: True)
def reply(message):
    # This line is now indented by 4 spaces
    bot.reply_to(message, "I'm alive 24/7! g7")

bot.polling(none_stop=True)
