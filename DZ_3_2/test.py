from main import is_valid_expression
import unittest

# Остальной код тестов оставляем без изменений


# Остальной код тестов оставляем без изменений

class TestExpressionValidation(unittest.TestCase):
    def test_valid_expressions(self):
        valid_expressions = [
            "a+b+c",
            "(a*b)/z+f",
            "a+(b*c)",
            "(x+y)*z/w",
            "a1+b2*c3",
            "a+b*c-d/e"
        ]
        for expression in valid_expressions:
            with self.subTest(expression=expression):
                self.assertTrue(is_valid_expression(expression))

    def test_invalid_expressions(self):
        invalid_expressions = [
            "a+b+c+",
            "(a*b)/z+f)",
            "a+(b*c",
            "x+y*z)/w",
            "a1+b2*c3+",
            "a+b*c-d/e*"
        ]
        for expression in invalid_expressions:
            with self.subTest(expression=expression):
                self.assertFalse(is_valid_expression(expression))

if __name__ == '__main__':
    unittest.main()
