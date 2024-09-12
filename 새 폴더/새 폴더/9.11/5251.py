from heapq import heappop, heappush

import sys
sys.stdin = open("sample_input (4).txt")
T = int(input())

def dijkstra(start):
    hq = []


    heappush(hq, (0, start))  # 0 은 누적값 (초기값)
    distance[start] = 0
    while hq:
        dist, now = heappop(hq)   # 값, 위치

        if distance[dist] < now:
            continue


        for next in graph[dist]:
            next_node = next[0]
            cost = next[1]

            new_cost = cost + now

            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heappush(hq, (next_node, new_cost))


for tc in range(1, T+1):
    N, E = map(int,input().split())
    graph = [[] for _ in range(E)]
    distance = [float('inf')] * (N+1)
    # print(graph)
    for i in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    # arr = [list(map(int, input().split())) for _ in range(E)]
    dijkstra(0)
    # print(graph)
    print(f'#{tc} {distance[-1]}')







