def mask_account_card(accaunt_number: str) -> str:
    """функция, возвращает тип, но маскирует номер данных"""

    if accaunt_number.isdigit() is True:
        return "введите тип карты или 'счет'"

    elif accaunt_number.isalpha() is True:
        return "введите номер"

    text = accaunt_number.split()
    just_words = []
    code = []

    for element in text:
        if element.isalpha():
            just_words.append(element)
        elif element.isdigit():
            issue = element

    i: int
    for i in range(0, len(issue), 4):
        if len(issue) >= 16:
            if len(issue) == 16:
                character = issue[i:i + 4]
                code.append(character)
                mask = " ".join(code)
                maske = f"{mask[0:7]}** **** {mask[-4:]}"
            elif len(issue) > 16:
                mask = issue[-4:]
                maske = f"**{mask}"
            continue
        return "неправильно введен номер"

    text_2 = " ".join(just_words)
    return f"{text_2} {maske}"


def get_date(character: str) -> str:
    """функция, которая фильтрует предоставленный набор данных
    и возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    text_new = character[0:10]
    text1 = text_new.replace("-", " ")
    words = text1.split()
    words1 = words[::-1]
    date = ".".join(words1)
    return date
