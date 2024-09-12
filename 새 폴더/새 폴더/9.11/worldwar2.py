import sys

sys.stdin = open("input (1).txt")

from heapq import heappush, heappop


def dijkstra(start):
    hq = []
    start_x, start_y = start
    distance = [[float('inf')] * N for _ in range(N)]
    distance[start_x][start_y] = 0
    heappush(hq, (0, start_x, start_y))

    while hq:
        dist, x, y = heappop(hq)

        if x == N-1 and y == N-1:
            return distance

        if distance[x][y] < dist:
            continue

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_dist = dist + arr[nx][ny]

                if new_dist >= distance[nx][ny]:
                    continue

                distance[nx][ny] = new_dist
                heappush(hq, (new_dist, nx, ny))
                # print(distance)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    direction = [(-1,0),(0,-1),(0, 1), (1, 0)]
    start = [0, 0]
    a = dijkstra(start)

    print(f'#{tc} {a[-1][-1]}')
