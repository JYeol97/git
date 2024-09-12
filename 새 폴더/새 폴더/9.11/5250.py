# 0,0 -> 2,2
import sys
sys.stdin = open("sample_in.txt")

from heapq import heappop, heappush

def dijstra(arr, N, start_x, start_y):
    visited = [[False] * N for _ in range(N)]
    min_heap = [(0, [start_x, start_y])]
    # print(min_heap)
    dist = [[float('inf')] * N for _ in range(N)]
    dist[start_x][start_y] = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while min_heap:
        cost, node = heappop(min_heap)

        if visited[node[0]][node[1]]:
            continue

        visited[node[0]][node[1]] = True

        for k in range(4):
            ni = node[0] + dx[k]
            nj = node[1] + dy[k]
            if 0<= ni < N and 0 <= nj <N:
                new_dist = cost + 1
                if arr[node[0]][node[1]] < arr[ni][nj]:
                    new_dist += arr[ni][nj] - arr[node[0]][node[1]]

                if dist[ni][nj] > new_dist:
                    dist[ni][nj] = new_dist
                    heappush(min_heap, (new_dist, [ni,nj]))

    return dist



T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = dijstra(arr, N, 0, 0)
    print(f'#{tc} {dist[-1][-1]}')
