# https://docs.python.org/3/reference/compound_stmts.html#for
# For Loop
for number in range(3):
    print("Attempt", number)
# 同樣結果，range 用不同簽章
for number in range(1, 4):
    print("Attempt", number)
# range 加 step 可以呈現 i + step 結果
for number in range(1, 6, 2):
    print("Attempt", number, number * "*")

# For...Else
# break 使用在 For/While loop，用來關閉迴圈以及跳過 else 條件（如果是 For...Else）
successful = True
for number in range(3):
    print("Attempt", number + 1)
    if successful:
        print("Success")
        break
else:
    print("Attempted 3 times and failed")

# 巢狀迴圈
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# 注意一件事情，Python For Loop 要 iterate 的清單可以在途中被修改，甚至增加/刪除
# 這樣的行為請避免，For Loop 每次 iterate 長度都會取清單現在長度，所以清單被刪除一個 item，那長度就會減 1，iterate 就會自動跳過原本的下一個 item
# 增加也是，這都是埋地雷的危險作法。
# 如果有需要修改清單，請複製一份另外操作


# 練習
count = 0
for i in range(1, 10):
    if i % 2 == 0:
        count += 1
        print(i)

print(f"We have {count} even number.")
