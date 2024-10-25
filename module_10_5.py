import multiprocessing
from time import *


def read_info(name):
    all_data = []
    file = open(name, 'r')
    for _ in file:
        all_data.append(file.readline())


if __name__ == '__main__':
    files_names = ['D:\\Files\\file 1.txt', 'D:\\Files\\file 2.txt', 'D:\\Files\\file 3.txt', 'D:\\Files\\file 4.txt']
    now = time()
    for f in files_names:
        read_info(f)
    end = time()
    print(f'{end - now} (линейны)')
    with multiprocessing.Pool(processes=4) as pool:
        now = time()
        pool.map(read_info, files_names)
    end = time()
    print(f'{end - now}  (многопроцессный)')
