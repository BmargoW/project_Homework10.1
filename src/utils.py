import json


def uploading_content(name_file):
    """функция из JSON-файла возвращает список словарей с данными о финансовых транзакциях."""
    with open(name_file) as json_file:
        try:
            data = json.load(json_file)
            return data
        except json.JSONDecodeError:
            print("invalid JSON data")
            return []
        except json.FileNotFoundError:
            print("invalid JSON data")
            return ["File not found"]
