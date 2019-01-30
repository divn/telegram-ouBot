import requests
import json

# config.URL for bot url plus token
import config


def get_updates():
    url = config.URL + 'GetUpdates?timeout=100'
    content = requests.get(url)
    js = json.loads(content.content)
    return js


def get_last_chat_id_and_text(update):
    last = len(update['result']) - 1
    text = update['result'][last]['message']['text']
    chat_id = update['result'][last]['message']['chat']['id']
    return (text, chat_id)


def send_message(text, chat_id):
    sendmsg = 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    url = config.URL + sendmsg
    requests.post(url)


text, chatid = get_last_chat_id_and_text(get_updates())
send_message(text, chatid)
