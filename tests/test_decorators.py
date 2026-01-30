from src.decorators import log

def test_log(capsys):
    log()
    captured = capsys.readouterr()

    assert captured.out == ""


def test_log_my_function(capsys):
    @log()
    def my_function(x, y):
        return x / y
    my_function(1, 2)
    captured = capsys.readouterr()

    assert captured.out == "my_function ok\n"

def test_log_my_function_error(capsys):
    @log()
    def my_function(x, y):
        return x / y
    my_function(1, 0)
    captured = capsys.readouterr()

    assert captured.out == "my_function error: division by zero, args: (1, 0), kwargs: {}\n"