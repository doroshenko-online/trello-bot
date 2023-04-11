from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext, ConversationHandler, CallbackQueryHandler
from bot.keyboard import MAIN_KEYBOARD, TRELLO_KEYBOARD
from trello_cls import Trello


class TGBot:
    app = None
    trello = None
    accepted_ids = ['439874726']

    def __init__(self, token, tr_app_key, tr_token, tr_board_id):
        self.app = Application.builder().token(token).build()

        self.app.add_handler(CommandHandler('help', self.help_command))
        self.app.add_handler(CommandHandler('id', self.id_command))
        self.app.add_handler(CommandHandler('start', self.start))
        self.trello = Trello(tr_app_key, tr_token, tr_board_id)

        self.app.add_handler(CommandHandler('start', self.start))
        self.app.add_handler(ConversationHandler(

            entry_points=[
                CommandHandler('trello', self.trello_handler)
            ],
            states={},
            fallbacks=[CommandHandler('cancel', self.cancel)]
        ))

        self.app.run_polling()

    async def start(self, update, context):
        if str(update.message.chat_id) in self.accepted_ids:
            await update.message.reply_text(
                text=f'Твой Telegram ID: {str(update.message.chat_id)}',
                reply_markup=ReplyKeyboardMarkup(MAIN_KEYBOARD)
            )

    async def cancel(self, update, context):
        if str(update.message.chat_id) in self.accepted_ids:
            await update.message.reply_text(reply_markup=ReplyKeyboardMarkup(MAIN_KEYBOARD))

    # Определяем функцию-обработчик команды /help
    async def help_command(self, update, context):
        if str(update.message.chat_id) in self.accepted_ids:
            resp = self.trello.get_lists()
            await update.message.reply_text(resp)

    # Определяем функцию-обработчик команды /id
    async def id_command(self, update, context):
        user_id = str(update.message.chat_id)
        if user_id in self.accepted_ids:
            await update.message.reply_text(
                text=f'Твой Telegram ID: {user_id}',
                reply_markup=ReplyKeyboardMarkup(MAIN_KEYBOARD)
            )
        else:
            await update.message.reply_text(text=f'Твой Telegram ID: {user_id}')

    async def trello_handler(self, update: Update, context: CallbackContext):
        print('huy')
        if str(update.callback_query.message.chat_id) in self.accepted_ids:
            print(update.callback_query.data)
            if update.callback_query.data == 'Trello>>':
                reply_markup = ReplyKeyboardMarkup(TRELLO_KEYBOARD)
                await update.callback_query.message.reply_text(text='Choice action', reply_markup=reply_markup)
            elif update.callback_query.data == 'Show lists':
                await update.callback_query.message.reply_text(self.trello.get_lists())
