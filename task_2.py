
def get_count_char(str_):
    d = {} # TODO посчитать количество каждой буквы в строке в аргументе str_
    count_char = str_.lower().split()
    count_char.sort()
    count_char = ''.join(count_char)
    for letter in count_char:
        d[letter] = d.get(letter, 0) + 1
    return d


main_str = """
    Данное предложение будет разбиваться на отдельные слова.
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
