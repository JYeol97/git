import sys

sys.stdin = open("sample_input (1).txt")
from collections import deque

def bfs(q,time,visited):
    while q:
        time += 1
        q = deque(list(set(q)))
        for _ in range(len(q)):
            next_N = q.popleft()

            if 0 <= next_N - 1 <= 1000000 and visited[next_N - 1] == 0:
                if next_N - 1 == M:
                    return time

                q.append(next_N - 1)
                visited[next_N - 1] = 1

            if 0 <= next_N + 1 <= 1000000 and visited[next_N + 1] == 0:
                if next_N + 1 == M:
                    return time
                q.append(next_N + 1)
                visited[next_N + 1] = 1

            if 0 <= next_N * 2 <= 1000000 and visited[next_N * 2] == 0:
                if next_N * 2 == M:
                    return time
                q.append(next_N * 2)
                visited[next_N * 2] = 1

            if 0 <= next_N - 10 <= 1000000 and visited[next_N - 10] == 0:
                if next_N - 10 == M:
                    return time
                q.append(next_N - 10)
                visited[next_N - 10] = 1




T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    q = deque([N])
    time = 0
    visited[N] = 1
    a = bfs(q, time, visited)

    print(f'#{tc} {a}')
