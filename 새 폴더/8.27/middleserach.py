import sys

sys.stdin = open("input (1).txt")

def soonhoi(root):
    if root==0:
        return

    soonhoi(left[root])
    print(word[root], end="")
    soonhoi(right[root])


T = 10
for tc in range(1, T+1):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    word = [''] * (N+1)
    for _ in range(N):
        arr = list(map(str,input().split()))
        if len(arr) ==2:
            A = int(arr[0])
            B = arr[1]
            word[A] = B

        elif len(arr) == 3:
            A = int(arr[0])
            B = arr[1]
            C = int(arr[2])
            word[A] = B
            left[A] = C

        elif len(arr) == 4:
            A = int(arr[0])
            B = arr[1]
            C = int(arr[2])
            D = int(arr[3])
            word[A] = B
            left[A] = C
            right[A] = D

    root = 1
    print(f'#{tc}',end=' ')
    soonhoi(root)
    print()