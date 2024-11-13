class StepValueError(ValueError):
    pass
class Iterator():
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step != 0:
            self.step = step
        else:
            raise StepValueError ('шаг не может быть равен 0')
        self.pointer = self.start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.pointer
        self.pointer += self.step
        if self.step > 0 and self.start < self.stop and num <= self.stop:
            return num
        elif self.step < 0 and self.start > self.stop and num >= self.stop:
            return num
        elif self.step > 0 and self.start > self.stop:
            print("Итерация не возможна, измените шаг на противоположный, возможно вы перепутали "
                  "местами значение стоп и старт")

        raise StopIteration()



        pass

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()