

from src.reading_file import reading_files_csv, reading_files_exel
from src.utils import uploading_content

def main():

    print("""Программа: Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")

    def user_selection():
        while True:
            level = input("Выберите необходимый пункт меню (1, 2 или 3): ")
            if level == "1":
                return uploading_content("C:/Users/Honor/PycharmProjects/project_Homework11.1/data/operations.json")
            elif level == "2":
                return reading_files_csv("C:/Users/Honor/PycharmProjects/project_Homework11.1/transactions.csv")
            elif level == "3":
                return reading_files_exel("C:/Users/Honor/PycharmProjects/project_Homework11.1/transactions_excel.xlsx")
            else:
                print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

    result = user_selection()
    print(result)

if __name__ == "__main__":
    main()


