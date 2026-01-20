import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    assert mask_account_card("Visa 1234567812345678") == "Visa 1234 56** **** 5678"
    assert mask_account_card("Maestro") == "введите номер"
    assert mask_account_card("123456789876543") == "введите тип карты или 'счет'"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2025-11-30T02:26:18.671407", "30.11.2025"),
        ("2024-10-31T02:26:18.671407", "31.10.2024"),
        ("2020-09-17T02:26:18.67", "17.09.2020"),
    ],
)
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected
