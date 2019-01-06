from collections import deque

# Queues 佇列：FIFO (Fist In First Out)
# 一般 Queue 很消耗記憶體，因為 List 第一個被移除，剩下的都要往左邊移動
# Python 可 import 一個模組 deque class 進行處理
queues = deque([])
queues.append(1)
queues.append(2)
print(queues)
if queues:
    queues.popleft()
print(queues)
if not queues:
    print("Empty")
