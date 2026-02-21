import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def uploading_content(name_file):
    """функция из JSON-файла возвращает список словарей с данными о финансовых транзакциях."""
    with open(name_file) as json_file:
        try:
            data = json.load(json_file)
            logger.info("valid data was received from the file")
            return data
        except json.JSONDecodeError:
            logger.error("invalid JSON data")
            print("invalid JSON data")
            return []


if __name__ == "__main__":
    uploading_content("../data/operations.json")
