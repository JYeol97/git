import sys

sys.stdin = open("sample_input.txt")


# find_set : 가장 최상위 부모(그룹의 대표)를 찾아라
def find_set_num(x):
    global cnt
    # 기저 조건 : 자기 자신이 부모라면 종료..
    if x == parent[x]:
        if visited[x] == 0:
            visited[x] = 1
            cnt += 1
        return x

    # 그룹의 대표자(최상위 부모) 부모로 변경 (경로 압축)
    find_set_num(parent[x])
    return

# find_set : 가장 최상위 부모(그룹의 대표)를 찾아라
def find_set(x):
    global cnt
    # 기저 조건 : 자기 자신이 부모라면 종료..
    if x == parent[x]:
        return x

    # 그룹의 대표자(최상위 부모) 부모로 변경 (경로 압축)
    parent[x] = find_set(parent[x])
    return parent[x]


# union : x와 y가 속한 두 그룹을 하나로 합쳐라
def union(x, y):
    root_x = find_set(x)  # x의 대표자
    root_y = find_set(y)  # y의 대표자

    # if root_x != root_y:
    parent[root_x] = root_y


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [i for i in range(N + 1)]
    # print(arr) # [1, 2, 3, 4]
    # print(parent) # [0, 1, 2, 3, 4, 5]
    visited = [0] * (N + 1)
    cnt = 0
    for i in range(0, M):
        union(arr[i * 2], arr[i * 2 + 1])
    # init_set(arr)
    print(parent)
    for j in range(1, len(parent)):
        find_set_num(j)
    # print(f'#{tc} {cnt}')
