# if 語法幾點特別注意
# 1. 以往有 () 表示條件的 expression，Python 也不用，而是用 : 做為條件 expression 結束
# 2. 以往有 { } 表示條件成立後的 expression 範圍，Python 也不用 { }，而是用縮排

temperature = 35

if temperature > 30:
    print("It's warm.")
print("This Line Always Print.")

temperature = 15
if temperature > 30:
    print("It's warm.")
elif temperature > 20:
    print("It's nice.")
else:
    print("It's cold")

print("Done")

# 三元 Ternary Operator
age = 9

# if age > 10:
#     message = "Eligible"
# else:
#     message = "Not eligible"

message = "Eligible" if age > 10 else "Not eligible"

print(message)
