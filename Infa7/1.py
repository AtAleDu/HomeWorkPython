def hash_mid_square(book_title):
    ascii_sum = sum(ord(char) for char in book_title)
    return ascii_sum % 100  # Просто ограничим хеш до 2 знаков

def insert_books(books):
    hash_table = {}
    for book_title in books:
        hash_value = hash_mid_square(book_title)
        if hash_value not in hash_table:
            hash_table[hash_value] = [book_title]
        else:
            hash_table[hash_value].append(book_title)
    return hash_table

# Создаем книги
books = ["Алгоритмы и структуры данных",
         "Искусство программирования",
         "Программирование на Python",
         "Введение в алгоритмы",
         "Мастер и Маргарита",
         "Мцыри",
         "Мертвые Души"]

# Вставляем книги в хеш-таблицу методом средних квадратов
hash_table = insert_books(books)

# Выводим результат
for key, values in hash_table.items():
    print(f"Хеш: {key}, Книги: {values}")
