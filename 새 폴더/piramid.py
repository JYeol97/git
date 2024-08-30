import sys

sys.stdin = open("sample_in.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for i in range(N):
        s = 0
        for j in range(M):
            if matrix[i][j] == 1:
                s += 1

            if mx < s:
                mx = s

            elif matrix[i][j] == 0:
                if mx < s:
                    mx = s
                s = 0

    matrix = list(map(list,zip(*matrix)))

    for i in range(M):
        s = 0
        for j in range(N):
            if matrix[i][j] == 1:
                s += 1

            if mx < s:
                mx = s

            elif matrix[i][j] == 0:
                if mx < s:
                    mx = s
                s = 0


    if mx == 1:
        print(f'#{tc} 0')

    else:
        print(f'#{tc} {mx}')
