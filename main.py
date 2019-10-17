import sys  
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QDoubleValidator as DoubleValidator
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

import simple_calc_with_file_btn
from my_calc import Calculator, CalculatorResult
from file_manager import write_string_to_file, get_full_file_path

'''
Класс для взаимодействия с элементами интерфейса
'''
class SimpleCalculatorApp(QtWidgets.QMainWindow, simple_calc_with_file_btn.Ui_MainWindow):
    def __init__(self):                
        super().__init__()        
        self.setupUi(self)
        # Задать иконку окну с
        icon_file_name = get_full_file_path(r'files\calc_icon.png')
        self.setWindowIcon(QtGui.QIcon(icon_file_name))
        # подключение клик-сигнала к слоту и вызов функции calc()
        self.calculate_btn.clicked.connect(self.calc)

        # подключение клик-сигнала к слоту и вызов функции save_row()
        self.save_file_btn.clicked.connect(self.save_row)

        # Масшабирование текста в label
        self.number_a_lbl.adjustSize()
        self.number_b_lbl.adjustSize()
        self.operation_lbl.adjustSize()

        # Меняем текст
        self.number_a_input.setPlaceholderText("Введите число А")
        self.number_b_input.setPlaceholderText("Введите число В")
        self.operation_input.setPlaceholderText("Введите операцию")

        # Задаем валидацию (только вещественные числа)
        dbl_validator = DoubleValidator()
        self.number_a_input.setValidator(dbl_validator)
        self.number_b_input.setValidator(dbl_validator)

        # Зададим количество столбцов в таблице
        self.result_table.setColumnCount(4)
        # Задаем заголовки столбцов в таблице
        self.result_table.setHorizontalHeaderLabels(
            ('Число А', 'Число В', 'Операция', 'Результат')
        )
        # Зададим тип выделения строки в таблице
        self.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Растянем последнюю колонку до конца виджета таблицы
        self.result_table.horizontalHeader().setStretchLastSection(True)

    '''
    Посчитать результат для введенных значений
    '''
    def calc(self):
        # Получим значение из полей ввода
        a = self.number_a_input.displayText()
        b = self.number_b_input.displayText()
        operation = self.operation_input.displayText()

        # Создать запись калькулятора
        new_calc = Calculator(a, b, operation)

        # посчитать результат вычисления калькулятора
        result = new_calc.calculate()

        print(new_calc.calculate())

        # Создадим и заполним новую строку с результатом в таблице
        self.create_new_row(str(a), str(b), str(operation), str(result))

        # Почистим ячейки
        self.number_a_input.setText('')
        self.number_b_input.setText('')
        self.operation_input.setText('')

    '''
    Создать и заполнить новую строку 
    '''
    def create_new_row(self, str_a, str_b, str_operation, str_result):
        # Занесем таблицу в переменную
        table = self.result_table

        # Посчитаем строки в таблице
        row = table.rowCount()
        print(row)

        # определим индекс новой строки
        new_row_index = 0 if row == 0 else row

        # Добавить строку в таблицу        
        table.insertRow(new_row_index)
        table.selectRow(new_row_index)

        # Получить добавленную строку
        current_row = table.currentRow()
        print(current_row)

        # Создадим ячейки для записи в таблицу
        a_cell = self.create_table_cell(str_a)
        table.setItem(current_row, 0, a_cell)

        b_cell = self.create_table_cell(str_b)
        table.setItem(current_row, 1, b_cell)

        operation_cell = self.create_table_cell(str_operation)
        table.setItem(current_row, 2, operation_cell)
        
        result_cell = self.create_table_cell(str_result)
        table.setItem(current_row, 3, result_cell)

    '''
    Создать ячейку только для чтения
    '''
    def create_table_cell(self, cell_input):
        cell_info = QTableWidgetItem(cell_input)
        # Только для чтения
        cell_info.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        )
        return cell_info

    '''
    Сохранить данные в файл (выделенную строку)
    '''
    def save_row(self):
        table = self.result_table
        current_row = table.currentRow()
        if (current_row != -1):
            a = table.item(current_row, 0).text()
            b = table.item(current_row, 1).text()
            operation = table.item(current_row, 2).text()
            result = table.item(current_row, 3).text()
            calc_result = CalculatorResult(a, b, operation, result)
            self.write_file(calc_result.get_data_str())

    def write_file(self, result_str):
        print(result_str)
        write_string_to_file(r'files\Result.txt', result_str)

'''
Инициализируем класс для запуска кода
'''
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = SimpleCalculatorApp()
    window.show()
    app.exec_()

# Точка входа в приложение
if __name__ == '__main__':    
    main()

