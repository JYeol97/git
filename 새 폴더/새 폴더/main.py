import sys
sys.stdin = open("sample_input (7).txt")

def dfs(core_idx, connected_cores, wire_length):
    global max_connected_cores, min_wire_length

    if core_idx == len(cores):
        if connected_cores > max_connected_cores:
            max_connected_cores = connected_cores
            min_wire_length = wire_length
        elif connected_cores == max_connected_cores:
            min_wire_length = min(min_wire_length, wire_length)
        return

    x, y = cores[core_idx]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        temp_wire_length = 0
        while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            arr[nx][ny] = 2
            temp_wire_length += 1
            nx += dx
            ny += dy

        if nx < 0 or nx >= N or ny < 0 or ny >= N:  # Reached the edge
            dfs(core_idx + 1, connected_cores + 1, wire_length + temp_wire_length)

        # Revert the grid
        while temp_wire_length:
            nx -= dx
            ny -= dy
            arr[nx][ny] = 0
            temp_wire_length -= 1

    # Consider not connecting this core
    dfs(core_idx + 1, connected_cores, wire_length)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cores = [(i, j) for i in range(1, N - 1) for j in range(1, N - 1) if arr[i][j] == 1]
    max_connected_cores = 0
    min_wire_length = float('inf')
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    dfs(0, 0, 0)
    print(f"#{tc} {min_wire_length}")