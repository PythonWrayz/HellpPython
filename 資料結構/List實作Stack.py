# Stack 堆疊: FILO (First In Last Out / Last In First Out)
user_sessions = []
user_sessions.append("a")
user_sessions.append("b")
# List 空的時候用 pop 會報錯，所以 if 先確認 List 是否為空
if user_sessions:
    user_sessions.pop()
if not user_sessions:
    print("Empty")
print(user_sessions)
