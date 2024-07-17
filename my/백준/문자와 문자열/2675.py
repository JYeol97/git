# string = "abc"
# result = ""
# for char in string:
#     result += char * 3
# print(result)  # 출력: aaabbbccc
# 슬라이싱 해서 intx해서 곱해서 따로 출력

# 리스트 슬라이싱
# a = [1, 2, 3, 4, 5]
# del a[2:3]
# print(a)
# 테스트 케이스 개수 입력
# T = int(input())

# # 각 테스트 케이스에 대해 반복
# for _ in range(T):
#     # 입력 받기: x와 y
#     x, y = input().split()
    
#     # x를 정수로 변환
#     x = int(x)
    
#     # 결과 문자열 초기화
#     result = ""
    
#     # 문자열 y의 각 문자에 대해 반복
#     for char in y:
#         # 각 문자를 x번 반복하여 결과에 추가
#         result += char * x
    
#     # 결과 출력
#     print(result)

S = int(input())

for _ in range(S):
    x,y = input().split()

    x = int()

    result = ""

    for char in y:
        result += char * x
print(result)

2
3 ABC
5 /HTP





# result = ""
# for char in y:
#     result += char * x
# print(result)


