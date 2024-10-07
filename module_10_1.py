from time import *
from threading import *

def write_words(word_count, file_name):
    file = open(file_name, 'r+', encoding='UTF-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1} \n' )
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start_1 = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end_1 = time()
time_res_1 = time_end_1 - time_start_1
print(f'Работа потоков {time_res_1}')

time_start_2 = time()

thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=( 200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end_2 = time()
time_res_2 = time_end_2 - time_start_2

print(f'Работа потоков {time_res_2}')