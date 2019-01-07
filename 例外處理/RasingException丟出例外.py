# rasie 可在自己的 function 裡面拋出對應 exception
# exception 可以上 https://docs.python.org/3/library/exceptions.html 查詢

# 基本上不建議
# 1. 之前寫 C# 也不會到處放 throw exception，exception 應該透過流程避免...
# 2. raise 其實耗效能


def demo(number):
    if number <= 0:
        raise ValueError("數字不可小於等於 0")
    print(number)


try:
    demo(-1)
except ValueError as ex:
    print(ex)
