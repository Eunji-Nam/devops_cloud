import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import contact

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    print("TELEGRAM_TOKEN 환경변수를 지정해주세요", file=sys.stderr)
    sys.exit(1)

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="안녕. 나는 dmswlbot이야. 만나서 반가워.")


def echo(update, context):
    received_text: str = update.message.text

    if contact.cat.check_available((received_text)):
        response_text = contact.cat.make_response(received_text)
    elif contact.photo.check_available(received_text):
        response_text =contact.photo.make_response(received_text)
    else:
        response_text = "지원하지 않는 명령입니다."

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response_text)


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(
    Filters.text & (~Filters.command),
    echo,
)
dispatcher.add_handler(echo_handler)

updater.start_polling()