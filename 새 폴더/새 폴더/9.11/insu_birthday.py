import sys

sys.stdin = open("input (2).txt")
from heapq import heappush, heappop


def dijkstra(start, arr):
    visited = [False] * (N + 1)
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, node = heappop(q)

        if visited[node] == True:
            continue

        visited[node] = True

        for next_node, next_cost in arr[node]:
            if dist[next_node] > cost + next_cost:
                dist[next_node] = cost + next_cost
                heappush(q, (dist[next_node], next_node))

    return dist


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [[] * M for _ in range(N + 1)]

    arr_reverse = [[] * M for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        arr[x].append((y, c))
        arr_reverse[y].append((x, c))

    dist = dijkstra(K, arr)
    dist_r = dijkstra(K, arr_reverse)

    max_cost = 0

    for j in range(1,N + 1):
        chk_cost = dist[j] + dist_r[j]
        max_cost = max(max_cost, chk_cost)

    print(f'#{tc} {max_cost}')
