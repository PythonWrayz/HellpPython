# 封裝屬性
# https://www.programiz.com/python-programming/property


class Product:
    def __init__(self, name, price):
        self._name = name
        self.set_price(price)

    # Pythonic 封裝寫法: 建議作法
    @property
    def name(self):
        return self._name

    # 如果沒有 setter，屬性就變成唯讀
    @name.setter
    def name(self, value):
        self._name = value

    # 另一種 Pythonic 封裝法
    # getter
    def get_price(self):
        return self._price

    # setter
    def set_price(self, value):
        if value < 0:
            raise ValueError("價格不可為負數")
        self._price = value

    # property 結合 get 和 set 給變數，成為屬性
    price = property(get_price, set_price)


product = Product("Ray", 10)
print(product.name)
print(product.price)
# product.price = -1
