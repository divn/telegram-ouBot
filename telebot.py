import requests
import json

# config.URL for bot url plus token
import config


def get_updates():
    # Get json from ur telegram bot
    url = config.URL + 'GetUpdates?timeout=100'
    content = requests.get(url)
    js = json.loads(content.content)
    return js


def get_last_chat_id_and_text(update):
    # get last text and chatid from telegram api
    last = len(update['result']) - 1
    text = update['result'][last]['message']['text']
    chat_id = update['result'][last]['message']['chat']['id']
    return (text, chat_id)


def get_last_chat_id(update):
    # get only last chatid not text
    last = len(update['result']) - 1
    chat_id = update['result'][last]['message']['chat']['id']
    return chat_id


def send_message(text, chat_id):
    # Used to send message to users chatid with text
    sendmsg = 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    url = config.URL + sendmsg
    requests.post(url)


def own_chat_id():
    # Return static chatid set in config.py
    return config.CHATID
