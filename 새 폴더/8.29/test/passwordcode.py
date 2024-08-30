import sys

sys.stdin = open("input (6).txt")


def zero(i, j):
    if zero(i, j) == 0:
        return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 세로   M : 가로
    matrix = [list(map(int, input())) for _ in range(N)]
    dct = {
        '0': [0, 0, 0, 1, 1, 0, 1],
        '1': [0, 0, 1, 1, 0, 0, 1],
        '2': [0, 0, 1, 0, 0, 1, 1],
        '3': [0, 1, 1, 1, 1, 0, 1],
        '4': [0, 1, 0, 0, 0, 1, 1],
        '5': [0, 1, 1, 0, 0, 0, 1],
        '6': [0, 1, 0, 1, 1, 1, 1],
        '7': [0, 1, 1, 1, 0, 1, 1],
        '8': [0, 1, 1, 0, 1, 1, 1],
        '9': [0, 0, 0, 1, 0, 1, 1]
    }


    def findone(i,j):
        for a in range(N-1, -1, -1):
            for b in range(M-1, -1, -1):
                if matrix[a][b] == 1:
                    return a, b


    '''
    dct = {
        '0' : [3,2,1,1],
        '1' : [2,2,2,1],
        '2' : [2,1,2,2],
        '3' : [1,4,1,1],
        '4' : [1,1,3,2],
        '5' : [1,2,3,1],
        '6' : [1,1,1,4],
        '7' : [1,3,1,2],
        '8' : [1,2,1,3],
        '9' : [3,1,1,2]
    }
    '''
    ohmygod = []
    sumshole = 0
    sumsjjak = 0

    i, j = findone(0,0)

    stack = []
    while 0< j < M:
        if len(stack) != 7:
            stack.append(matrix[i][j])
            j -= 1

        elif len(stack) == 7:
            stack.reverse()
            for key, value in dct.items():
                if value == stack:
                    ohmygod.append(key)
                    break
            stack = []
    ohmygod.reverse()
    # print(ohmygod)
    for k in range(len(ohmygod)):
        if k % 2 == 0:
            sumshole += int(ohmygod[k])

        elif k % 2 != 0:
            sumsjjak += int(ohmygod[k])

    p = (sumshole * 3) + sumsjjak

    if p % 10 == 0:
        print(f'#{tc} {sumshole + sumsjjak}')

    elif p % 10 != 0:
        print(f'#{tc} 0')