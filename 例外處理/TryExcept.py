# Python 的 try/catch
# exception 可以上 https://docs.python.org/3/library/exceptions.html 查詢
# try:
#     pass
# except expression as identifier:
#     pass
# else:
#     pass
# finally:
#     pass

try:
    age = int(input("Age: "))
except ValueError as ex:
    print("請輸入數字")
    print(ex)
    print(type(ex))
else:
    print("沒有錯誤，成功執行")

# For Loop 裡面配合 break 也可以放 else

# 如果想抓多種 Exception 類型
try:
    age = int(input("Age: "))
    10 / age
except ValueError:
    print("請輸入數字")
except ZeroDivisionError:
    print("數字不可為 0")

# 另一種
try:
    age = int(input("Age: "))
    10 / age
except (ValueError, ZeroDivisionError):
    print("請輸入合法數字")

# 情境：檔案被打開還沒關閉就拋 Exception，怎麼做才會一定關閉檔案？
try:
    file = open("../app.py")
    age = int(input("Age: "))
    10 / age
except (ValueError, ZeroDivisionError):
    print("enter valid number please.")
else:
    print("no exception were thrown")
finally:
    file.close()
