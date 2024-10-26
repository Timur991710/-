from logging.config import valid_ident
import math
from encodings.punycode import selective_find


class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides, filled: bool = False):  # палитра и стороны
        self.__color = color
        self.__side = list(sides)
        self.filled = filled

    def get_color(self):
        return [*self.__color]

    def _is_valid_color(self, r, g, b):
        v = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        s = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return v and s

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
            return True

    def set_sides(self, *sides):
        if len(sides) == 1:
            sides = sides[0]
            valid_sides = []
            for side in range(self.sides_count):
                if self.__is_valid_sides(sides):
                    valid_sides.append(sides)
            self.__side = valid_sides

    def get_sides(self):
        return self.__side

    def __len__(self):
        return sum(self.__side)



class Circle(Figure):
    sides_count = 1
    def __init__(self, color: tuple[int, int, int], *hieght: int, filled: bool = False):
        if len(hieght) > 1:
            hieght =1
        else:
            hieght = hieght[0]
        self.hieght = hieght
        super().__init__(color,hieght, filled = filled)

    def radius_l(self):
        self.__radius = self.hieght / 2*math.pi
        self.__radius = int(self.__radius)
        return  self.__radius



class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple[int, int, int], *hieght, filled: bool = False):
        if len(hieght) != self.sides_count:
            if len(hieght) == 1:
                hieght = hieght[0]
                triangle_hieght = [hieght] * 3
            else:
                hieght = 1
                triangle_hieght = [hieght] * 3
        else:
            triangle_hieght = hieght
        super().__init__(color, *triangle_hieght, filled=filled)

    def square(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        p = (1/2) * (a + b + c)
        s = math.sqrt(p *(p - a) * (p - b) * (p - c))
        if s > 1:
            return int(s)
        else:
            return round(s, 2)




class Cube(Figure):
    sides_count = 12
    def __init__(self, color: tuple[int, int, int], *hieght, filled: bool = False):
        if len(hieght) == 1:
            hieght = hieght[0]
        else:
            hieght = 1
        cub_hieght = [hieght] * 12
        super().__init__(color,*cub_hieght, filled = filled)

    def get_volume(self):
        v = self.get_sides()[0] ** 3
        return v

if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 12)
    tri = Triangle( (100, 120, 50), 12, 13)
    print(tri.get_sides())

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 6)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))
    print(tri.square())

    # Проверка объёма (куба):
    print(cube1.get_volume())