from app import bot

bot.set_webhook('https://python2022g.pythonanywhere.com/api')
print(bot.getWebhookInfo())