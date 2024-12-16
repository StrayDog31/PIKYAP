import main
from operator import itemgetter
import unittest


class TestMainMethods(unittest.TestCase):
    def test_first_task_method(self):
        test_list = [('second', 'second', 'second'), ('first', 'first', 'first'), ('third', 'third', 'third')]
        result = main.first_task(test_list)
        reference = sorted(test_list, key=itemgetter(0))
        self.assertEqual(result, reference)

    def test_second_task_method(self):
        test_list = [('A. Mercer', 120000, 'Resource department'), ('R. Gosling', 110000, 'Archive department'),
                     ('E. Yeger', 80000, 'Resource department'), ('C. Nolan', 130000, 'Logistic department')]
        result = main.second_task(test_list)
        reference = [('Resource department', 2), ('Archive department', 1), ('Logistic department', 1)]
        self.assertEqual(result, reference)

    def test_third_method(self):
        test_list = [('A. Mercer', 120000, 'Resource department'), ('R. Gosling', 110000, 'Archive department'),
                     ('E. Yeger', 80000, 'Resource department'), ('C. Nolan', 130000, 'Logistic department')]
        result = main.third_task(test_list, 'r')
        reference = [('A. Mercer', 'Resource department'), ('E. Yeger', 'Resource department')]
        self.assertEqual(result, reference)
