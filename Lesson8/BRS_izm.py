import random
from prettytable import PrettyTable

def main():
    num_students = int(input('Сколько студентов у вас в группе? '))
    num_krms = int(input('Сколько контрольных работ посмотрим? '))

    # Веса КРМ (в данном случае все веса равны 1)
    krms_weights = [1] * num_krms

    student_scores = generate_scores(num_students, num_krms)
    student_scores = calculate_discipline_rating(student_scores, krms_weights)

    display_results(student_scores, num_krms)


def generate_scores(num_students, num_krms):
    scores = {}
    for i in range(num_students):
        full_name = input(f"Как зовут студента номер {i + 1}? ")

        # Добавим проверку наличия пробела в строке
        if ' ' not in full_name:
            print("Введите имя и фамилию через пробел. Попробуйте снова.")
            i -= 1
            continue

        student_name, student_surname = full_name.split()
        full_name = f"{student_surname} {student_name}"
        scores[full_name] = {"ФИО": full_name, "Рейтинг промежуточной аттестации": random.randint(0, 100)}

        for j in range(1, num_krms + 1):
            n = random.uniform(0, 35)
            score = assign_score(n)
            scores[full_name][f"Рейтинг КРМ {j}"] = score
            scores[full_name][f"КРМ {j}"] = score * 25

    return scores


def assign_score(n):
    if n < 5:
        return 0
    elif n < 10:
        return 1
    elif n < 20:
        return 2
    elif n < 30:
        return 3
    else:
        return 4

def calculate_discipline_rating(scores, krms_weights):
    num_krms = len(krms_weights)
    for student_data in scores.values():
        total_weight = sum(krms_weights)
        current_ratings = [student_data[f"КРМ {i}"] for i in range(1, num_krms + 1)]
        weights = [w / total_weight for w in krms_weights]

        current_rating = sum((weights[i - 1] * current_ratings[i - 1]) for i in range(1, num_krms + 1))

        student_data["Рейтинг текущего контроля"] =  round(current_rating, 1)
        student_data["Рейтинг по дисциплине"] = round(max(0.6 * current_rating + 0.4, current_rating), 1)

        determine_grade(student_data)

    return scores

def determine_grade(student_data):
    if student_data["Рейтинг по дисциплине"] >= 85:
        student_data["Оценка за дисциплину"] = "Отлично"
    elif student_data["Рейтинг по дисциплине"] >= 75:
        student_data["Оценка за дисциплину"] = "Хорошо"
    elif student_data["Рейтинг по дисциплине"] >= 60:
        student_data["Оценка за дисциплину"] = "Удовлетворительно"
    else:
        student_data["Оценка за дисциплину"] = "Неудовлетворительно"

def display_results(student_scores, num_krms):
    table = PrettyTable()
    table.field_names = ["ФИО", *[f"КРМ {i}" for i in range(1, num_krms + 1)],
                         "Рейтинг промежуточной аттестации",
                         "Рейтинг текущего контроля",
                         "Рейтинг по дисциплине",
                         "Оценка за дисциплину"]

    for student_data in student_scores.values():
        row_data = [student_data["ФИО"]]
        for i in range(1, num_krms + 1):
            row_data.append(student_data[f"Рейтинг КРМ {i}"])
        row_data.extend([
            student_data["Рейтинг промежуточной аттестации"],
            student_data["Рейтинг текущего контроля"],
            student_data["Рейтинг по дисциплине"],
            student_data["Оценка за дисциплину"]
        ])
        table.add_row(row_data)
    with open("output1.txt", "w") as file:
        file.write(str(table))
    # Вывод результатов в консоль закомментирован
    # print(table)

if __name__ == "__main__":
    main()
