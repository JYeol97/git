import sys

sys.stdin = open("sample_input (10).txt")

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    lst = ''
    while N != 0:
        N = N * 2
        if N >= 1:
            lst += '1'
            N -= 1
        else:
            lst += '0'
    if len(lst) > 12:
        print(f'#{tc} overflow')

    else:
        print(f'#{tc} {lst}')
