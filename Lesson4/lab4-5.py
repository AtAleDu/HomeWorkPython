# Создаем словарь для каждого из пяти призывников
recruit1 = {}
recruit2 = {}
recruit3 = {}
recruit4 = {}
recruit5 = {}

# Вводим данные для каждого призывника
recruit1["Фамилия"] = input("Введите фамилию 1-го призывника: ")
recruit1["Имя"] = input("Введите имя 1-го призывника: ")
recruit1["Отчество"] = input("Введите отчество 1-го призывника: ")
recruit1["Год рождения"] = input("Введите год рождения 1-го призывника: ")
recruit1["Заболевание"] = input("Введите заболевание 1-го призывника: ")

recruit2["Фамилия"] = input("Введите фамилию 2-го призывника: ")
recruit2["Имя"] = input("Введите имя 2-го призывника: ")
recruit2["Отчество"] = input("Введите отчество 2-го призывника: ")
recruit2["Год рождения"] = input("Введите год рождения 2-го призывника: ")
recruit2["Заболевание"] = input("Введите заболевание 2-го призывника: ")

recruit3["Фамилия"] = input("Введите фамилию 3-го призывника: ")
recruit3["Имя"] = input("Введите имя 3-го призывника: ")
recruit3["Отчество"] = input("Введите отчество 3-го призывника: ")
recruit3["Год рождения"] = input("Введите год рождения 3-го призывника: ")
recruit3["Заболевание"] = input("Введите заболевание 3-го призывника: ")

recruit4["Фамилия"] = input("Введите фамилию 4-го призывника: ")
recruit4["Имя"] = input("Введите имя 4-го призывника: ")
recruit4["Отчество"] = input("Введите отчество 4-го призывника: ")
recruit4["Год рождения"] = input("Введите год рождения 4-го призывника: ")
recruit4["Заболевание"] = input("Введите заболевание 4-го призывника: ")

recruit5["Фамилия"] = input("Введите фамилию 5-го призывника: ")
recruit5["Имя"] = input("Введите имя 5-го призывника: ")
recruit5["Отчество"] = input("Введите отчество 5-го призывника: ")
recruit5["Год рождения"] = input("Введите год рождения 5-го призывника: ")
recruit5["Заболевание"] = input("Введите заболевание 5-го призывника: ")

# Выводим результат в виде таблицы
print("\nТаблица призывников:")
print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Фамилия", "Имя", "Отчество", "Год рождения", "Заболевание"))
print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
    recruit1["Фамилия"], recruit1["Имя"], recruit1["Отчество"], recruit1["Год рождения"], recruit1["Заболевание"]
))
print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
    recruit2["Фамилия"], recruit2["Имя"], recruit2["Отчество"], recruit2["Год рождения"], recruit2["Заболевание"]
))
print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
    recruit3["Фамилия"], recruit3["Имя"], recruit3["Отчество"], recruit3["Год рождения"], recruit3["Заболевание"]
))
print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
    recruit4["Фамилия"], recruit4["Имя"], recruit4["Отчество"], recruit4["Год рождения"], recruit4["Заболевание"]
))
print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
    recruit5["Фамилия"], recruit5["Имя"], recruit5["Отчество"], recruit5["Год рождения"], recruit5["Заболевание"]
))