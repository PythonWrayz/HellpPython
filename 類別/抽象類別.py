from abc import ABC, abstractmethod

# 特性和熟悉的抽象類別相同，不能建立實體，繼承需被實作
# 抽象類別兩個步驟：1. import ABC, abstractmethod 2. @abstractmethod


class Stream(ABC):
    @abstractmethod
    def read(self):
        pass


class MemoryStream(Stream):
    def read(self):
        print("Read data from memory")


m = MemoryStream()
m.read()
