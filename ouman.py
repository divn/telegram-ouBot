import requests
import config

VALVE = 'S_272_85'


def valve_position():
    try:
        temp = requests.get('http://' + config.OUMANIP +
                            '/request?' + VALVE, timeout=1)

        data = temp.text
        data = int(data[17:-2])
        return data

    except requests.exceptions.RequestException:
        return 666
