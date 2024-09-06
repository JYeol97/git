# import sys
#
# sys.stdin = open("sample_input (9).txt")


def backtrack(a, K):
    global cnt
    global mn
    K -= 1
    if mn <= cnt:
        return

    if a == N - 1:
        if mn > cnt:
            mn = cnt
        return
    # 카운트 증가 시키는 부분이 내가 만약 배터리가 없을때
    cnt += 1
    # 이 부분이 K 값이 아니라 시작점이 다음으로 넘어거야 해서 bus[K] -> bus[a + 1] 로 바꿔줌
    backtrack(a + 1, bus[a + 1])
    cnt -= 1
    if K:
        backtrack(a + 1, K)


T = int(input())
for tc in range(1, T + 1):
    bus = list(map(int, input().split()))
    N = bus[0]
    K = bus[1]
    a = 1
    cnt = 0
    mn = 123123
    backtrack(a, K)
    print(f'#{tc} {mn}')