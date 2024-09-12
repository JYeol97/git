import sys

sys.stdin = open("sample_input (5).txt")


def find_set_case(x):
    global cnt
    if x == parent[x]:
        if visited[x]:
            visited[x] = False
            cnt += 1
            return

    return


def find_set(x):
    if x == parent[x]:
        return x

    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    nx = find_set(x)
    ny = find_set(y)

    parent[nx] = ny
    # parent[nx] = ny

    return parent


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = list(range(N + 1))
    visited = [True] * (N + 1)
    cnt = 0
    for i in range(M):
        union(arr[i * 2], arr[(i * 2) + 1])

    # print(arr)
    for j in range(1, len(parent)):
        find_set_case(j)

    print(f'#{tc} {cnt}')
