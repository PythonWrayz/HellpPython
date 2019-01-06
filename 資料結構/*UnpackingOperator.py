# 使用 * 可解包 list，跟 JavaScript 的 ... 一樣
first = [1, 2, 3]
print(*first)
# 更多操作，包含可解包 str（Python特殊）
values = [*range(5), *"Hello"]
print(values)

# 使用 ** 可解包 dict，重複的 key 會被後者取代
first = {"x": 1}
second = {"x": 10, "y": 20}
combined = {**first, **second, "z": 1}
print(combined)
