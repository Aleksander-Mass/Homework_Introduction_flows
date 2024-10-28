# # Импорты необходимых модулей и функций
import time
from time import sleep
from threading import Thread

# Функция для записи слов в файл
def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза в 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Вызов функций с аргументами
# # Взятие текущего времени
start_time_functions = time.perf_counter()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# # Взятие текущего времени
end_time_functions = time.perf_counter()

# # Вывод разницы начала и конца работы функций
print(f"Работа функций {end_time_functions - start_time_functions:.6f} секунд")

# Создание потоков для параллельного запуска
threads = [
    Thread(target=write_words, args=(10, 'example5.txt')),
    Thread(target=write_words, args=(30, 'example6.txt')),
    Thread(target=write_words, args=(200, 'example7.txt')),
    Thread(target=write_words, args=(100, 'example8.txt'))
]

# Замер времени начала работы потоков
start_time_threads = time.perf_counter()

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Замер времени окончания работы потоков
end_time_threads = time.perf_counter()

# # Вывод разницы начала и конца работы потоков
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")

###   Вывод на консоль:
"""
Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Работа функций 34.184374 секунд
Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Работа потоков 20.116048 секунд
"""