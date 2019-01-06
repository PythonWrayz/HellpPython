# Tuple 特性是 readonly list：無法被 modify
# 使用 Tuple 的時機，我認為跟 C# 使用 readonly 關鍵字的理由相同，從外部注入且不允許被修改的 list
tuple1 = (1, 2)
tuple2 = 1, 2
print(type(tuple2))
tuple3 = 1,
print(type(tuple3))
empty_tuple = ()
print(type(empty_tuple))

# 其他的初始操作都跟 List 相同
tuple4 = tuple([1, 2])
print(tuple4)
tuple5 = tuple("Hello")
print(tuple5)
tuple6 = (1, 2) + (3, 4)
print(tuple6)
tuple7 = (1, 2) * 2
print(tuple7)
print(tuple7[0])
print(tuple7[0:2])
x, y, a, b = tuple7
if 10 in tuple7:
    print("exists")
