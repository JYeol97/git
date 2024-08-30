import sys

sys.stdin = open("sample_input (6).txt")


def change(root, N):
    global cnt
    if root > N:
        return

    change(root * 2, N)
    tree[root] += cnt
    cnt += 1
    change((root * 2) + 1, N)
    return tree


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)
    cnt = 1
    i = 1
    a = change(i, N)

    print(f'#{tc} {tree[1]} {tree[N//2]}')
