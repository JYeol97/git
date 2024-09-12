import sys
sys.stdin = open("sample_input (3).txt")

def mareummo(cx,cy, d):
    global mn
    global indices
    global stack
    if d > N+1:
        return
    if indices:
        # 운영비용
        d_total = d * d + (d-1)*(d-1)
        total = len(indices)*M - d_total
        # indices = []
        if len(indices) >= mn and total >= 0:
            mn = len(indices)

        # elif len(indices) <= mn or total < 0:
        #     return


    for i in range(-d, d + 1):
        for j in range(-d + abs(i), d - abs(i) + 1):
            x, y = cx + i, cy + j
            if 0 <= x < N and 0 <= y < N:  # 배열의 범위 내에 있는지 확인
                if arr[x][y] == 1:
                    indices.add((x, y))

    mareummo(cx,cy,d+1)

    return



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    mn = 0
    stack = 0
    for i in range(N):
        for j in range(N):
            indices = set()
            mareummo(i,j,0)
    print(f'#{tc} {mn}')