# 9093 문장 뒤집기

def main():
    input_num()
    return

def input_num():
    n = int(input())
    for i in range(n):
        solve()

def solve():
    st = input()
    answer = ''
    st_list = st.split(' ')
    for i in range(len(st_list)):
        print(''.join(reversed(st_list[i])), end= ' ')

    print(answer)


if __name__ == "__main__":
	main()