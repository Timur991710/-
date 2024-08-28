from numbers import Number
import re

def Factorial():
    num = int(input('Введите целое число: '))
    x = 1
    for i in range(1, num + 1):
      x = i * x
    print(x)
Factorial()

def Searching_for():
    word = str(input('Введите любое предложение: '))
    Glas = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    Word =[]
    Word1 =[]
    for i in Glas:
        matches = re.finditer(i, word)
        indices = [match.start() for match in matches]
        Word.append(indices)
        if i in word:

            Word1.append(i)
        else:
            continue
    y = (len(sum(Word, [])))
    print('Количество повторений: ', y, 'Гласные: ', Word1)

Searching_for()


