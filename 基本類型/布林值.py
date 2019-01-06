# Python boolean 首字必須為大寫
is_right = True
is_right = False

# Falsy: "", 0, None, []
print(bool(""))
print(bool(0))
print(bool(None))
print(bool([]))

# Truthy: 除 Falsy 都是 True
print(bool(1))
# 注意：以下也是 True
print(bool(-1))
print(bool("None"))
print(bool("False"))
