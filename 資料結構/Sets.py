# https://docs.python.org/2/library/sets.html?highlight=set#module-sets
# The sets module provides classes for constructing and manipulating
# unordered collections of unique elements.
# Common uses include membership testing,
# removing duplicates from a sequence, and
# computing standard math operations on sets such as intersection, union, difference, and symmetric difference.

# sets 模組提供用於構造和操作獨特元素的無序集合的類別。
# 常見用途包括成員資格測試，從序列中刪除重複項，以及計算集合上的標準數學運算，例如交集，聯集，差異和對稱差異。

# set
default_set = {1, 5}
# 使用 Comprehensions 建立
values = {x for x in range(5)}
print(values)
# 刪除重複項
numbers = [1, 1, 2, 3, 4, 4]
no_duplicate_set = set(numbers)
print(no_duplicate_set)
# 聯集
print(default_set | no_duplicate_set)
# 交集
print(default_set & no_duplicate_set)
# left outter join
print(no_duplicate_set - default_set)
# outter join
print(default_set ^ no_duplicate_set)

if 1 in default_set:
    print("yes")

# set 不支援 index
# default_set.index(1)
