import telebot
import ouman
import time


def main():
    print('Bot Started')
    chatid = telebot.own_chat_id()
    warninglimit = 25
    errorcode = 666
    while True:
        valveposition = ouman.valve_position()
        warning = 'Warning valve position ' + str(valveposition)
        if errorcode > valveposition >= warninglimit:
            telebot.send_message(warning, chatid)
            print('Error Send ' + str(valveposition))
            time.sleep(300)

        else:
            print(valveposition)
            time.sleep(120)


if __name__ == '__main__':
    main()
