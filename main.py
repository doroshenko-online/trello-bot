import sys
from os import getenv

from bot.app import TGBot


TG_TOKEN = getenv('TG_TOKEN')
TRELLO_API_KEY = getenv('TR_API_KEY')
TRELLO_TOKEN = getenv('TR_TOKEN')
TRELLO_BOARD_ID = getenv('TR_BOARD_ID')


if __name__ == '__main__':
    if not TG_TOKEN:
        print('Wrong TG_TOKEN')
        sys.exit(2)

    if not TRELLO_TOKEN or not TRELLO_API_KEY or not TRELLO_BOARD_ID:
        print('Wrong trello credentials')
        sys.exit(2)

    tg_bot = TGBot(TG_TOKEN, TRELLO_API_KEY, TRELLO_TOKEN, TRELLO_BOARD_ID)
