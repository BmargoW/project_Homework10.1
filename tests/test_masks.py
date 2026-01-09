from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1234567898765432") == "1234 56** **** 5432"
    assert get_mask_card_number("visit") == "ошибка ввода"
    assert get_mask_card_number("123456789876543") == "неверный номер"


def test_get_mask_account() -> None:
    assert get_mask_account("1234123412345678") == "**5678"
    assert get_mask_account("doc") == "ошибка ввода"
    assert get_mask_account("123456") == "неверный номер"
