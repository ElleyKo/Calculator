import os

'''
Запись в файл

@param filename - имя файла
@param row_array - массив данных строки таблицы
'''
def write_string_to_file(filename, save_string):
    file_name_to_save = get_full_file_path(filename)
    with open(file_name_to_save,'a',encoding = 'utf-8') as resultFile:
        resultFile.write(save_string)
        resultFile.write('\n')

'''
Получить полный путь до файла
@param filename - наименование файла
@returns путь до файла с заданным наименованием
'''
def get_full_file_path(filename):
    file_dir = os.path.abspath(os.path.dirname(__file__))
    file_to_save = os.path.join(file_dir, '..', filename)
    return file_to_save
