import pandas as pd

import csv


def reading_files_csv(name_file):
    with open(name_file) as file:
        transaction = csv.DictReader(file)
        rows = []
        for row in transaction:
            rows.append(row)
        return rows


print(reading_files_csv("../transactions.csv"))


def reading_files_exel(name_f):
    excel_data = pd.read_excel(name_f)
    res = excel_data.to_dict(orient="records")

    return res


print(reading_files_exel("../transactions_excel.xlsx"))
