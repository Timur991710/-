def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return (f"{a}{b}")

print(add_everything_up(123456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


try:
    def add_everything_up(a, b):
        return a + b
except TypeError:
    print (f"{a}{b}")

print(add_everything_up(123456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
