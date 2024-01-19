def hash_by_title_length(book_title):
    return len(book_title) % 1000  # Ограничим хеш до 3 знаков

def insert_books(books):
    hash_table = {}
    for book in books:
        hash_value = hash_by_title_length(book)
        if hash_value not in hash_table:
            hash_table[hash_value] = [book]
        else:
            hash_table[hash_value].append(book)
    return hash_table

# Создаем книги
books = ["Введение в алгоритмы",
         "Мастер и Маргарита",
         "Мцыри",
         "Мертвые Души",
         "Преступление и наказание"]

# Вставляем книги в хеш-таблицу по длине названия
hash_table_by_length = insert_books(books)

# Выводим результат
for key, values in hash_table_by_length.items():
    print(f"Хеш: {key}, Книги: {values}")
