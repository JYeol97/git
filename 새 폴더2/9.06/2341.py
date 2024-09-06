import sys

sys.stdin = open("sample_input (15).txt")

dxs = [1, 1, -1, -1]  # 1 2 3 4 분면 4 3 2 1
dys = [1, -1, -1, 1]  # 1 2 3 4 분면 4 3 2 1


def permutation(root):
    if root == N - 2:
        a = stack[::]
        return par_size_lst.append(a)

    for k in range(1, N - 1):
        stack.append(k)
        permutation(root + 1)
        stack.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rotate = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    par_size_lst = []
    permutation(0)

    for i in range(N - 2):
        for j in range(1, N - 1):
            for k in range(4):
                for p in range(len(par_size_lst) - 1, -1, -1):
                    nx = i + dxs[k] * par_size_lst[p][0]
                    ny = j + dys[k] * par_size_lst[p][1]