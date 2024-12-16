import unittest
from operator import itemgetter
from main import Book, Chapter, BookChap, task1, task2, task3

class TestBookChapterFunctions(unittest.TestCase):
    def setUp(self):
        self.books = [
            Book(1, "All Quiet on the Western Front"),
            Book(2, "Luftwaffe aces"),
            Book(3, "Achtung Panzer"),
        ]

        self.chapters = [
            Chapter(1, "Chapter 11", 43, 1),
            Chapter(2, "Chapter 24", 45, 2),
            Chapter(3, "Chapter 32", 61, 3),
            Chapter(4, "Chapter 47", 38, 2),
            Chapter(5, "Chapter 52", 47, 2),
            Chapter(6, "Chapter 27", 42, 1)
        ]

        self.book_chap = [
            BookChap(1, 1),
            BookChap(2, 2),
            BookChap(3, 3),
            BookChap(3, 4),
            BookChap(1, 5),
        ]

        self.one_to_many = [(ch.name, ch.length, bk.name)
                            for bk in self.books
                            for ch in self.chapters
                            if ch.book_chap_id == bk.id]

    def test_task1(self):
        expected = sorted(self.one_to_many, key=itemgetter(0))
        result = task1(self.one_to_many)
        self.assertEqual(result, expected)

    def test_task2(self):
        expected = [("Luftwaffe aces", 3),
                    ("All Quiet on the Western Front", 2),
                    ("Achtung Panzer", 1)]
        result = task2(self.one_to_many)
        self.assertEqual(result, expected)

    def test_task3(self):
        many_to_many_temp = [(bk.name, bc.book_chap_id, bc.ch_id)
                             for bk in self.books
                             for bc in self.book_chap
                             if bc.book_chap_id == bk.id]

        many_to_many = [(ch.name, ch.length, bk_name)
                        for bk_name, bk_id, ch_id in many_to_many_temp
                        for ch in self.chapters if ch.id == ch_id]

        expected = [("Chapter 47", 38)]  # Указывает на главы, которые действительно есть
        result = task3(many_to_many, '7')
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()