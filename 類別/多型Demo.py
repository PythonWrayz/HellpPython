# 拉到最下方看 demo
from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# 由於 Python 是 dynamic language，執行不檢查型別
# 所以TextBox, DropDownList 不做繼承也是可以做實現多型

# 多型 demo
def draw(controls):
    for control in controls:
        control.draw()


textBox = TextBox()
dropDownList = DropDownList()
draw([textBox, dropDownList])
