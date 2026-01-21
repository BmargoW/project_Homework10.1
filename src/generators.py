usd_transactions = filter(lambda x: x["operationAmount"]["currency"]["code"] == "USD" , list)


def transaction_descriptions(my_list):
    for person in my_list:
        yield f"{person["description"]}"


def card_number_generator(start,stop):
    for i in range(start, stop):
        number_1= str('{:016d}'.format(i))
        split_number = " ".join([number_1[0:4], number_1[4:8], number_1[8:12], number_1[12:]])
        yield split_number



