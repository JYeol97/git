# N=10 X=5
# A= 1 10 4 9 2 3 8 5 7 6
# f문자열 포매팅
# name = '홍길동'
# age = 30
# a = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
# print(a)
# a = f'나의 이름은 {name}입니다. 나이는 {age + 1}입니다.'
# print(a)
# a = f'{"hi":<10}'
# print(a)


# N = int(input())
# X = int(input())
# A = list(map(int, input().split()))

# result = [b for b in A if b < X]
# print(f' '+result)
 # str : 문자열로 바꿈
N,X = map(int, input().split())
A = list(map(int, input().split()))
result = [str(b) for b in A if b < X]
print(" ".join(result))
