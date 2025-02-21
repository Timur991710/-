from pprint import pprint


class Product():
    def __init__(self, name: str, weight: float, category: str, ):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
        pass

class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        __file_name = open(self.__file_name, "r+")
        pro_read = __file_name.read()
        __file_name.close()
        return pro_read


    def  add(self, *products):
        file_get = self.get_products()
        for i in products:
            if (self.get_products().find(f"{i.weight}") or self.get_products().find(f"{i.name}")) == -1:
                file = open(self.__file_name, "a")
                file.write(f'{i}\n')
                file.close()
            else:
                print((f"Продукт {i} уже существует"))

        pass

if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())