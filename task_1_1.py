def task() -> list:
    num_list = [
        "12",
        "14",
        3.1415926,
        5,
        0xFF,  # шестнадцатеричное представление
        0b1010101010  # бинарное представление представление
    ]

    return list(map(lambda x: int(x), num_list))  # TODO c помощью функции map привести каждый элемент списка к типу int


if __name__ == "__main__":
    print(task())
