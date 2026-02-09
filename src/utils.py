import json


def uploading_content(name_file):
    with open(name_file) as json_file:
        try:
            data = json.load(json_file)
            return data
        except json. JSONDecodeError:
            print("invalid JSON data")
            return []