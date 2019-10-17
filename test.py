import unittest
from my_calc import Calculator

class TestCalc(unittest.TestCase):
    '''Тесты проверки функций калькулятора'''
    # Сложение
    def test_composition(self):    
        self.assertEqual(Calculator(5, 7, '+').calculate(), 12)

    # Вычитание 
    def test_subtruction(self): 
        self.assertEqual(Calculator(5, 7, '-').calculate(), -2)

    # Умножение
    def test_multiply(self): 
        self.assertEqual(Calculator(5, 7, '*').calculate(), 35)

    # Деление
    def test_division(self): 
        self.assertEqual(Calculator(35, 7, '/').calculate(), 5)

    # Целочисленное деление (div)
    def test_div(self): 
        self.assertEqual(Calculator(36, 5, 'div').calculate(),   7)

    # Целочисленное деление (//)
    def test_div_2(self): 
        self.assertEqual(Calculator(36, 5, '//').calculate(),   7)

    # Вычисление остатка от деления (mod)
    def test_mod(self): 
        self.assertEqual(Calculator(36, 5, 'mod').calculate(),   1)

    # Вычисление остатка от деления (%)
    def test_mod_2(self): 
        self.assertEqual(Calculator(36, 5, '%').calculate(),   1)

    # Возведение в степень (pow)
    def test_pow(self): 
        self.assertEqual(Calculator(2, 12, '**').calculate(),   4096)

    # Возведение в степень (pow)
    def test_pow_2(self): 
        self.assertEqual(Calculator(2, 12, 'pow').calculate(),   4096)

    '''Общая проверка обработки исключений'''
    # Операции с отрицительными числами
    def test_negative_numbers(self): 
        self.assertEqual(Calculator(-2, 13, '*').calculate(), -26)

    # Ввод строковых значений вместо вещественных
    def test_str_input(self): 
        self.assertEqual(Calculator('aaa', 12, '*').calculate(),   "Ошибка ввода: должно быть введено число")

    # Ввод несуществующей функции
    def test_absent_function(self):
        self.assertEqual(Calculator(-2, 12, 'func').calculate(),   "Операция не поддерживается в калькуляторе")

    # Деление на 0 (для операции /)
    def test_zero_division_error(self): 
        self.assertEqual(Calculator(7, 0, '/').calculate(),   "Деление на 0!")

    # Деление на 0 (для операции div)
    def test_zero_div_error(self): 
        self.assertEqual(Calculator(7, 0, 'div').calculate(),   "Деление на 0!")

    # Деление на 0 (для операции mod)
    def test_zero_mod_error(self): 
        self.assertEqual(Calculator(7, 0, '%').calculate(),   "Деление на 0!")

if __name__ == '__main__':    
    unittest.main()
