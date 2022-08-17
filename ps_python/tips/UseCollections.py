from collections import Counter

arr = [int(input()) for _ in range(10)]

val = Counter(arr).most_common()

print(val)