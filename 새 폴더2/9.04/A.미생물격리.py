import sys

sys.stdin = open("sample_input(8).txt")

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    dct = {}

    dx = [-1, 1, 0, 0]  # 상 하 좌 우  [1 2 3 4]
    dy = [0, 0, -1, 1]
    q = []
    for u in range(K):
        i, j, nums, delta = map(int, input().split())
        q.append([i, j, nums, delta])
        dct[i, j] = [nums, delta]
    print(dct)

    time = 0
    while time != M:
        time += 1
        q_set = []
        cnt = 0
        for _ in range(len(q)):
            cnt += 1
            pops_q = q.pop(0)
            nx = pops_q[0] + dx[pops_q[3]]
            ny = pops_q[1] + dy[pops_q[3]]
            if 0 <= nx < N and 0 <= ny < N:
                if [nx, ny] not in q_set:
                    q_set.append([nx, ny])

                elif [nx, ny] in q_set:
                    for l in range(len(q_set)):
                        if [nx, ny] == q_set[l]:
                            q_set.pop(l)




