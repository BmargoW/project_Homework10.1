def get_mask_card_number(numbers: str) -> str:
    """Функция которая маскирует номер карты
    :rtype: str
    """
    code = []
    for i in range(0, len(numbers), 4):
        if numbers.isdigit() is False:
            return "ошибка ввода"
        elif len(numbers) != 16:
            return "неверный номер"
        elif len(numbers) == 16:
            numi = numbers[i:i + 4]
            code.append(numi)
            mask = " ".join(code)
            maske = f"{mask[0:7]}** **** {mask[-4:]}"
    return maske


def get_mask_account(row: str) -> str:
    """Функция которая маскирует номер счета"""
    for i in range(0, len(row)):
        if row.isdigit() is False:
            return "ошибка ввода"
        elif len(row) != 16:
            return "неверный номер"
        elif len(row) == 16:
            numb = row[-4:]
            mask = f"**{numb}"
    return mask
