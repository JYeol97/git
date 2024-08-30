

a = [list(map(int, input().split())) for _ in range(N)]

#아래와 같음

for _ in range(N):
    a.append(list(map(int, input().split())))



# '''
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# '''
# # left, right 를 쓰는 버전
# # 단 입력이 반드시 각 노드당 최대 2번 씩만 들어온다고 가정한 코드
#
# # 후위 순회 ( 나-> 왼쪽 -> 오른쪽 )
# def preorder(node):
#     if node == 0:
#         return
#
#     preorder(left[node])   # 왼쪽 재귀호출
#     preorder(right[node])   # 오른쪽 재귀호출
#     print(node, end =' ')
#
#
# N = int(input())        # 1번부터 N번까지인 정점
# E = N-1
# arr = list(map(int, input().split()))
# left = [0]*(N+1)        # 왼쪽 자식 번호를 저장할 리스트
# right = [0]*(N+1)       # 오른쪽 자식 번호를 저장할 리스트
# # ex) left[3] = 2 -> 3번 부모의 왼쪽 자식은 2다.
# for i in range(0, len(arr), 2):
#     parent, child = arr[i], arr[i+1]
#     if left[parent]==0:          # 왼쪽 자식이 없으면
#         left[parent] = child
#     else:                       # 오른쪽 자식이 없으면
#         right[parent] = child
#
# root = 1        # 시작점을 1이라 가정 (그래프에서 가장 윗쪽이 1이라고 가정)
# preorder(root)