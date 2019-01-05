# Function 定義使用 def
def greet():
    print("Morning")


greet()

# 帶參數


def greeting(first_name, last_name):
    print(f"Morning! {first_name} {last_name}")


greeting("Ray", "Wu")

# return


def get_greet(name):
    return f"Hi, {name}"


print(get_greet("Ray"))
message = get_greet("Ray")
# 注意：function 沒有 return 的話，預設回傳 None
print(greet())


# 使用 keyword 讓程式更有可讀性


def increment(number, by):
    return number + by


print(increment(5, by=2))


# 選擇性參數：預設參數值，但必須放最後面


def default_increment(number, by=1):
    return number + by


print(default_increment(2))
print(default_increment(5, 2))


# *args 傳遞動態 Tuple 參數，Tuple 跟 [] 不同


def caculating(*numbers):
    print(numbers)
    total = 0
    for n in numbers:
        total += n
    print(total)


caculating(2, 5, 6)


# **args 傳遞動態 Dictionary 參數


def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="Ray", age=32)
