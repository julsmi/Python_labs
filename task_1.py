list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
list_unique = len(set(list_))
sum_unique = sum(set(list_))
mean_list_unique = sum_unique / list_unique
print(sum_unique)
print(list_unique)
print(round(mean_list_unique, 5))
