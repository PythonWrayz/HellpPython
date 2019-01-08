# 讓使用者輸入值，結果是字串
# 注意不能用runner快捷鍵執行，請打開 terminal 執行才能互動
# x = input("x: ")
# print(type(x))


# def fizz_buzz(input):
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     if input % 3 == 0 and input % 5 == 0:
#         return "FizzBuzz"
#     return input


# fizz_buzz(1)

# a = [1, 2, 3]
# a.append("str")
# a.insert(2, "b")
# print(a)

import requests

response = requests.get("http://www.google.com")
print(response)
