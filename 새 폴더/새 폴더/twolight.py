import sys
sys.stdin = open("sample_input.txt")

T = int(input())
arr = []
for tc in range(1,T+1):
    A,B,C,D = map(int, input().split())

    first = max(C,A)

    last = min(D,B)

    total = last - first
    if total <= 0:
        total = 0

    arr.append(total)

for k in range(len(arr)):
    print(f'#{k+1} {arr[k]}')