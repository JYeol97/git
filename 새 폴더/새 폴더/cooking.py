import sys
sys.stdin = open("sample_input (6).txt")

def dfs(i,j,visited, root,result_A):
    global result_B
    global total
    if total >= abs(result_A - result_B):
        total = abs(result_A - result_B)

    for l in range(0, N-1):
        for k in range(0, N-1):
            if visited[k] == 0 and visited[l] == 0:
                visited[k] = 1
                visited[l] = 1
                result_B += arr[i][k] + arr[k][i]
                dfs(i, j, visited, root + 1, result_A)
                result_B = 0
                visited[k] = 0
                visited[l] = 0



T = int(input())
for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result_B = 0
    stack = []
    total = 1000000000000000000000000000
    for i in range(0, N-1):
        for j in range(i+1, N):
            visited[i] = 1
            visited[j] = 1
            result_A = arr[i][j] + arr[j][i]
            dfs(i,j,visited, 0,result_A)
            visited[i] = 0
            visited[j] = 0
    print(total)