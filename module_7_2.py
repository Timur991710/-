from os import write
from pprint import pprint


def custom_write(file_name, strings):
    trings_positions = {}
    line_number = 1
    file = open(file_name, 'w')
    for i in strings:

        l_byte = file.tell()
        file.write("f{strings}\n")
        trings_positions[(line_number, l_byte)] = i
        line_number +=1
    file.close()
    return trings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
    result = custom_write('.venv/test.txt', info)
    for elem in result.items():
        print(elem)


