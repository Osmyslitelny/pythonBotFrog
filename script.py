from project.src.config import CONFIG
from project.src import handler_day
from project.src import handler_tea
from telegram.ext import CommandHandler, Updater


def main():
    updater = Updater(CONFIG['token'])
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('day', handler_day.day))
    dp.add_handler(CommandHandler('tea', handler_tea.tea))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()