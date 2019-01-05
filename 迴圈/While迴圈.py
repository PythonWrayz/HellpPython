# While 迴圈需要條件成立才執行
number = 100
while number > 0:
    print(number)
    number //= 2

# While 迴圈可以透過 break 關閉
number = 10
while True:
    print(number)
    number //= 2
    if number > 0:
        break
