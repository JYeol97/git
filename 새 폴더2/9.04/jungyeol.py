import sys

sys.stdin = open("sample_input (6).txt")


def merge_sort(ai):
    global cnt
    if len(ai) == 1:
        return ai

    mid = len(ai) // 2
    left = merge_sort(ai[:mid])
    right = merge_sort(ai[mid:])
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)


def merge(left, right):
    # 두 리스트를 병합할 결과 리스트를 초기화
    result = [0] * (len(left) + len(right))
    l = r = 0  # 왼쪽 리스트와 오른쪽 리스트의 인덱스

    # 두 리스트를 순차적으로 비교하여 작은 값을 결과 리스트에 추가
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 요소들을 결과 리스트에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 리스트에 남은 요소들을 결과 리스트에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    # 병합된 결과 리스트를 반환
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    cnt = 0
    ai = merge_sort(ai)
    b = ai[N // 2]
    print(f'#{tc} {b} {cnt}')
