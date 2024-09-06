import sys

sys.stdin = open('sample_input (16).txt')


dx = [0, 1, 0, -1]  # 우 하 좌 상
dy = [1, 0, -1, 0]  # 우 하 좌 상


def find_max():
    mx = 0
    mx_lst = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] > mx:
                mx = maps[i][j]
                mx_lst = [[i, j]]  # 최대값 갱신 시 리스트 초기화
            elif maps[i][j] == mx:
                mx_lst.append([i, j])
    return mx_lst


def asdf(i, j, K, length):
    global max_length
    if length > max_length:
        max_length = length
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < N and 0 <= nj < N:
            if maps[i][j] > maps[ni][nj]:
                stack.append([ni, nj])
                asdf(ni, nj, K, length + 1)
                stack.pop()

            elif maps[i][j] <= maps[ni][nj]:
                if maps[i][j] > maps[ni][nj] - K:
                    maps[ni][nj] -= K
                    stack.append([ni, nj])
                    asdf(ni, nj, 0, length + 1)
                    maps[ni][nj] += K
                    stack.pop()



T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    dct = {}
    max_length = 0
    stack = []
    mx = -999999999999
    start_lst = find_max()

    for i in range(len(start_lst)):
        x, y = start_lst[i]
        asdf(x, y, K, 1)

    print(max_length)