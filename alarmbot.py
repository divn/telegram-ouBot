import telebot
import ouman
import time


def main():
    print('Bot Started')
    chatid = telebot.get_last_chat_id(telebot.get_updates())
    warninglimit = 30
    errorcode = 666
    while True:
        valveposition = ouman.valve_position()
        warning = 'Warming valve position ' + str(valveposition)
        if errorcode > valveposition >= warninglimit:
            telebot.send_message(warning, chatid)
            time.sleep(300)
            print('Error Send' + valveposition)

        time.sleep(120)
        print(valveposition)


if __name__ == '__main__':
    main()
