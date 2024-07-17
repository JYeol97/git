# import sys
# input = sys.stdin.read

# X = 42
# H = list(map(int, input().split()))
# J = set(H)

# for number in H:
#     remain = number % X
#     A = set(remain)
#     is_duplicate = False
#     for element in H:
#         if list(H).count(element) > 1:
#             is_duplicate = True
#             break


import sys
input = sys.stdin.read

numbers = list(map(int, input().split()))

remainders = set(num % 42 for num in numbers)  # 중복 제거

print(len(remainders))   # 집합의 길이로 출력