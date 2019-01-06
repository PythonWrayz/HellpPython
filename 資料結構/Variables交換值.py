# 請交換 a, b 的值
a = 10
b = 11
# 以往寫法是要有第三個變數來進行操作
# Python 只要一行 code，透過的是 Tuple 特性
a, b = b, a
print(a, b)
# Why? 攤開數字可以這麼看
# Tuple 寫法其中一個就是這樣，parameter, parameter = value, value
a, b = 11, 10
