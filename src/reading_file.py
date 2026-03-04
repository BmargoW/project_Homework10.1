import pandas as pd

import csv


def reading_files_csv(name_file):
    """Функция, которая считывает  финансовые операции из файла - csv
    и возвращает список словарей с транзакциями"""
    data = []
    with open(name_file, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            data.append(row)
    return data



def reading_files_exel(name_f):
    """Функция, которая считывает  финансовые операции из файла - Excel
    и возвращает список словарей с транзакциями"""
    excel_data = pd.read_excel(name_f)
    res = excel_data.to_dict(orient="records")

    return res


if __name__ == "__main__":
    print(reading_files_exel("../transactions_excel.xlsx"))
    print(reading_files_csv("../transactions.csv"))
