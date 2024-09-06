import sys
sys.stdin = open("sample_input (5).txt")


'''
N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N : 컨테이너 수  M : 트럭 수

    truck = list(map(int,input().split()))  # 화물의 무게  1 5 3
    ton = list(map(int, input().split()))  # 트럭 적재용량  8 3

    ton.sort()

    while True:
        ton -= truck
