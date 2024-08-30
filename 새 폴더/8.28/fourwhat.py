import sys

sys.stdin = open("input (5).txt")

T = 10


def inorder(root):
    if root == 0:
        return

    inorder(left[root])
    print(parent[root], end="")
    inorder(right[root])


for tc in range(1, T + 1):
    N = int(input())
    arr = [None] * (N + 1)

    left = [0] * (N + 2)
    right = [0] * (N + 2)
    parent = [0] * (N + 2)
    for _ in range(N):
        arrs = list(map(str, input().split()))
        if len(arrs) == 4:
            parent[int(arrs[0])] = arrs[1]
            left[int(arrs[0])] = int(arrs[2])
            right[int(arrs[0])] = int(arrs[3])
        elif len(arrs) == 3:
            parent[int(arrs[0])] = arrs[1]
            left[int(arrs[0])] = int(arrs[2])

        else:
            parent[int(arrs[0])] = arrs[1]
    print(f'#{tc}', end =" ")
    inorder(1)
    print()
