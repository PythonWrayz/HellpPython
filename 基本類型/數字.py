# Python 有 3種 Number
import math

x = 1  # int
y = 3.33  # float
z = 1 + 2j  # a + bi: Complex number，就像數學公式

# 運算子
print(10 + 1)
print(10 - 1)
print(10 * 3)
print(10 / 3)  # 得到 float 的相除結果
print(10 // 3)  # 得到商數
print(10 % 3)  # 得到餘數
print(10 ** 3)  # 得到 10 * 10 * 10 = 1000

# 可以將運算子結合 = 使用
x = 10
x += 3  # x = x + 3
print(x)

# 四捨五入
print(round(2.6))
# 四捨五入 + 指定小數位
print(round(2.26, 1))
# 絕對值
print(abs(-1))

# 更複雜的數學方法，就要載入模組 import math
# 可自行查找 Python 3 math module
math.ceil(2.2)
