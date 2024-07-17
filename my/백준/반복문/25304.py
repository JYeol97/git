# X = int(input())
# N = int(input())
# a,b = map(int, input().split())

# if X == sum(a*b):
#     print(Yes)
# else:
#     print(No)



# X = int(input())
# N = int(input())

# for _ in range(N):
#     a,b = map(int, input().split())
#     a = a+b
# if X == a:
#     print("Yes")
# else:
#     print("No")


# X = int(input())
# N = int(input())

# for _ in range(N):
#     a,b = map(int, input().split())
#     c = c + a*b
# if X == c:
#     print("Yes")
# else:
#     print("No")

# 변수 c를 반드시 초기화 시켜야함
X = int(input())
N = int(input())
c = 0
for _ in range(N):
    a,b = map(int, input().split())
    c = c + a*b
if X == c:
    print("Yes")
else:
    print("No")