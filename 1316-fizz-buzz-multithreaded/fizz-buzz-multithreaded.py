from typing import Callable
import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.cv = threading.Condition()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.i <= self.n and not (self.i % 3 == 0 and self.i % 5 != 0):
                    self.cv.wait()
                if self.i > self.n:
                    self.cv.notify_all()
                    return
                printFizz()
                self.i += 1
                self.cv.notify_all()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.i <= self.n and not (self.i % 5 == 0 and self.i % 3 != 0):
                    self.cv.wait()
                if self.i > self.n:
                    self.cv.notify_all()
                    return
                printBuzz()
                self.i += 1
                self.cv.notify_all()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.i <= self.n and not (self.i % 15 == 0):
                    self.cv.wait()
                if self.i > self.n:
                    self.cv.notify_all()
                    return
                printFizzBuzz()
                self.i += 1
                self.cv.notify_all()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.cv:
                while self.i <= self.n and not (self.i % 3 != 0 and self.i % 5 != 0):
                    self.cv.wait()
                if self.i > self.n:
                    self.cv.notify_all()
                    return
                printNumber(self.i)
                self.i += 1
                self.cv.notify_all()
