import sys
input = sys.stdin.readline

T = int(input())
c = 0
for _ in range(T):
    A,B = map(int, input().split())
    c = c + A + B
print(c)


import sys
input = sys.stdin.readline().strip()

T = int(input())
c = 0
for _ in range(T):
    A,B = map(int, input().split())
    c = c + A + B
print(c)