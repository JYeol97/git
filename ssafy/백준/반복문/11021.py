# # f문자열 포매팅
# name = '홍길동'
# age = 30
# a = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
# print(a)
# a = f'나의 이름은 {name}입니다. 나이는 {age + 1}입니다.'
# print(a)
# a = f'{"hi":<10}'
# print(a)

# T = int(input())
# c=0

# for x in range(1, T):
#     A,B = map(int, input().split())
#     result = A+B
# print(f'Case #{x}: {result}')

T = int(input())

for x in range(1, T+1):
    A, B = map(int, input().split())
    result = A+B
    print(f'Case #{x}: {result}')


