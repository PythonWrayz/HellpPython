# List
list1 = [1, 2, 3]
list2 = [4, 5]
# 內容可以不同型別
list3 = [1, "1"]
# 結合 concat 就這麼簡單
print(list1 + list2)
# 懶得在 [] 打同樣的值無數遍
print([2] * 10)

# list() 讓屬於 Iterable 型別的物件 to list
items = list(range(20))
print(items)
# 長度
print(len(items))
# [-1] 代表從最後一個數來第一個
print(items[-1])
# List[ : ] 可以 return 範圍內的 List，預設範圍為第一個到最後一個
print(items[1:2])
# return 從倒數第一個到最後一個
print(items[-1:])
# List[::] 第二個 : 可以指定 return 的 List 要間隔幾個 item 再取下一個
print(items[::2])
# 變倒序
print(items[::-1])

# List Unpacking 解包變成個別 item
customers = ["a", "b", "c", "d"]
# old way
print(customers[0])
# Python way
first, second, third, fourth = customers  # 左邊變數個數必須跟 List 內個數相同
print(first)
first, *others = customers
print(first)
print(others)
first, *others, last = customers
print(first)
print(others)
print(last)

# 使用 enumerate(List) + 迴圈，每一個 item 都會有 index
for item in enumerate(customers):
    print(f"index: {item[0]}")
    print(list(item))
for index, customer in enumerate(customers):
    print(index, customer)

# List 增加 item
customers.append("e")  # 直接加在最後面
customers.insert(0, "123")  # 指定位置
print(customers)
# List 移除 item: 原始 List 會有變動
# 透過 index 移除，使用 pop
last_customer = customers.pop()
third_customer = customers.pop(2)
print(customers)
# 透過指定值移除，使用 remove
customers.remove("a")
print(customers)
# 透過指定範圍移除，使用 del
del customers[0]
del customers[0:1]
print(customers)
# 全部清除
customers.clear()
