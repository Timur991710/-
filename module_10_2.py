import threading
import time

from libpasteurize.fixes.fix_imports2 import power_onename


class Knight(threading.Thread):
    def __init__(self, name: str, power: int ):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
    def run(self):
        count = 100
        print(f'{self.name} на нас напали!')
        x = 1
        while count:

            time.sleep(1)
            y = count - self.power
            print(f'{self.name} сражается {x} день(дня)..., осталось {y} воинов.')
            x +=1
            count -= self.power
        print(f"{self.name} одержал победу спустя {x-1} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
second_knight.start()
first_knight.start()
second_knight.join()