import random
first = 'Мама мыла раму'
second = 'Рамена мало было'

sov = lambda x, y: True if x == y else False
print(list(map(sov, first, second)))

def get_advanced_writer(file_name):
        def write_everything(*data_set):
            with open('example.txt', 'r+', encoding="UTF-8", ) as file_name:
                for i in data_set:
                    i = str(i)
                    file_name.write(i + '\n')
        return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall():
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())