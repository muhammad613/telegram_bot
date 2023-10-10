from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from menu import (
    main_menu_keyboard,
    courses_menu_keyboard
)
from key_buttons import tele_button, courses
user_navigation_stack = []


ABOUT = tele_button[0]
COURSES = tele_button[1]
LOCATION = tele_button[2]


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Добро пожаловать {update.effective_user.username}\nЭтот бот поможет вам с информацией о курсах',
        reply_markup=main_menu_keyboard()
    )

def about(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Преимущества обучения в Codify · Обучение с нуля до Junior.'
        f' Пройди обучение по авторской программе Codify и стань Junior специалистом.'
    )

def courses(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Choose course:',
        reply_markup=courses_menu_keyboard()
    )

def python(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Python',
    )

def java(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Java',
    )

def js(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'JS',
    )

def qa(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'QA',
    )

def back(update: Update, context: CallbackContext):
        update.message.reply_text(
            f"Возвращение в меню:",
            reply_markup=main_menu_keyboard()
        )

def location(update:Update, context:CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Location of Codify'
    )
    update.message.reply_location(
        #42.82909025000069, 74.61687279022618
        longitude=74.61687279022618,
        latitude=42.82909025000069,
        reply_to_message_id=msg.message_id
    )
             

updater = Updater(token=TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSES),
    courses
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('Python'),
    python
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('Java'),
    java
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('JS'),
    js
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('QA'),
    qa
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('Back'),
    back
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATION),
    location
))

updater.start_polling()
updater.idle()