day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))

sum_of_date_and_month = day + month

remainder = sum_of_date_and_month % 5

result = remainder + 1

print("Ваш вариант:", result)