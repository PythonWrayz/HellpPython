# dict
point = {"x": 1, "y": 2}
# 建議寫法
point = dict(x=1, y=2, z=3)
print(point["x"])
# 使用 comprehensions 建立
values = {x: x * 2 for x in range(5)}
print(values)
# 修改值
point["x"] = 10
print(point["x"])
# 如果 key 不存在 dict，會報錯，所以
if "z" in point:
    print(point["z"])
# 更好的取值方法
print(point.get("x"))
print(point.get("a"))  # None
print(point.get("a", 0))  # 可像 SQL 的 ISNULL 設定預設值
# 刪除
del point["x"]
print(point)
# for loop 操作
for key in point:
    print(key, point[key])
# 用 items 方法
for item in point.items():
    print(item)
# items() + tuple 特性
for key, value in point.items():
    print(key, value)
