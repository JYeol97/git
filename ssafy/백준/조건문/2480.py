# A,B,C = map(int, input().split())

# if A == B == C:
#     result = int(10000 + A*1000)
# elif A != B and B == C:
#     result = int(1000 + B*100)
# elif B != C and A == C:
#     result = int(1000 + A*100)
# else:
#     A,B,C.sort()
#     result = int(A,B,C.sort([2]*100))

# print(result)

# A, B, C = map(int, input().split())

# if A == B == C:
#     result = 10000 + A * 1000
# elif A != B and B == C:
#     result = 1000 + B * 100
# elif B != C and A == C:
#     result = 1000 + A * 100
# else:
#     max = sorted([A, B, C])[2]    # sorted 는 새로운 리스트로 반환
#     result = max * 100

# print(result)


# A, B, C = map(int, input().split())

# if A == B == C:
#     result = 10000 + A * 1000
# elif A != B and B == C:
#     result = 1000 + B * 100
# elif B != C and A == C:
#     result = 1000 + A * 100
# else:
#     max_number = sorted([A, B, C])[2]
#     result = max_number * 100

# print(result)

# A, B, C = map(int, input().split())

# if A == B == C:
#     result = 10000 + A * 1000
# elif A != B and B == C:
#     result = 1000 + B * 100
# elif B != C and A == C:
#     result = 1000 + A * 100
# else:
#     max_number = max(A,B,C)
#     result = max_number * 100

# print(result)

# A, B, C = map(int, input().split())

# if A == B == C:
#     result = 10000 + A * 1000
# elif A == B or B == C or A == C:
#     if A == B == C:
#         result = 10000 + A * 1000
#     else:
#         if A == B:
#             result = 1000 + A * 100
#         elif B == C:
#             result = 1000 + B * 100
#         else:  # A == C
#             result = 1000 + A * 100
# else:
#     max_value = max(A, B, C)
#     result = max_value * 100

# print(result)

A, B, C = sorted(map(int, input().split()))

if A == B == C:
    result = 10000 + A * 1000
elif A == B or B == C:
    result = 1000 + B * 100
else:
    result = C * 100

print(result)

# 애초에 리스트를 만들 때 정렬도 같이해서 새로운 리스트 만듬