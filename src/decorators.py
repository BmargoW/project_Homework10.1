def log(filename=None):
    """декоратор логирует детали выполнения функций, передавая информацию в консоль
    либо в файл, если в Декоратор передан аргумент с именем данного файла"""

    def abbreviated_text(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)  # Выполнение функции
                log_message = "my_function ok"
            except Exception as e:
                result = None
                log_message = f"my_function error: {e}, args: {args}, kwargs: {kwargs}"

            if filename is None:
                print(log_message)
            else:
                with open(filename, "a") as file:
                    file.write(log_message + "\n")

            return result  # Возврат результата или None при ошибке

        return wrapper

    return abbreviated_text
