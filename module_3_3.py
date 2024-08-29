from math import factorial


def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['w', 1, 3.45]
values_dict = {'a': 123, 'b': [1, 2, 3], 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 =[1, 'Werden']

print_params(*values_list_2)
