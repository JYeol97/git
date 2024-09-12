import sys
sys.stdin = open("sample_input (7).txt")

def dfs(idx, connect_core, wire_length):
    global max_cores, min_wire

    if idx == len(cores):
        if connect_core > max_cores:
            max_cores = connect_core
            min_wire = wire_length

        elif connect_core == max_cores:
            min_wire = min(min_wire, wire_length)

        return

    x, y = cores[idx]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        temp_wire_length = 0
        while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            arr[nx][ny] = 2
            temp_wire_length += 1
            nx += dx
            ny += dy

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            dfs(idx + 1, connect_core + 1, wire_length + temp_wire_length)

        while temp_wire_length:
            nx -= dx
            ny -= dy
            arr[nx][ny] = 0
            temp_wire_length -= 1

    dfs(idx + 1, connect_core, wire_length)




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cores.append((i,j))

    max_cores = 0
    min_wire = 99999999999999999999999999
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    dfs(0,0,0)
    print(f'#{tc} {min_wire}')
