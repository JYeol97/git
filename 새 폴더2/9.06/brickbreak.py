import sys

sys.stdin = open("sample_input (13).txt")


def boom(t, lst):
    if t == N:
        return

    dx = [0, 1, 0, -1]  # 우 하 좌 상
    dy = [1, 0, -1, 0]  # 우 하 좌 상

    boom_lst = []
    now_lst = lst[0]
    for k in range(4):
        i = now_lst[0]
        j = now_lst[1]
        l = now_lst[2]
        for r in range(1, l + 1):
            ni = i + dx[l] * r
            nj = j + dy[l] * r
            if 0 <= ni < W and 0 <= nj < H and arr[ni][nj] != 0:
                boom_lst.append([ni, nj, arr[ni][nj]])
    return boom_lst


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())  # W : 가로    H : 세로

    arr = [list(map(int, input().split())) for _ in range(H)]

    # 복제하기
    q = []
    for i in range(len(arr)):
        q.append(arr[i])
    # 맨 위에 있는 벽돌의 리스트
    # print(q)

    lst = []
    for j in range(W):
        for i in range(H):
            if arr[i][j] != 0:
                lst.append([i, j, arr[i][j]])
                break

    print(boom(0, lst))
