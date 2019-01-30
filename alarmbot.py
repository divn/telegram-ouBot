import telebot
import ouman

text, chatid = telebot.get_last_chat_id_and_text(telebot.get_updates())
valveposition = ouman.valve_position()
telebot.send_message(valveposition, chatid)
