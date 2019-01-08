# for loop 可以倒出 Iterable 型別的物件，那有哪些是 Iterable？
# range(5), String, []
for i in range(5):
    print(i)

for x in "Python":
    print(x)

for item in [1, 2, 3]:
    print(item)
