from src.masks import get_mask_card_number, get_mask_account
import pytest
from typing import Any


def test_get_mask_card_number(numbers: Any) -> None:
    assert get_mask_card_number("1234567898765432") == "1234 56** **** 5432"
    assert get_mask_card_number("visit") == "ошибка ввода"
    assert get_mask_card_number("123456789876543") == "неверный номер"

    with pytest.raises(TypeError):
        get_mask_card_number(" ")


def test_get_mask_account(numbers: Any) -> None:
    assert get_mask_account("1234123412345678") == "**5678"
    assert get_mask_account("doc") == "ошибка ввода"
    assert get_mask_account("123456") == "неверный номер"

    with pytest.raises(TypeError):
        get_mask_account(row=" ")


@pytest.fixture
def numbers(numbers: str) -> str:
    return "**5687"


def test_get_mask(numbers: Any) -> None:
    assert get_mask_account("1243223412345687") == numbers
