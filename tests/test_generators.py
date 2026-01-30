import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(my_list_transaction, currency):

    usd_transactions = filter_by_currency(my_list_transaction, currency)

    assert next(usd_transactions) == (
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    )
    assert next(usd_transactions) == (
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    )
    assert next(usd_transactions) == (
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        })


def test_filter_by_currency_empty_list():
    with pytest.raises(StopIteration):
        usd_transactions = filter_by_currency([], "USD")
        assert next(usd_transactions) == StopIteration


def test_filter_by_currency_empty():
    with pytest.raises(StopIteration):
        non_transaction = [
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            }
        ]
        usd_transactions_1 = filter_by_currency(non_transaction, "USD")
        assert next(usd_transactions_1) == StopIteration


def test_transaction_descriptions(my_list_transaction):
    description = transaction_descriptions(my_list_transaction)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            "Перевод организации",
        ),
        (
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "Перевод со счета на счет",
        ),
        (
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
            ],
            "Перевод со счета на счет",
        ),
    ],
)
def test_transaction_descriptions_1(value: list, expected: str) -> None:
    description = transaction_descriptions(value)
    assert next(description) == expected


def test_transaction_descriptions_empty_list():
    with pytest.raises(StopIteration):
        transaction = []
        description = transaction_descriptions(transaction)
        assert next(description) == StopIteration


def test_transaction_descriptions_key_error():
    with pytest.raises(KeyError):
        transaction = [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        ]
        description = transaction_descriptions(transaction)
        assert next(description) == KeyError


def test_card_number_generator():
    result = list(card_number_generator(0, 5))
    expected = [
        "0000 0000 0000 0000",
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
    ]

    assert result == expected
