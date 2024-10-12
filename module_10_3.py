from threading import Thread, Lock
from random import randint
from time import sleep


class Bank(Thread):

    def __init__(self):
        super(Bank, self).__init__()
        self.balance = 0
        self.new_balance = 0

    lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                sleep(0.001)
            popolnenie = randint(50, 100)
            self.balance += popolnenie
            sleep(0.001)
            print(f'Пополнение: {popolnenie}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            snyatie = randint(50, 100)
            print(f'Запрос на {snyatie}')
            if snyatie <= self.balance:
                self.balance -= snyatie
                print(f'Снятие: {snyatie}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
