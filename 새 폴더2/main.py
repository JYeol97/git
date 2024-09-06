# def quick_sort(arr):
#     if len(arr) <= 1:  # 배열의 길이가 1 이하라면 이미 정렬된 상태
#         return arr
#
#     pivot = arr[len(arr) // 2]  # 중간 값을 피벗으로 선택
#     left = [x for x in arr if x < pivot]  # 피벗보다 작은 값들
#     middle = [x for x in arr if x == pivot]  # 피벗과 같은 값들
#     right = [x for x in arr if x > pivot]  # 피벗보다 큰 값들
#
#     return quick_sort(left) + middle + quick_sort(right)  # 정렬된 배열 합치기
#
#
# # 예제 배열 정렬
# arr = [3, 6, 8, 10, 1, 2, 1]
# sorted_arr = quick_sort(arr)
# print("정렬된 배열:", sorted_arr)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]


# arr = [11, 45, 23, 81, 28, 34]
# arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
# arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]


# 피벗: 제일 왼쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
def hoare_partition1(left, right):
    pivot = arr[left]  # 피벗을 제일 왼쪽 요소로 설정
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j


# 피벗: 제일 오른쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
def hoare_partition2(left, right):
    pivot = arr[right]  # 피벗을 제일 오른쪽 요소로 설정
    i = left
    j = right - 1

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[right] = arr[right], arr[i]
    return i


# 피벗: 중간 요소로 설정
# 일반적으로 더 균형 잡힌 분할이 가능하며, 퀵 정렬의 성능을 최적화할 수 있습니다.
def hoare_partition3(left, right):
    mid = (left + right) // 2
    pivot = arr[mid]  # 피벗을 중간 요소로 설정
    arr[left], arr[mid] = arr[mid], arr[left]  # 중간 요소를 왼쪽으로 이동 (필요 시)
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j


def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition1(left, right)
        # pivot = hoare_partition2(left, right)
        # pivot = hoare_partition3(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)
#
#
#
#
#
#
#
#
#
#
# # def merge_sort(m):
# #     # 리스트의 길이가 1이면 이미 정렬된 상태이므로 그대로 반환
# #     if len(m) == 1:
# #         return m
# #
# #     # 리스트를 절반으로 나누기 위해 중간 인덱스를 계산
# #     mid = len(m) // 2
# #     left = m[:mid]  # 리스트의 앞쪽 절반
# #     right = m[mid:]  # 리스트의 뒤쪽 절반
# #
# #     # 재귀적으로 왼쪽 부분과 오른쪽 부분을 정렬
# #     left = merge_sort(left)
# #     right = merge_sort(right)
# #
# #     # 두 개의 정렬된 리스트를 병합하여 반환
# #     return merge(left, right)
# #
# #
# # def merge(left, right):
# #     # 두 리스트를 병합할 결과 리스트를 초기화
# #     result = [0] * (len(left) + len(right))
# #     l = r = 0  # 왼쪽 리스트와 오른쪽 리스트의 인덱스
# #
# #     # 두 리스트를 순차적으로 비교하여 작은 값을 결과 리스트에 추가
# #     while l < len(left) and r < len(right):
# #         if left[l] < right[r]:
# #             result[l + r] = left[l]
# #             l += 1
# #         else:
# #             result[l + r] = right[r]
# #             r += 1
# #
# #     # 왼쪽 리스트에 남은 요소들을 결과 리스트에 추가
# #     while l < len(left):
# #         result[l + r] = left[l]
# #         l += 1
# #
# #     # 오른쪽 리스트에 남은 요소들을 결과 리스트에 추가
# #     while r < len(right):
# #         result[l + r] = right[r]
# #         r += 1
# #
# #     # 병합된 결과 리스트를 반환
# #     return result
# #
# #
# # arr = [69, 10, 30, 2, 16, 8, 31, 22]
# # arr = merge_sort(arr)
# # print(arr)
