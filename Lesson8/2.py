# Мои "день, месяц и год рождения"
day = int(input("Введите день - "))
month = int(input("Введите месяц - "))
year = int(input("Введите год - "))

# Вычисляем сумму
result = day + month + year

# Вычисляем остаток от деления на 4 и добавляем 1
final_result = (result % 4) + 1

print("Итоговый результат:", final_result)
