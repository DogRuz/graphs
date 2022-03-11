from unittest import TestCase

from operation.utils import Calculate


class TestCalculate(TestCase):
    def test_add(self):
        calculate = Calculate(1, [[4, 3, 2, 4], [1, 1, 1, 1]])
        vector = calculate.execute()
        self.assertEqual(vector, [5, 4, 3, 5])

    def test_subtraction(self):
        calculate = Calculate(3, [[4, 3, 2, 4], [1, 1, 1, 1]])
        vector = calculate.execute()
        self.assertEqual(vector, [3, 2, 1, 3])

    def test_mul(self):
        calculate = Calculate(2, [[4, 3, 2, 4], [1, 1, 1, 1]])
        vector = calculate.execute()
        self.assertEqual(vector, [4, 3, 2, 4])

    def test_division(self):
        calculate = Calculate(4, [[4, 3, 2, 4], [1, 1, 1, 1]])
        vector = calculate.execute()
        self.assertEqual(vector, [4.0, 3.0, 2.0, 4.0])
