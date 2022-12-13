OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, 'w') as f:
        for line in range(1,11):
            f.write(f"{line * '*':>10}\n")# TODO записать лесенку в файл


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
