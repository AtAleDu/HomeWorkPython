"""""  
Основные различия:

Изменяемость:

Список изменяем, т.е., вы можете добавлять, удалять и изменять элементы после создания.
Словарь изменяем, и вы можете изменять значение элементов по ключу.
Кортеж неизменяем, после создания вы не можете добавить, удалить или изменить элементы.
Упорядоченность:

Список и кортеж упорядочены, что означает, что элементы хранятся в определенном порядке.
Словарь не упорядочен до версии Python 3.7, но с Python 3.7+ порядок элементов в словаре сохраняется (произошли изменения в языке).
Способы обращения к элементам:

В списках и кортежах элементы доступны по индексу.
В словарях элементы доступны по ключу.
Синтаксис:

Списки записываются в квадратных скобках: my_list = [1, 2, 3].
Словари записываются в фигурных скобках: my_dict = {'a': 1, 'b': 2}.
Кортежи записываются в круглых скобках: my_tuple = (1, 2, 3).

### Операции:
- **`in`:** Проверяет наличие элемента в структуре данных.
- **`len`:** Возвращает количество элементов.
- **`clear`:** Очищает содержимое структуры данных.

### Дополнительные операции:
- **Математические операции с множествами:**
  - Объединение: `union(set2)`
  - Пересечение: `intersection(set2)`
  - Разность: `difference(set2)`
  - Дополнение: `symmetric_difference(set2)`

Python предоставляет богатый набор операций для управления данными, и эти возможности структур данных делают его мощным инструментом для разработки.

Если у тебя есть конкретные вопросы или что-то еще хочешь узнать, дай знать!
"""""
# Создание списка
listik = [1, 2, 3, 4]

# Добавление элемента в конец
listik.append(5)

# Добавление элемента в середину
listik.insert(2, 10)

# Удаление элемента с конца
removed_element = listik.pop()

# Удаление элемента из середины
specific_element = listik.pop(1)
