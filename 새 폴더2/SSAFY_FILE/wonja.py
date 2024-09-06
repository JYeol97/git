import sys

sys.stdin = open("sample_input (2).txt")

dx = [0, 0, -0.5, 0.5]
dy = [0.5, -0.5, 0, 0]


def add_to_dict(key, value):
    if key in dct:
        dct[key].append(value)11111111111111111111111111
    else:
        dct[key] = [value]


T = int(input())

for test in range(1, T + 1):
    N = int(input())
    lst = []
    energy = 0

    for _ in range(N):
        x, y, d, e = list(map(int, input().split()))
        lst.append([x, y, d, e])
    cnt = 4002
    check = set()

    while cnt != 0:

        for i in range(4):
            lst[i][0] = lst[i][0] + dx[lst[i][2]]
            lst[i][1] = lst[i][1] + dy[lst[i][2]]

        dct = {}
        for i in range(len(lst)):
            add_to_dict((lst[i][0], lst[i][1]), lst[i])



        # for key in dct.keys():
        #     a = dct[key]
        #     if len(a) >= 2:
        #         for j in range(len(a)):
        #             energy += a[j][3]


    # print(f'#{test} {energy}')
