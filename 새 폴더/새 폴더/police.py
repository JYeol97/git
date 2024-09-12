import sys

sys.stdin = open("sample_input (4).txt")


def bfs(i, j, q):
    time = 1
    visited[i][j] = 1
    cnt = 1
    while q:
        if time == L:
            break
        time += 1
        for _ in range(len(q)):
            position = q.pop(0)
            for k in range(4):
                ni = position[0] + dx[k]
                nj = position[1] + dy[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if visited[ni][nj] == 0 and arr[ni][nj] != 0:
                        a = dct[arr[position[0]][position[1]]]
                        b = dct[arr[ni][nj]]
                        if a[k] == 1 and b[k - 2] == 1:
                            visited[ni][nj] = 1
                            q.append([ni, nj])
                            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    # N : 세로 M :가로 R : 맨홀 세로  C : 멘홀 가로  L : 시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = [[R, C]]

    dct = {
        1: [1, 1, 1, 1],  # 우 하 좌 상
        2: [0, 1, 0, 1],  # 우 하 좌 상
        3: [1, 0, 1, 0],
        4: [1, 0, 0, 1],
        5: [1, 1, 0, 0],
        6: [0, 1, 1, 0],
        7: [0, 0, 1, 1]
    }

    dx = [0, 1, 0, -1]  # 우 하 좌 상
    dy = [1, 0, -1, 0]  # 우 하 좌 상
    print(f'#{tc} {bfs(R, C, q)}')
