def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) < 2:
        return first







print(get_multiplied_digits(40503))
rez = get_multiplied_digits(40503)
print(rez)




