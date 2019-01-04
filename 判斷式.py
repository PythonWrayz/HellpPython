# if 語法幾點特別注意
# 1. if expressiong 後面要加 :
# 2. if 條件成立後內容沒有實用上下括號表示範圍，而是用縮排

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
