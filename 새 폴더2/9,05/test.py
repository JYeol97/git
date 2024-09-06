import sys

sys.stdin = open("sample_input (9).txt")

def backtrack(a, bus, K):
    global cnt
    global mn

    # 종점에 도달했을 때
    if a + K >= len(bus) - 1:
        if mn > cnt:
            mn = cnt
        return

    # 현재 지점에서 선택할 수 있는 모든 범위 탐색
    for k in range(a+1, a+K+1):
        cnt += 1
        backtrack(k, bus, bus[k])  # 현재 선택한 위치에서 갈 수 있는 최대 거리로 갱신
        cnt -= 1  # 백트래킹: 원래 상태로 복원

T = int(input())
for tc in range(1, T + 1):
    bus = list(map(int, input().split()))
    K = bus[1]  # 첫 번째 정류장에서 갈 수 있는 거리
    a = 1
    cnt = 0
    mn = float('inf')  # 최솟값을 무한대로 초기화
    backtrack(a, bus, K)
    print(mn)