import sys
sys.stdin = open("sample_input (8).txt")

def down(arr):
    pass


def dfs(i,j,root):
    global reservation_boom
    if root == N:
        return


    for dx, dy in direction:
        k = arr[i][j]
        while reservation_boom:
            for _ in range(len(reservation_boom)):
                reservation_boom.pop(0)
                for l in range(k):
                    nx = i + dx * (k)
                    ny = j + dy * (k)
                    if 0<= nx<H and 0<=ny<W and arr[nx][ny] !=0:
                        reservation_boom.add((nx,ny))
                        i, j = nx, ny
                        arr[nx][ny] = 0
                        dfs(nx,ny,root +1)
                        arr[nx][ny] = arr[i][j]

    for x, y in reservation_boom:
        arr[x][y] = 0

    down(arr)




T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(H)]
    # print(arr)
    reservation_boom = set()
    direction = [(0,1), (0,-1), (1,0), (-1,0)]
    for j in range(W):
        for i in range(H):
            if arr[j][i] != 0:
                # reservation_boom.add((i,j))
                dfs(i, j, 0)