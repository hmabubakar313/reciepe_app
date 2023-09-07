from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 4), 6)

    
    def test_subtract(self):
        res = calc.subtract(2, 4)
        self.assertEqual(res, 2)

