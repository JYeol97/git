import sys
sys.stdin = open("sample_input (3).txt")

from heapq import heappop, heappush

# def find_set(x):
#     # 기저 조건 : 자기 자신이 부모라면 종료..
#     if x == parent[x]:
#         return x
#
#     # 그룹의 대표자(최상위 부모) 부모로 변경 (경로 압축)
#     parent[x] = find_set(parent[x])
#     return parent[x]
#
#
# # union : x와 y가 속한 두 그룹을 하나로 합쳐라
# def union(x, y):
#     root_x = find_set(x)  # x의 대표자
#     root_y = find_set(y)  # y의 대표자
#
#     if root_x != root_y:
#         parent[root_x] = root_y



def dijstra(adj, E, start):
    global total_weight
    visited = [0] * E
    min_heap = [(0, start)]
    # dist = [float('inf') * V]
    mst = []
    # dist[start] = 0

    while min_heap:
        weight, moving = heappop(min_heap)

        if visited[moving] == 1:
            continue

        visited[moving] = 1
        mst.append(weight)

        for next_node, next_weight in adj[moving]:
            if visited[next_node] == 0:
                heappush(min_heap, (next_weight, next_node))

    return mst








T = int(input())
for tc in range(1, T+1):
    # N : 마지막 연결지점 번호  E : 도로의 개수
    V, E = map(int, input().split())
    adj = [[] for _ in range(E)]
    # arr = [list(map(int, input().split())) for _ in range(E)]
    # print(arr)
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v,w))
        adj[v].append((u,w))
    # parent = [0] * E
    total_weight = 0
    mst = dijstra(adj,E,0)
    print(f'#{tc} {sum(mst)}')