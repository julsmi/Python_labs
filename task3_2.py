def min_len_check(fn):
    # TODO записать обертку для исходной функции
    def wrapper(str_):
        if len(str_) < 10:
            raise ValueError("Строка слишком короткая")
        result = fn(str_)
        return result
    return wrapper


# TODO задекорировать функцию
@min_len_check
def some_func(str_arg: str):
    ...


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
