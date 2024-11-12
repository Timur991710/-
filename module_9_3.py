from logging import fatal

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
zip_1 = zip(first, second)
first_result  = ((len(i[0]) -  len(i[1])) for i in zip_1 if len(i[0]) !=  len(i[1]))
second_result = (True if len(first[i]) ==  len(second[i]) else False for i in range(3))
print(list(first_result))
print(list(second_result))

