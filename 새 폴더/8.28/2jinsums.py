import sys
sys.stdin = open("sample_input (7).txt")

from heapq import heappush, heappop, heapify

def right(root, N):
    global sums
    if root <= 0:
        return
    if root >=N:
        return

    right((root//2), N)
    sums += arr2[root]
    return arr2




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr2 = []
    for i in range(N):
        heappush(arr2, arr[i])
    sums = 0

    arr2.insert(0,0)

    root = N//2
    right(root, N)
    print(f'#{tc} {sums}')


