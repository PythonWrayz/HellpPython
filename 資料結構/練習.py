# 題目：取得重複最多次的字元
sentence = "This is a common interview question"
# Mosh way
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda item: item[1],
    reverse=True)
print(char_frequency_sorted[0])

# my way(no good)
sets = set(sentence)
dicts = {c: 0 for c in sets}
for c in sentence:
    if c in sets:
        dicts[c] += 1
lists = []
for key, count in dicts.items():
    lists.append((key, count))
lists.sort(key=lambda item: item[1], reverse=True)
print(lists[0])
