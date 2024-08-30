import sys
sys.stdin = open("sample_input (8).txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N == 0:
        print(f'#{tc} -1')
        break

    for i in range(1, N+1):
        if i ** 3 > N:
            print(f'#{tc} -1')
            break
        if i**3 == N:
            print(f'#{tc} {i}')
            break
    else:
        print(f'#{tc} -1')


