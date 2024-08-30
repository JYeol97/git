'''
상 - 0
하 - 1
좌 - 2
우 - 3

X  , Y , 방향, 에너지
'''

def quantum(X,Y,energy):









T = int(input())

for tc in range(1, T + 1):
    # 원자의 개수
    N = int(input())
    for _ in range(N):
        # X  , Y , 방향, 에너지
        X, Y, direction, energy = map(int, input().split())



