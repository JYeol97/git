import sys

sys.stdin = open("sample_input (12).txt")


def permutation(i, j, s):
    global stack_set
    if len(s) == 7:
        stack_set.add(s)
        return

    dx = [0, 1, 0, -1]  # 우 하 좌 상
    dy = [1, 0, -1, 0]

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            permutation(ni, nj, s + arr[ni][nj])


def chk():
    for i in range(4):
        for j in range(4):
            permutation(i, j, arr[i][j])



N = int(input())
for tc in range(1, N+1):
    arr = [list(input().split()) for _ in range(4)]
    stack_set = set()

    chk()
    print(f'#{tc} {len(stack_set)}')
