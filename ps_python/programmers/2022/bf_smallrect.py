# brute force _ 최고 직사각형 _ level1
import sys
input = sys.stdin.readline

# [[60, 50], [30, 70], [60, 30], [80, 40]]	
sizes_len = int(input())
sizes = [list(map(int, input().split())) for _ in range(sizes_len)]
w, h = 0, 0

for s in range(len(sizes)):
    if sizes[s][0] > sizes[s][1]:
        sizes[s][0], sizes[s][1] = sizes[s][1], sizes[s][0]
    w = max(w, sizes[s][0])
    h = max(h, sizes[s][1])

answer = w*h
# print(answer)