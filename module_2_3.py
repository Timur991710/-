from operator import ifloordiv

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
numbers = len(my_list)
ind = 0
print(numbers)
while ind <= (numbers - 1):
    if my_list[ind] > 0:
        print(my_list[ind])
        ind = ind + 1
    elif my_list[ind] < 0:
        break
    elif my_list[ind] == 0:
        ind = ind + 1
        continue

else:
    print('Перебор списка окончен')