from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super(Knight,self).__init__()
        self.name = name
        self.power = power



    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        size_army = 100
        while size_army >= 0:
            day += 1
            if size_army > 0:
                size_army -= self.power
                print(f'{self.name} сражается {day} день(дня)..., осталось {size_army} воинов.')
                sleep(1)
            elif size_army == 0:
                print(f'{self.name} одержал победу спустя {day - 1} дней(дня)!')
                break

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')


