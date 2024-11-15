import threading
import time
import datetime


def write_words(word_count, file_name):
    with open(file_name, 'r+', encoding='utf-8') as file_name:
        words = "Какое-то слово №"
        for i in range(word_count):
            x = i +1
            file_name.write(f'{words}{x}\n')
            time.sleep(0.001)
        print(f"Завершилась запись в файл {file_name.name}. {threading.current_thread()}")



start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
execution_time = end_time - start_time
execution_time_1_1 = str(datetime.timedelta(seconds=execution_time))
print(f'Работа потоков {execution_time_1_1} секунды')

start_time_1 = time.time()
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_1.start()
thread_1.join()
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_2.start()
thread_2.join()
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_3.start()
thread_3.join()
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread_4.start()
thread_4.join()
end_time_1 = time.time()
execution_time_1 = end_time_1 - start_time_1
execution_time_1_2 = str(datetime.timedelta(seconds=execution_time_1))
print(f'Работа потоков {execution_time_1_2} секунды')



