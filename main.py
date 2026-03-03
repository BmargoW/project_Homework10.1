from pycodestyle import continued_indentation

from src.reading_file import reading_files_csv, reading_files_exel
from src.utils import uploading_content
from src.processing import filter_by_state, sort_by_date

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



    def user_status(ruster):
        while True:
            u_s = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().upper()
            if u_s in ["EXECUTED", "CANCELED", "PENDING"]:
                return filter_by_state(ruster,u_s)
            else:
                print(f"Статус операции {u_s} недоступен")
                print("""Некорректный ввод. Пожалуйста, введите статусы: EXECUTED, CANCELED, PENDING""")


    def user_data(roster):
        u_d = input("Отсортировать операции по дате? ДА/НЕТ: ").strip().upper()
        if u_d == "ДА":
            my_data = input(
                "Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию: ").strip().lower()
            if my_data == "по возрастанию":
                return sort_by_date(roster, decreasing=False)
            elif my_data == "по убыванию":
                return sort_by_date(roster, decreasing=True)
            else:
                print("Некорректный ввод сортировки.")
                return roster
        elif u_d == "НЕТ":
            print("ok")
            return roster
        else:
            print("Некорректный ввод Да/Нет.")
            return roster


    result = user_selection()
    result_2 = user_status(result)
    result_3 = user_data(result_2)
    print(result_3)


if __name__ == "__main__":
    main()


