def log(filename=None):
    def abbreviated_text(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = "my_function ok"
            except Exception as e:
                result = None
                log_message = f"my_function error: {e}, args: {args}, kwargs: {kwargs}"

            if filename is None:
                print(log_message)
            else:
                with open(filename, 'a') as file:
                    file.write(log_message + '\n')

            return result

        return wrapper

    return abbreviated_text
