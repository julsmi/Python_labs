INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, 'r') as input_:
        with open(OUTPUT_FILE, 'w') as output_:
            for upper_str in (map(str.upper, input_)):
                output_.write(upper_str)# TODO перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
