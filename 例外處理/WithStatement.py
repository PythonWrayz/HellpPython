# with expression as target:
#     pass

# 只要物件有兩個屬性：__enter__、__exit__
# 使用 with, Python 就會自動去呼叫這兩個方法

# 這解決什麼？
# 例外處理檔案關閉的時候，通常會放 finally
# 但是另一種方式，在開檔案的時候用 with, 當程式執行結束以後，Python 就會自動呼叫 __exit__ 關閉它
try:
    with open("../app.py") as file:
        print("file opened")
    value = int(input("Age: "))
    10 / value
except (ValueError, ZeroDivisionError):
    print("請輸入正確數字")
else:
    print("沒有錯誤，正常執行")

# with 裡面也可以開多個檔案
with open("../app.py") as file, open("../筆記.md") as note:
    print("file opened")
