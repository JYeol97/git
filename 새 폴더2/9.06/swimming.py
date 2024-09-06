import sys
sys.stdin = open("sample_input (14).txt")


##############################접근 방법 1 (dfs)##################################
def dfs(month, sum_cost):
    global ans
    # 기저조건
    if month > 12:
        ans = min(ans, sum_cost)
        return

    # 1일권으로 모두 구매 (다음 재귀에서 다음 달을 확인)
    dfs(month + 1, sum_cost + (days[month] * cost[0]))
    # 1달권 (다음 재귀에서 다음 달을 확인)
    dfs(month + 1, sum_cost + cost[1])
    # 3달권 (다음 재귀에서 다음 3달 후를 확인)
    dfs(month + 3, sum_cost + cost[2])
    # 1년권 (다음 재귀에서 다음 12달 후를 확인) -> 사실 재귀에서 빼도 됨
    dfs(month + 12, sum_cost + cost[3])

T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))

    ans = 99999999999999999999999999999999999999999999999999999

    dfs(1, 0)
    print(ans)

##############################접근 방법 2 (DP)##################################

# 3월 기준으로 생각: 2월 까지의 최소 금액 + 본인의 금액 중 최소 금액
# 이전의 최소 금액들을 활용해서 내 최소금액을 구할 수 있음
# DP 활용하기
# 작은문제로 분할 가능
#    -> 전체 문제의 합 = 각 달까지 최소 금액들이 쌓여서 완성
#    -> 각 달까지의 최소 금액 문제로 생각
#    -> 앞의 결과를 건드려선 안됨

# T = int(input())
# for tc in range(1, T+1):
#     cost = list(map(int, input().split()))
#     days = [0] + list(map(int, input().split()))
#     dp = [0] * 13 # 1~ 12월 최소 금액 저장
#     dp[1] = min(days[i] * cost[0] , cost[1])
#     dp[2] = min(dp[1] -)
#
#     for i in range(1, 13):
#         # 현재 달 최소 비용
#         # 1~2월 까지는 이전 달 + 1일 권 구입 /이전 달 + 1달 권
#         # 이전 달 + 1일 권 구입 /이전 달 + 1달 권/ 3달 전에 3달권 구입// 3개중 최소
#         dp[i] = min(dp[i-1] + (days[i] * cost[0]) , dp[i-1] + cost[1], dp[i-3] + cost[2])
#
#
#         # 인덱스 오류 피하기 위해
#         if i >= 3:
#             dp[i] = min(dp[i], dp[i - 3]+ cost[2])

























