import os
import tempfile

def merge_sort(arr, chunk_size, memory_limit):
    # Функция сортировки слиянием для отрезка массива
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Функция разделения массива на отрезки
    def split_into_chunks(array, chunk_size):
        return [array[i:i + chunk_size] for i in range(0, len(array), chunk_size)]

    # Запись отрезка в файл
    def write_chunk_to_file(chunk):
        with tempfile.NamedTemporaryFile(delete=False, mode='w+') as temp_file:
            temp_file.write('\n'.join(map(str, chunk)))

        return temp_file.name

    # Чтение отрезка из файла
    def read_chunk_from_file(file_path):
        with open(file_path, 'r') as file:
            return list(map(int, file.read().splitlines()))

    # Сортировка отрезка и запись в файл
    def sort_chunk_and_write(chunk):
        sorted_chunk = sorted(chunk)
        return write_chunk_to_file(sorted_chunk)

    # Сортировка массива слиянием
    def merge_sort_recursive(array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        left_file = sort_chunk_and_write(left)
        right_file = sort_chunk_and_write(right)

        left_chunk = read_chunk_from_file(left_file)
        right_chunk = read_chunk_from_file(right_file)

        merged_chunk = merge(left_chunk, right_chunk)

        os.remove(left_file)
        os.remove(right_file)

        return merged_chunk

    # Сортировка слиянием для всего массива
    chunks = split_into_chunks(arr, chunk_size)
    chunk_files = [sort_chunk_and_write(chunk) for chunk in chunks]

    while len(chunk_files) > 1:
        new_chunk_files = []

        for i in range(0, len(chunk_files), 2):
            if i + 1 < len(chunk_files):
                left_chunk = read_chunk_from_file(chunk_files[i])
                right_chunk = read_chunk_from_file(chunk_files[i + 1])
                merged_chunk = merge(left_chunk, right_chunk)
                new_chunk_files.append(write_chunk_to_file(merged_chunk))
            else:
                # Если нечетное количество файлов, просто копируем оставшийся файл
                new_chunk_files.append(chunk_files[i])

        for file_path in chunk_files:
            os.remove(file_path)

        chunk_files = new_chunk_files

    sorted_array = read_chunk_from_file(chunk_files[0])
    os.remove(chunk_files[0])

    return sorted_array

# Пример использования
arr = [5, 3, 8, 4, 2, 1, 7, 6]
chunk_size = 2  # P
memory_limit = 10  # M

result = merge_sort(arr, chunk_size, memory_limit)
print("Отсортированный массив:", result)
