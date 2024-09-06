import sys
sys.stdin = open("input (2).txt")


def binary_search(target, A):
    low = 0
    high = N - 1
    flag = 0
    while low <= high:
        mid = (low + high)//2

        if target == A[mid]:
            return 1

        elif A[mid] > target:
            if flag == 1:
                break
            high = mid - 1
            flag = 1

        elif A[mid] < target:
            if flag == 2:
                break
            low = mid + 1
            flag = 2
    return 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N : A 정수의 갯수  M : B 정수의 갯수

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(M):
        result = binary_search(B[i], A)
        cnt += result

    print(f'#{tc} {cnt}')



