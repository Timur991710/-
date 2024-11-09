def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    try:
        for i in numbers:
            try:
                result = result + i
            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
                incorrect_data = incorrect_data + 1
    except TypeError:
        return (f"Переданные данные не являются списком {numbers}")

    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        x = personal_sum(numbers)
        l = len(numbers) - x[1]
        sr_aref = x[0] / l
        return sr_aref
    except ZeroDivisionError:
        return 0
    except TypeError:
        print ('В numbers записан некорректный тип данных')
        return None





print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
