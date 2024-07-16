# a = [1, 2, 3]
# print(a.index(3)) # 찾기
import sys
input = sys.stdin.read   # 한번에 받아와서 문자열로 정리
A = list(map(int, input().split()))

max_numbers = max(A)
max_index = A.index(max_numbers) + 1
print(max_numbers)
print(max_index)