import sys

sys.stdin = open("input.txt")


def abs(root,k):
    global stack
    if root == lc:
        return print(*stack)

    for k in range(lc):
        if visited[k] == 0:
            visited[k] = 1
            stack.append(card[k])
            abs(root + 1, k)
            visited[k] = 0
            stack.pop(-1)


T = int(input())

for tc in range(1, T + 1):
    card = list(map(int, input()))
    lc = len(card)
    visited = [0] * lc
    stack = []
    root = 0
    a = 0
    stack_set = set()
    k = 0
    abs(root,k)
