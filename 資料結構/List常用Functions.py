# 以下介紹有 index、sort、sorted、map、filter、zip，對應labmda寫法

# Finding 尋找
numbers = [1, 2, 3]
print(numbers.index(1))
# 防呆，List 不存在要找的物件時，使用 index() 會錯，兩種方式防呆
if 1 in numbers:
    print(numbers.index(1))
if numbers.count(1) != 0:
    print(numbers.index(1))

# Sort 排序
# sort() 會改變原 List 的方法
numbers.sort()  # 正序
numbers.sort(reverse=True)  # 倒序
print(numbers)
# sorted() 不改變原 List，而是回傳 tuple 結果的方法
new_number = sorted(numbers)  # 正序
print(new_number)
new_number = sorted(numbers, reverse=True)  # 倒序
print(new_number)

# List 裡面裝 Tuple 時
items = [
    ("product1", 6),
    ("product2", 3),
    ("product3", 7),
]

# 尋找不能用 iterms.index("product1") 改用如下
for index, item in enumerate(items):
    if item[0] == "product2":
        print(index)

# 排序沒效果 items.sort()
# 要使用委派 Function


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
# 一樣可改用 lambda，倒序
items.sort(key=lambda item: item[1], reverse=True)
print(items)

# Map：什麼時候用？想要從 List 得到組合過的 List
# old way
prices = []
for item in items:
    prices.append(item[1])
print(prices)
# 使用 map()
prices = map(lambda item: item[1], items)
print(list(prices))

# Filter
filters = filter(lambda item: item[1] > 5, items)
print(list(filters))

# List Comprehensions，另一種高端寫法可改寫 Map、Filter
# 語法 [expression for item in List]
# 說明：從 for loop 得到的 item 可以在 expression 應用
maps = [item[1] for item in items]
print(maps)
# 語法 [expression1 for item in List if expression2]
# 說明：從 for loop 得到每一個 item，透過 if 判斷後的 item 可以在 expression1 應用
filters = [item for item in items if item[1] > 5]
print(filters)

# Zip，把多個 List “壓縮”成一個 List，以最少的 List 為限，裡面的 item 為對應出來的一組物件
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zips = zip(list1, list2)
print(list(zips))
zips = zip("ABC", list1, list2)
print(list(zips))
