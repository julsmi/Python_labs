money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


while money_capital >= spend:
    money_left = (money_capital - spend) + salary
    spend *= 1.05
    if money_left >= spend:
        month += 1

print(month)
