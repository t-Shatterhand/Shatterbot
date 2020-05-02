from __future__ import unicode_literals
from commands import info_commands, video_commands, weather_commands
from telegram.ext import Updater, CommandHandler

import logging
import tokens

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! To get the help information, type /help. To get the list of commands, try /commands')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    update.message.reply_text(str(context.error))


def main():
    updater = Updater(tokens.bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('getWeather', weather_commands.getWeather))
    dp.add_handler(CommandHandler('contacts', info_commands.contacts))
    dp.add_handler(CommandHandler('help', info_commands.bot_help))
    dp.add_handler(CommandHandler('commands', info_commands.commands))
    dp.add_handler(CommandHandler('getMusic', video_commands.getMusic))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
