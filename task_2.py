list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total = sum(set(list_numbers))
amount = len(set(list_numbers))
mean_list_numbers = total / amount

list_numbers[4] = mean_list_numbers
print(list_numbers)
