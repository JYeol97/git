import sys
sys.stdin = open("s_input.txt")

def init_set(N):
    a = list(range(N+1))
    return a

def find_parent(x):
    if parent[x] == x:
        return x

    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    nx = find_parent(x)
    ny = find_parent(y)


    parent[nx] = ny

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    relationship = [list(map(int, input().split())) for _ in range(M)]

    parent = init_set(N)
    # print(parent)
    for i in range(0, M):
        union(relationship[i][0], relationship[i][1])

    for j in range(M-1,-1,-1):
        union(relationship[j][0], relationship[j][1])

    print(f'#{tc} {len(set(parent))-1}')