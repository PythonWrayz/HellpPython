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
    def walk(self):
        return "walk"


human = Human()
print(human.tast)
print(human.eat())
print(human.walk())
