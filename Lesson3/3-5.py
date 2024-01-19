surname = input("Введите фамилия: ")
name = input("Введите имя: ")
group = input("Введите номер группы: ")

print("Привет, %s %s из группы %s!\nВведи свою электронную почту?" % (surname, name, group))

email = input("Введи свою электронную почту: ")

text = (
    surname[:5].lower() +
    name[:5].lower() * 2 +
    email[:5].lower() * 3
)



print("Зашифрованный текст: ", text)