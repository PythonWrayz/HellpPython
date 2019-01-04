# 比較運算子
10 > 1
10 < 11
10 == 10
10 >= 10
10 <= 10

# 三元運算子 Ternary Operator
age = 9
# if age > 10:
#     message = "Eligible"
# else:
#     message = "Not eligible"
message = "Eligible" if age > 10 else "Not eligible"
print(message)

# 邏輯運算子 Logical Operator
high_income = True
good_credit = True
student = False

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

if not student:
    print("Eligible")

if (high_income or good_credit) and not student:
    print("Eligible")

# Chaining Comparison Operator
# 如果要寫一個判斷是 年紀要介於 20 到 65 歲之間
age = 22
# 一般語言寫法
if age >= 20 and age < 65:
    print("Adult")

# Python 可以用數學表示寫法，這就是 Chaining Comparison Operator
if 20 <= age < 65:
    print("Adult")
