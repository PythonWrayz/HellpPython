# 單/雙引號都表示 string
course = "Python Programming"
sequences = 'Ray are a "LENGEN"'

# 3個雙引號用來表示換行文字段落
prase = """
Hi there, this is a test.
Testing good.
"""
print(prase)

# 使用 len() 取得字串長度
print(len(course))

# 使用 [] + index 取得指定字元
print(course[0])
# 最後一個字元
print(course[-1])

# 使用「:」取得 a-n 字元
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

# 跳脫字元
print("\"跳脫字元\"")
print("\'跳脫字元\'")
print("\\跳脫字元\\")
# 換行
print("Python \nProgramming")

# format string, 使用 f"" 再用{}裝變數（C# 用 $）
first = "Ray"
last = "Wu"
print(f"{first} {last}")
print(f"{len(first)} {last}")
print(f"{len(first)} {2 + 2}")

# 其他方法
course = "python programming"
print(course.upper())
print(course.lower())
print(course.title())
print("pro" in course)
print("pro" not in course)

course = "  python programming"
# 移除字串兩邊空白
print(course.strip())
# 移除字串左邊空白
print(course.lstrip())
# 移除字串右邊空白
print(course.rstrip())

# 取得 character index
print(course.find("p"))
print(course.find("PP"))

# 取代
print(course.replace("p", "j"))
