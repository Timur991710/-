from random import choice
number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
number2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
i = choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(i)
sequence = []
for j in number1:
    for k in number1:
        if j > k:
            continue
        if j != k and i % (j + k) == 0:
            sequence.append(j)
            sequence.append(k)
        else:
            continue
print('Ключь: ', i, ' ', 'Пароль: ', str(sequence)[1:-1].replace(", ", ""))

