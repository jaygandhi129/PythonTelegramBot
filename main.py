from datetime import *
from pytz import *
from telegram import *
from telegram.ext import *

birthdays = {
    "26-01":["Jay", "Jack"],
    "29-06": ["Jill","John"],
    "06-06": ["Sam", "Samantha"]
}

today = datetime.now(timezone('Asia/kolkata'))
today_string = today.strftime("%d-%m")

API_Key = "<BOT API KEY HERE>"
CHAT_ID = "<CHAT ID HERE>"

bot = Bot(API_Key)
updater = Updater(API_Key, use_context=True)
updater.start_polling()

if today_string in birthdays:
    message = "Birthday Notification\n"
    for i in birthdays[today_string]:
        message += i +'\n'
    print(message)
    bot.send_message(
        chat_id = CHAT_ID,
        text = message
    )
else:
    message = "No birthdays today."
    bot.send_message(
        chat_id = CHAT_ID,
        text = message
    )
updater.stop()
