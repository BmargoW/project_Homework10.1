import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    my_dict = []
    for element in data:
        if re.fullmatch(search, element["description"]):
            my_dict.append(element)
        else:
            pass
    return my_dict


def process_bank_operations(data: list[dict], categories: list) -> dict:
    new_list = []
    for element in data:
        if element["description"] in categories:
            new_list.append(element["description"])
    counted = Counter(new_list)
    return counted
