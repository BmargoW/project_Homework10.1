def filter_by_currency(my_list, b):
    """функция, которая принимает на вход список словарей, представляющих транзакции."""

    return filter(lambda x: x["operationAmount"]["currency"]["code"] == b, my_list)


def transaction_descriptions(my_list):
    """функция, которая принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    for person in my_list:
        yield f"{person['description']}"


def card_number_generator(start, stop):
    """функция, которая генирирует номера банковских карт"""
    for i in range(start, stop):
        number_1 = str("{:016d}".format(i))
        split_number = " ".join([number_1[0:4], number_1[4:8], number_1[8:12], number_1[12:]])
        yield split_number
