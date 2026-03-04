import pytest
from src.banking_research import process_bank_search, process_bank_operations


def test_process_bank_search(my_list_transaction) -> None:

    assert process_bank_search(my_list_transaction, "Перевод организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    with pytest.raises(TypeError):
        process_bank_search(my_list_transaction, 2)


def test_process_bank_operations(my_list_transaction):
    sequence = ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]
    assert process_bank_operations(my_list_transaction, sequence) == {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1,
    }
