import logging
from telegram import Update, ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler

def get_lang(context:CallbackContext):
    lang = '' 
    try:
        lang = context.user_data['preference']['lang']
    except Exception as e :
        lang = 'en' #Default Language
    return lang


def initialize_user_data(context: CallbackContext):
    context.user_data.clear()
    lang = 'en' # Default language    
    context.user_data['preference'] = {} # set the default language
    context.user_data['preference']['lang'] = lang
    context.user_data['preference']['time'] = 2

    return lang


def reset_user_data(context: CallbackContext):
    if 'preference' in context.user_data:
        # Delete the search selection
        preference = context.user_data['preference']
        context.user_data.clear()
        context.user_data['preference'] = preference
    else:
        context.user_data.clear()
        initialize_user_data(context)


def update_lang(lang , context:CallbackContext):
    context.user_data['preference']['lang'] = lang

def update_campus(campus , context:CallbackContext):
    context.user_data['preference']['campus'] = campus

def update_time(time , context:CallbackContext):
    context.user_data['preference']['campus'] = int(time)

def get_user_preferences(context:CallbackContext):
    time = 0
    loc = None
    try:
        time = context.user_data["preference"]["time"]
    except Exception:
        print("time")
    try:
        loc = context.user_data["preference"]["campus"]
    except Exception:
        print("loc")
    print(loc , time)
    return loc , time