# Animal: Parent, Base
# Human: Child, Sub
# 繼承就只要類別宣告的時候 class Sub(Base)
# PS: 所有的 class 都是繼承 object class


class Animal:
    def __init__(self):
        self.tast = "meat"

    def eat(self):
        return "eat"


class Human(Animal):
    # overriding 建構式，如果 Base Constructor 也要執行的話，就要用 super()
    def __init__(self):
        super().__init__()
        self.age = 30

    def walk(self):
        return "walk"


human = Human()
print(human.tast)
print(human.eat())
print(human.walk())
print(human.age)
