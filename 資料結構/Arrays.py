from array import array

# array 比起 list 較佔記憶體以及會強制型別，但執行上更有效率
# 建議碰到效能調教的時候再考慮將 list 變成 array
# array 初始化要指定型別，請參考 https://docs.python.org/2/library/array.html
numbers = array('i', [1, 2, 3])
print(numbers)
# 操作上跟 list 一樣
print(numbers[0])
# 唯一的不同，array 有指定型別，所以不能 assign 其它型別的 value 進去
# numbers[0] = "string"
