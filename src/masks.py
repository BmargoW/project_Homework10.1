import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(numbers: str) -> str:
    """Функция которая маскирует номер карты
    :rtype: str
    """
    code = []
    for i in range(0, len(numbers), 4):
        if numbers.isdigit() is False:
            logger.error("There are more than just numbers in the card number")
            return "ошибка ввода"
        elif len(numbers) != 16:
            logger.error("incorrect number of digits")
            return "неверный номер"
        elif len(numbers) == 16:
            numi = numbers[i : i + 4]
            code.append(numi)
            mask = " ".join(code)
            maske = f"{mask[0:7]}** **** {mask[-4:]}"
            logger.info("the card number is being mask")
    return maske


def get_mask_account(row: str) -> str:
    """Функция которая маскирует номер счета"""
    for i in range(0, len(row)):
        if row.isdigit() is False:
            logger.error("There are more than just numbers in the card number")
            return "ошибка ввода"
        elif len(row) != 16:
            logger.error("incorrect number of digits")
            return "неверный номер"
        elif len(row) == 16:
            numb = row[-4:]
            mask = f"**{numb}"
            logger.info("the account number is being masked")
    return mask


if __name__ == "__main__":
    get_mask_card_number("1234567812345679")
