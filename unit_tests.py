import unittest # библиотека для создания тестов
from logic_and_smallgraphic import decimalToBinary, numAfterComm, fill_the_table # импорт тестируемых функции
import pandas as pd # библиотека для создания правильного примера таблицы истинности для теста
# таблица-пример для тестирования работы функции
table_test = pd.DataFrame(
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 1],
                [0, 0, 1, 0, 1],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 0, 0, 0],
                [1, 1, 0, 1, 0],
                [1, 1, 1, 0, 0],
                [1, 1, 1, 1, 0]
            ],
            columns=["A", "B", "C", "D", 'F']
        )


class Test_of_some_CSHfunc(unittest.TestCase):
    def test_decimalToBinary_ok(self):
        self.assertEqual(decimalToBinary(5), "101.0")

    def test_decimalToBinary_wrong(self):
        self.assertEqual(decimalToBinary("test"), 0)

    def test_numAfterComm_ok(self):
        self.assertEqual(numAfterComm(5.666, 6.555), 12)

    def test_numAfterComm_wrong(self):
        self.assertEqual(numAfterComm("test", "test2"), 0)

    def test_fill_the_table_ok(self):
        pd.testing.assert_frame_equal(fill_the_table("1111000011110000"), table_test)

    def test_fill_the_table_wrong(self):
        self.assertEqual(fill_the_table("testtesttesttest"), "Пожалуйста введите ровно 16 символов(0 или 1)")
