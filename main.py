from datetime import datetime
import requests
import json
import os

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
CURRENCY_RATES_FILE = 'currency_rates.json'

def main():
    while True:
        currency = input('Введите название валюты  - EUR / USD\n> ')
        if currency not in ('USD', 'EUR'):
            print('Некорректный ввод')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f'Курс {currency} к рублю {rate}')

        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choise = input('Выберите действие: \n1 - продолжить \n2 -выйти')
        if choise == '1':
            continue
        elif choise == '2':
            break
        else:
            print('Некорректный ввод')

def get_currency_rate(base: str) -> float:
    """Получает курс по API и возвращает FLOAT"""

    url = f"https://api.apilayer.com/exchangerates_data/latest"

    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': base})

    rate = response.json()['rates']['RUB']
    return rate

    # response_data = json.loads(response.text())
    # rate = response_data["rates"]["RUB"]
    # return rate

def save_to_json(data):
    """Сохраняет данные в JSON файл"""

    with open(CURRENCY_RATES_FILE, 'a') as f:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], f)
        else:
            with open(CURRENCY_RATES_FILE) as f:
                data_list = json.load(f)
                data_list.append(data)

            with open(CURRENCY_RATES_FILE, 'w') as f:
                json.dump(data_list, f)

if __name__ == '__main__':
    # print(get_currency_rate('USD'))
    main()
