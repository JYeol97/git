import sys
sys.stdin = open("sample_input (10).txt")

# def check(a, i, visited, total):
#     global mx
#     if i == N:
#         if mx > total:
#             mx = total
#         return
#
#     if total > mx:
#         return
#
#     for k in range(a, N):
#         if visited[k] == 0:
#             visited[k] = 1
#             check(0, i+1, visited, total+arr[i][k])
#             visited[k] = 0
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     mx = 9000
#     visited = [0] * (N)
#     check(0, 0, visited, 0)
#     print(f'#{tc} {mx}')
def check(a, i, visited, total):
    global mx
    if i == N:
        if mx > total:
            mx = total
        return

    if total > mx:
        return

    for k in range(a, N):
        if visited[k] == 0:
            visited[k] = 1
            check(0, i+1, visited, total+arr[i][k])
            visited[k] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    mx = 9000
    visited = [0] * (N)
    check(0, 0, visited, 0)
    print(f'#{tc} {mx}')
