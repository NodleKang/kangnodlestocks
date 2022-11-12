import telegram
from config import settings

#for key, value in settings.items():
#    print(key, value)

if isinstance(settings.telegram.bot_token, str):
    bot = telegram.Bot(token=settings.telegram.bot_token)
if isinstance(settings.telegram.chat_id, int):
    chat_id = settings.telegram.chat_id

bot.sendMessage(chat_id=chat_id, text="read file")
