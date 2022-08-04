# input output 연습
import sys

# a = sys.stdin.readline() # 한 줄 입력
# b = list(map(int, sys.stdin.readline().split()))

# 2차원 배열 입력받기
input1 = []
N = int(sys.stdin.readline())
# for i in range(N):
#     input1.append(list(map(int, sys.stdin.readline().split())))
input1 = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

print(input1)

# 문자열 입력받아서 list에 넣게

input2 = []
N = int(sys.stdin.readline())
input2 = [sys.stdin.readline().strip() for i in range(N)]
# strip()는 문자열 맨 앞과 맨 끝의 공백문자를 제거한다.

print(input2)