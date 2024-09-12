import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    q = []
    A = []
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        A.append([x*2, y*2, d, k])
        q.append([x*2, y*2, d, k])


    energy = 0
    dx = [1, -1, 0, 0] # 상하
    dy = [0, 0, -1, 1] # 좌우
    time = 0
    remove_set = []
    # for _ in range(4002):
    #     time = 0
    while q:
        if time == 4000:
            break
        time += 1
        position = {}
        for _ in range(len(q)):
            now = q.pop(0)
            nx = now[0] + dy[now[2]]
            ny = now[1] + dx[now[2]]
            if -2000<= nx<= 2000 and -2000 <= ny<= 2000:
                if (nx, ny) not in position.keys():
                    position[nx, ny] = [now]

                else:
                    position[nx,ny].append(now)

            else:
                continue

        for key, value in position.items():
            if len(value) > 1:
                for l in range(len(value)):
                    remove_set.append(value[l])

            elif len(value) == 1:
                q.append([key[0], key[1], value[0][2], value[0][3]])

    for j in range(len(remove_set)):
        energy += remove_set[j][3]

    print(f'#{tc} {energy}')




