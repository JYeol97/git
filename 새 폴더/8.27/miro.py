import sys
sys.stdin = open("input (3).txt")

def findtwo(matrix):
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                return i, j

def findthird(matrix):
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 3:
                return i, j

def findend(matrix, endi, endj):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    starti, startj = findtwo(matrix)
    q = [[starti, startj]]
    visited = [[0 for _ in range(16)] for _ in range(16)]
    while q:
        si, sj = q.pop(0)
        visited[si][sj] = 1
        if matrix[si][sj] == matrix[endi][endj]:
            return 1

        for k in range(4):
            ni, nj = si + dx[k], sj + dy[k]
            if 0 <= ni < 16 and 0 <= nj < 16 and matrix[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
    return 0

T = 10
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]
    endi, endj = findthird(matrix)
    a = findend(matrix, endi, endj)
    print(f'#{tc} {a}')
