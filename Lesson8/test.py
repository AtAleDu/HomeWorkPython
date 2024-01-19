import unittest
from unittest.mock import patch
from io import StringIO
from BRS import generate_scores, calculate_discipline_rating, determine_grade

class ТестСистемыОценок(unittest.TestCase):
    def test_equal_weights(self):
        num_students = 3
        num_krms = 4

        # Веса всех КРМ равны 1
        krms_weights = [1] * num_krms

        # Генерируем оценки для студентов
        with patch("builtins.input", side_effect=["Иван Иванов", "Елена Петрова", "Александр Сидоров"]):
            student_scores = generate_scores(num_students, num_krms)

        # Рассчитываем итоговые оценки с весами КРМ равными 1
        final_scores = calculate_discipline_rating(student_scores, krms_weights)

        # Проверяем, что итоговые оценки верны
        expected_results = {
            "Иван Иванов": "Хорошо",
            "Елена Петрова": "Отлично",
            "Александр Сидоров": "Удовлетворительно"
        }

        for student_name, expected_grade in expected_results.items():
            with self.subTest(student_name=student_name):
                self.assertEqual(final_scores[student_name]["Оценка за дисциплину"], expected_grade)

if __name__ == "__main__":
    unittest.main()
