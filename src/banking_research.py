import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    my_dict = []
    for element in data:
        if re.fullmatch(search, element["description"]):
            my_dict.append(element)
        else:
            pass
    return my_dict
