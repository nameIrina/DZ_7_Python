from data_import import data_import
from data_export import data_export
from data_print import data_print
import data_search as fc

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_num = input("Введите телефон: ")
    return [last_name, first_name, phone_num]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Что сделать:\n\
    1 - импорт;\n\
    2 - экспорт справочника;\n\
    3 - поиск контакта.")
    
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        data_import(input_data(), sep)
    
    elif ch == '2':
        data_print(data_export())
    
    elif ch == '3':
        line = fc.find()
        data_print(line)
   
