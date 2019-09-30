import logging
from datetime import datetime

from pymongo.collection import Collection
from telegram import Update, User, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

from db.mongo import get_db
from mode import Mode

MAGIC_NUMBER = 42
logger = logging.getLogger(__name__)


# todo: extract maybe?
class DB:
    def __init__(self, db_name: str):
        self._coll: Collection = get_db(db_name).quarantine

    def add_user(self, user_id: str):
        self._coll.insert_one({
            "user_id": user_id,
            "datetime": datetime.now()
        })

    def find_user(self, user_id: str):
        return self._coll.find_one({"user_id": user_id})


db = DB("towel_mode")
mode = Mode(mode_name="towel_mode", default=True)


def quarantine_filter(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    # todo: cache it
    user = db.find_user(user_id)
    # if user exist -> remove message
    if user is not None:
        context.bot.delete_message(
            update.effective_chat.id,
            update.effective_message.message_id, 10
        )


@mode.add
def add_towel_mode(upd: Updater, handlers_group: int):
    logger.info("registering towel-mode handlers")
    dp = upd.dispatcher

    # catch all new users and drop the towel
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, catch_new_user),
                   handlers_group)

    # remove messages from users from quarantine
    dp.add_handler(MessageHandler(
        Filters.group & ~Filters.status_update, quarantine_filter),
        handlers_group
    )

    # catch "I am a bot" button press and instantly ban!
    # kick all not replied users (check every minutes)


def quarantine_user(user: User, chat_id: str, context: CallbackContext):
    logger.info(f"put {user} in quarantine")
    db.add_user(user.id)

    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Я не бот!", callback_data=MAGIC_NUMBER)]])
    context.bot.send_message(
        chat_id,
        # todo: rewrite test
        f"{user.name} Нажми кнопку ниже, чтобы доказать, что ты не бот.\n"
        "Я буду удалять твои сообщения, пока ты не сделаешь это.\n"
        "А коли не сделаешь, через час выкину из чата.\n"
        "Ничего личного, просто боты одолели.\n",
        reply_markup=markup
    )


def catch_new_user(update: Update, context: CallbackContext):
    for user in update.message.new_chat_members:
        quarantine_user(user, update.effective_chat.id, context)
