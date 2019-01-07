# https://docs.python.org/3/tutorial/classes.html


class MyClass:
    # 屬性
    default_color = "Red"

    # 建構式
    # 方法第一個 argument 要求放 self，Python 才會指向此 class
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.兩個底線算是 private
        self.__z = 9

    # classmethod 第一個 argument 指定為 cls，指向這個 class
    # 一種工廠方法回傳新的預設實體
    @classmethod
    def creat_instance(cls):
        return cls(0, 0)

    # 自訂方法
    def draw(self):
        print(f"Point: {self.x}, {self.y}")

    # Comparison magic method 改寫相等
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Comparison magic method 改寫大於
    # 同時 Python 會自動辨識小於是這個的相反條件
    def __gt__(self, other):
        return self.x > other.x

    # representing magic method 改寫顯示 str
    def __str__(self):
        return f"Point {self.x}, {self.y}"

    # arithmetic operators 改寫
    def __add__(self, other):
        return MyClass(self.x + other.x, self.y + other.y)


# 使用 class
# 若建構式沒有 argument：myClass = MyClass()
myClass = MyClass(1, 2)
defaultClass = MyClass.creat_instance()
# 檢查是否為 MyClass 型別
print(isinstance(myClass, MyClass))
print(myClass.x)
# 同 javascript 可直接新增&設置 class instance 屬性，其他實體不會被新增
myClass.check = True
print(myClass.check)
# 屬性
print(defaultClass.default_color)
myClass.default_color = "Yellow"
print(myClass.default_color)
# magic method 比較方法改寫
print(defaultClass == myClass)
print(defaultClass > myClass)
print(defaultClass < myClass)
# magic method str 改寫
print(str(myClass))
# arithmetic 運算子相加改寫
print(defaultClass + myClass)
# 半套的封裝
print(myClass._MyClass__z)  # 可叫出私有變數
print(myClass.__z)  # 這樣叫不出
