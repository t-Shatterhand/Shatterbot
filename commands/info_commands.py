def bot_help(update, context):
    update.message.reply_text(
        "This multi-purpose bot is made and maintained by Shatterhand. Use /contacts to get my contact info.\n\n"
        "Text me if you do have any questions or propositions. For the list of commands, type /commands.\n\n"
        "The bot is written on python 3.7 with the usage of telegram-bot-api lib. Feel free to ask me for the code. ")


def contacts(update, context):
    update.message.reply_text('''
    Contacts:
    Telegram: t.me/t_shatterhand (@t_shatterhand)
    Discord: t_shatterhand#3181
    GitHub/GitLab: GitHub.com/CognitusNL 
    GitHub repo for this project: GitHub.com/CognitusNL/Shatterbot
    ''')


def commands(update, context):
    update.message.reply_text('''
    List of commands:
    /help - brief information about the bot
    /commands - SUDDENLY, commands!
    /start - actually starts bot
    /contacts - show my contact info
    /getweather <city> - get the current weather information in the city
    /getmusic <URL> - get the audio from youtube video in m4a
    ''')
