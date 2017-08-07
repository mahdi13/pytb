import requests
import ujson
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

from constants import *

info = {}


def start(bot, update):
    info[update.message.chat.id] = [0, None, None, None]

    update.message.reply_text(
        TXT_FA_HELP
    )


def search(bot, update):
    if update.message.chat.id in info:
        info[update.message.chat.id][0] = 1

        update.message.reply_text(
            TXT_FA_FIRST_NAME
        )
    else:
        return start(bot, update)


def process_message(bot, update):
    if update.message.chat.id in info:
        if info[update.message.chat.id][0] == 0:  # Non found
            return start(bot, update)
        elif info[update.message.chat.id][0] == 1:  # First name
            info[update.message.chat.id][1] = update.message.text
            info[update.message.chat.id][0] = 2
            update.message.reply_text(TXT_FA_LAST_NAME)
        elif info[update.message.chat.id][0] == 2:  # Last name
            info[update.message.chat.id][2] = update.message.text
            info[update.message.chat.id][0] = 3
            update.message.reply_text(TXT_FA_FATHERS_NAME)
        elif info[update.message.chat.id][0] == 3:  # Fathers name
            info[update.message.chat.id][3] = update.message.text
            info[update.message.chat.id][0] = 0
            result = requests.request('POST', 'http://postyafteh.post.ir/r/Handlers/SearchAllHandler.ashx',
                                      data=ujson.dumps(dict(
                                          fName=info[update.message.chat.id][1],
                                          lName=info[update.message.chat.id][2],
                                          fatherName=info[update.message.chat.id][3],
                                          type='-1'
                                      )).encode())

            if result.json()['success'] == False:
                update.message.reply_text('\n'.join([TXT_FA_RESULTS_ERROR, TXT_FA_RE_SEARCH]))
            else:
                update.message.reply_text('\n'.join([TXT_FA_RESULTS,
                                                     result.json()['message']] + ['   '.join([
                    t['fName'],
                    t['lName'],
                    t['fatherName'],
                    t['n'],
                    t['nationalCode'],
                    t['findDate'],
                    t['identityNumber'],
                ]) for t in result.json()['data']] + [TXT_FA_RE_SEARCH]))
    else:
        return start(bot, update)


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('search', search))

updater.dispatcher.add_handler(MessageHandler(Filters.command, start))

updater.dispatcher.add_handler(MessageHandler(Filters.text, process_message))

updater.start_polling()
updater.idle()
