import threading
from multiprocessing import Pool
import time
import os

from requests.packages import target


def read_info(name):
    all_data =[]
    with open(name) as file:
        for i in file:
            if file.readline() != None:
                all_data.append(file.readline())




if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    x = time.time()
    for i in filenames:
        read_info(i)
    y = time.time()
    finish = y - x
    print(f'Время выполнения {finish} линейный процесс')

    x = time.time()
    with Pool(processes=5) as pool:
        pool.map(read_info, filenames)
    y = time.time()
    finish = y - x
    print(f'Время выполнения {finish} многопроцессорный процесс')