from heapq import heappush, heappop
import sys

sys.stdin = open("re_sample_input.txt")


def result(x1, y1, x2, y2, E):
    # 거리의 제곱에 환경 부담 세율을 곱함
    return E * ((x1 - x2) ** 2 + (y1 - y2) ** 2)


def prim(start):
    hq = []
    visited = [False] * N
    total_cost = 0
    num_edges = 0

    heappush(hq, (0, start))  # (가중치, 정점)

    while hq and num_edges < N:
        cost, u = heappop(hq)

        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost
        num_edges += 1   # 섬 갯수 새기

        x, y = island[u]

        for v in range(N):
            if not visited[v]:
                next_x, next_y = island[v]
                edge_cost = result(x, y, next_x, next_y, E)
                heappush(hq, (edge_cost, v))

    return total_cost


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]  # x, L
    E = float(input())

    island = [(arr[0][i], arr[1][i]) for i in range(N)]

    mst_cost = prim(0)

    print(f'#{tc} {round(mst_cost)}')
