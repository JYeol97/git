import sys
sys.stdin = open("sample_input (7).txt")

def partition(left, right):
    pivot = ai[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and ai[i] <= pivot:
            i += 1

        while i <= j and ai[j] >= pivot:
            j -= 1

        if i < j:
            ai[i], ai[j] = ai[j], ai[i]

    ai[left], ai[j] = ai[j], ai[left]

    return j


def quick_sort(left, right):
    if left < right:
        pivot = partition(left, right)

        quick_sort(left, pivot-1)
        quick_sort(pivot + 1, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    N2 = N//2
    quick_sort(0, N-1)
    print(f'#{tc} {ai[N2]}')

    # if N % 2 == 0:
    #     print(f'#{tc} {ai[N2]}')
    #
    # else:
    #     print(f'#{tc} {ai[N2-1]}')
