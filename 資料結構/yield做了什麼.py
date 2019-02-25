map(int, input().split())
t = tuple(map)
for i in t:
    print(t)  # 每一個 input 分割後的數字

# 這裡幾個問題
# 為什麼 map 可以直接用 tuple() 建立？
# 1. tuple() 需要什麼？
# 依照 Python3 文件這樣寫 tuple([iterable])
# 看底下的 2, 3，就可以知道為何 map() 可以接著使用 tuple 建立 tuple 物件

# 2. map() 回傳什麼？
# Return an iterator that applies function to every item of iterable, yielding the results.
# 重點在最後的 yielding the result
# 3. yield 做了什麼？
# yield 會暫存每次 loop 進來要產生的值，
# 所以每次 loop 不會執行 return，而是到最後才一口氣 return 所有的值，值都可被迭代 (iterable特性)


def xrange(n):
    x = 0
    print('進來了')  # 出現一次
    while x != n:
        yield x
        x += 1
        print('yield了')  # 出現 10 次


for n in xrange(10):
    print(n)  # 印出 yield 後的 x
