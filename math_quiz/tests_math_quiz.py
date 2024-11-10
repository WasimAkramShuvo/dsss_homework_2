import unittest
from math_quiz import generate_random_integer, generate_random_operator, create_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        """Test if the function returns one of the valid operators ('+', '-', '*')."""
        valid_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random operator selections
            operator = generate_random_operator()
            self.assertIn(operator, valid_operators, f"Invalid operator generated: {operator}")


    def test_create_problem(self):
            test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (11, 6, '+', '11 + 6', 17),
            (11, 6, '-', '11 - 6', 5),
            (11, 6, '*', '11 * 6', 66)
        ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem_statement, answer = create_problem(num1, num2, operator)
                self.assertEqual(problem_statement, expected_problem, f"Problem statement {problem_statement} does not match expected {expected_problem}")
                self.assertEqual(answer, expected_answer, f"Answer {answer} does not match expected {expected_answer}")

if __name__ == "__main__":
    unittest.main()
