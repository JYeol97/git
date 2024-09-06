import sys

sys.stdin = open("input (1).txt")


def check(stack, B, a):
    global mx
    if sum(stack) >= B:
        if mx > sum(stack):
            mx = sum(stack)
        return

    elif sum(stack) >= B and mx <= sum(stack):
        return

    else:
        for k in range(a, N):
            if visited[k] == 0:
                visited[k] = 1
                stack.append(top[k])
                check(stack, B, k)
                visited[k] = 0
                stack.pop()



T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    top = list(map(int, input().split()))
    visited = [0] * N
    stack = []
    mx = 200000000000000000000000000000000000000
    check(stack, B, 0)
    print(f'#{tc} {mx-B}')
