'''
Класс простого калькулятора
'''
class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        '''
        Вычислить выражение
        '''
        operation_array = {
            '+': self.composition,     # операция сложения
            '-': self.subtruction,     # операция вычитания
            '*': self.multiply,        # операция умножения
            '/': self.division,        # операция деления
            'mod': self.mod,           # операция вычисления остатка от деления
            '%': self.mod,             # операция вычисления остатка от деления
            'pow': self.pow_new,       # операция возведения в степень
            '**': self.pow_new,        # операция возведения в степень (предусмотрим другую запись)
            'div': self.div,           # операция целочисленного деления
            '//': self.div             # операция целочисленного деления (предусмотрим другую запись)
        }
        try:
            operation = self.operation
            checked = self.check_values()
            return operation_array[operation]() if checked == True else checked 
        except KeyError:
            return "Операция не поддерживается в калькуляторе"      

    def check_values(self):
        try:
            self.a = float(self.a)
            self.b = float(self.b)
            return True
        except ValueError:
            return "Ошибка ввода: должно быть введено число"

    def division (self):
        '''
        Операция деления
        '''
        try:
            a = self.a
            b = self.b
            return a / b
        except ZeroDivisionError:
            return "Деление на 0!"

    def multiply (self):
        '''
        Операция умножения
        '''
        a = self.a
        b = self.b
        return a * b

    def composition (self):
        '''
        Операция сложения
        '''
        a = self.a
        b = self.b
        return a + b

    def subtruction (self):
        '''
        Операция вычитания
        '''
        a = self.a
        b = self.b
        return a - b

    def mod (self):
        '''
        Операция вычисления остатка от деления
        '''
        try:
            a = self.a
            b = self.b
            return a % b
        except ZeroDivisionError:
            return "Деление на 0!"

    def pow_new (self):
        '''
        Операция возведения в степень
        '''
        a = self.a
        b = self.b
        return a ** b

    def div(self):
        '''
        Операция целочисленного деления
        '''
        try:
            a = self.a
            b = self.b
            return a // b
        except ZeroDivisionError:
            return "Деление на 0!"

class CalculatorResult:
    def __init__(self, a, b, operation, result):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = result

    def get_data_str(self):
        a = self.a
        b = self.b
        operation = self.operation
        result = self.result
        return '{0} {1} {2} = {3}'.format(a, operation, b, result)

if __name__ == "__main__":
    try:
        a = float(input())
        b = float(input())
    except ValueError:
        print("Ошибка ввода: должно быть введено число")
        raise SystemExit
    
    calc = Calculator(a, b, input())
    solution = calc.calculate()
    print(solution)
    