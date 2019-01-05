# Finding 尋找
numbers = [1, 2, 3]
print(numbers.index(1))
# 防呆，List 不存在要找的物件時，使用 index() 會錯，兩種方式防呆
if 1 in numbers:
    print(numbers.index(1))
if numbers.count(1) != 0:
    print(numbers.index(1))

# Sort 排序
# 會改變原 List 的方法
numbers.sort()  # 正序
numbers.sort(reverse=True)  # 倒序
print(numbers)
# 不改變原 List，而是回傳結果的方法
new_number = sorted(numbers)  # 正序
print(new_number)
new_number = sorted(numbers, reverse=True)  # 倒序
print(new_number)

# List 裡面裝 Tuple
items = [
    ("product1", 123),
    ("product2", 345),
    ("product3", 456),
]
