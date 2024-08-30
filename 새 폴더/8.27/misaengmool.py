import sys

sys.stdin = open('sample_input (3).txt')


def kill(K):
    K = K // 2
    return K


def change(x, y, k):
    if k == 1:
        k = 2
        return k

    elif k == 2:
        k = 1
        return k

    elif k == 3:
        k = 4
        return k

    elif k == 4:
        k = 3
        return k

def check(stack, stack2):
    result = 0
    for j in range(1, M + 1):
        while stack:
            for _ in range(K):
                x, y, k, d = stack.pop(0)  # 가는 방향
                nx = x
                ny = y
                if nx == 0 or ny == 0:
                    d = change(x, y, d)
                    k = kill(k)  # 미생물 컷
                nx = x + di[d]
                ny = y + dj[d]
                matrix[nx][ny] = k
                if k != 0:
                    stack2.append([nx, ny, k, d])
        stack = stack2

    return stack


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N : 한 변의 셀의 개수   M : 격리 시간    K : 미생물 군집의 개수
    lst = [list(map(int, input().split())) for _ in range(K)]  # 1 1 7 1

    matrix = [[0] * N for _ in range(N)]

    di = [0, 0, 1, 0, -1]
    dj = [0, 1, 0, -1, 0]
    stack = []
    stack2 = []
    for i in range(K):
        matrix[lst[i][0]][lst[i][1]] = lst[i][2]
        stack.append([lst[i][0], lst[i][1], lst[i][2], lst[i][3]])   # 세로, 가로, 미생물, 이동방향


    check(stack, stack2)