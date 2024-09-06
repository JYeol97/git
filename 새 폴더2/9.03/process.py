import sys

sys.stdin = open("sample_input (4).txt")

def DFS(cr_lst, cell, i, connected, wire_length):
    global mx, max_connected

    if i == len(cr_lst):
        # 현재 연결된 코어의 수가 더 많거나, 같은 경우에 더 짧은 전선 길이로 갱신
        if connected > max_connected or (connected == max_connected and wire_length < mx):
            max_connected = connected
            mx = wire_length
        return

    dx = [0, 1, 0, -1]  # 우 하 좌 상
    dy = [1, 0, -1, 0]  # 우 하 좌 상
    now_i = cr_lst[i][0]
    now_j = cr_lst[i][1]

    # 코어를 연결하지 않는 경우
    DFS(cr_lst, cell, i + 1, connected, wire_length)

    # 각 방향에 대해 탐색
    for k in range(4):
        q = []
        for l in range(1, N):
            nx = now_i + dx[k] * l
            ny = now_j + dy[k] * l
            if 0 <= nx < N and 0 <= ny < N:
                if cell[nx][ny] == 0:
                    cell[nx][ny] = 2
                    q.append([nx, ny])
                else:
                    break
            else:
                break

        # 유효한 위치가 있을 경우 탐색 진행
        if q:
            DFS(cr_lst, cell, i + 1, connected + 1, wire_length + len(q))
            # 상태를 복원하기 위해 원래 상태로 되돌림
            for x, y in q:
                cell[x][y] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cell = [list(map(int, input().split())) for _ in N]
    cr_lst = []
    mx = float("inf")
    max_connected = 0

    for i in range(N):
        for j in range(N):
            if cell[i][j] == 1:
                # 가장자리에 위치한 코어는 이미 전원이 연결된 것으로 간주하고 리스트에 추가하지 않음
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    max_connected += 1
                else:
                    cr_lst.append([i, j])

    DFS(cr_lst, cell, 0, max_connected, 0)
    print(mx)
