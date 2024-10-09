# Животное
from math import factorial


class Animal:


    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        self.food = food
        if food.edible == False:
            print(f"{self.name}, не стал есть {food.name}")
            self.alive = False
        else:
            print(f"{self.name}, съел  {food.name}")
            self.fed = True


# Растение
class Plant:

    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible

# Млекопитающее
class Mammal(Animal):
        pass

# Хищник
class Predator(Animal):
        pass

# Цветок
class Flower(Plant):
        pass

# Фрукт
class Fruit(Plant):
    def __init__(self, name, edible = True):
        self.name = name
        self.edible = edible

if __name__ == "__main__":
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
