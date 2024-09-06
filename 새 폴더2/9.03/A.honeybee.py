'''
4 2 13  N: 벌통 갯수  M: 채집할 수 있는 최대 갯수 C: 채집할 수 있는 최대 양
6 1 9 7
9 8 5 8
3 4 5 3
8 2 6 7
'''
import sys
sys.stdin = open("sample_input (3).txt")

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int,input().split())

    bee_house = [list(map(int, input().split())) for _ in range(N)]

    # 내가 m개씩 캘건데 절대 그 양이 C보다 높지 않은 최댓값을 구해야함. 따라서
    # 반복문을 돌며 두개씩 확인했을때 제일 많지만 c보다 작은 애들 두개를 구해야함
    total = 0
    lst = []
    total_lst = []
    for i in range(N):
        for j in range(N-M+1):
            if bee_house[i][j] + bee_house[i][j+1] <= C:
                if len(lst)<M:
                    lst.append([[i,j], [i,j+1]])
                    total_lst.append(bee_house[i][j]**2+ bee_house[i][j+1]**2)


                elif lst[-1][1] != [i, j]:
                    lst.append([[i,j], [i,j+1]])
                    total_lst.append(bee_house[i][j]**2+ bee_house[i][j+1]**2)
    total_lst.sort()
    final_lst = []
    for k in range(len(total_lst)-1, -1, -1):
        if len(final_lst) != M:
            final_lst.append(total_lst[k])

    print(sum(final_lst))


    # for k in range(len(lst)):
    #     a = bee_house[lst[k][0][0]][lst[k][0][1]]
    #     b = bee_house[lst[k][1][0]][lst[k][1][1]]
    #     if a+b <= C:
    #         if total < a**2+b**2:
    #             total = a+b
    #
    # print(total)


    # mx = 0
    # for k in range(len(lst)):
    #     for l in range(2):
    #         if mx < lst[k] <= C:
    #             mx = lst[k]
    #
    # print(mx)
    #
















