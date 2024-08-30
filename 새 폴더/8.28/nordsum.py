import sys
sys.stdin = open("sample_input (5).txt")

def change(root, N):
    global tree
    if root > N:
        return tree

    change(root*2, N)
    change(root*2+1, N)
    if tree[root]==0:
        tree[root] = tree[root*2] + tree[root*2+1]
    return tree

T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split())) # N:노드의 개수  M:리프노드의 개수  L:출력할 노드 번호
    arr = [list(map(int, input().split())) for _ in range(M)]
    j = 1
    tree = [0]*(N+2)
    for i in range(len(arr)):
        tree[arr[i][0]] = arr[i][1]

    a = change(j, N)
    print(f'#{tc} {a[L]}')

