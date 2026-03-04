import os

import requests
from dotenv import load_dotenv

load_dotenv()

t = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "1.00", "currency": {"name": "USD", "code": "USD"}},
}


def report_operation(action):
    """функция, которая принимает на вход транзакцию и возвращает сумму транзакции (
    amount) в рублях, тип данных — float. Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли."""
    if action["operationAmount"]["currency"]["code"] == "RUB":

        return float(action["operationAmount"]["amount"])
    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"

        API_KEY = os.getenv("API_KEY")

        payload = {
            "amount": (action["operationAmount"]["amount"]),
            "from": (action["operationAmount"]["currency"]["name"]),
            "to": "RUB",
        }
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers, params=payload)

        # status_code = response.status_code
        resultet = dict(response.json())
        d = float(resultet["result"])

        return d


if __name__ == "__main__":
    print(report_operation(t))
