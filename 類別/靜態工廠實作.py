#!/bin/python3
from abc import ABCMeta, abstractmethod

n = int(input())


class Printer(metaclass=ABCMeta):
    def __init__(self, n):
        self.number = n

    @abstractmethod
    def printing(self):
        pass


class OddPrinter(Printer):
    def printing(self):
        print("Weird")


class EvenPrinter(Printer):
    def printing(self):
        if self.number in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")


class PrinterCreator:
    @staticmethod
    def create_instance(n):
        remainder = n % 2
        return {
            0: EvenPrinter(n),
            1: OddPrinter(n),
        }[remainder]


printer = PrinterCreator.create_instance(n)
printer.printing()
