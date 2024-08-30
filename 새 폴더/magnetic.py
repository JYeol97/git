import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(str, input().split()))

    H = N//2

    if N %2 == 0:
        arr1 = arr[:H]
        arr2 = arr[H:]
    elif N%2 != 0:
        arr1 = arr[:H+1]
        arr2 = arr[H+1:]
    lst = []
    for i in range(H):
        lst.append(arr1[i])
        lst.append(arr2[i])

    if len(arr) % 2 != 0:
        lst.append(arr1[-1])

    print(f'#{tc}',*lst)


for i in range(N):
    print(i, end="")