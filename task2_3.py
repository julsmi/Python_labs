import json


def task():
    filename = "input.json"
    with open(filename) as f:
        data = json.load(f)
    # TODO считать содержимое JSON файла

    return max(data, key=lambda item: item["score"])  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
