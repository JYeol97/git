import sys

sys.stdin = open("sample_input.txt")


def finds(matrix):
    global result
    for i in range(N):
        for j in range(len(matrix[i])):
            if N == 1 and matrix[i][j] == '#':
                print(f'#{tc} yes')
                return
            lst = []
            if matrix[i][j] == '#' and visited[i][j] != 1:
                for k in range(0, len(matrix[i]) - j):
                    b = j + k
                    if matrix[i][b] == '#' and visited[i][b] != 1:
                        visited[i][b] = 1
                        lst.append([i, b])

                    elif matrix[i][b] != '#':
                        break
                result = deltasearch(lst, matrix)

    else:
        return print(f'#{tc} {result}')


def deltasearch(lst, matrix):
    global visited
    dx = 1
    x = len(lst)
    for r in range(len(lst)):
        for t in range(0, N):
            nx = lst[r][0] + t
            if nx < N and matrix[nx][lst[r][1]] == '#' and visited[nx][lst[r][1]] != 1:
                visited[nx][lst[r][1]] = 1
                lst.append([nx, t])

    if len(lst) == x ** 2:
        return 'yes'

    return 'no'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = 'no'
    matrix = [list(map(str, input())) for _ in range(N)]
    visited = [[0] * len(matrix[0]) for _ in range(N)]
    finds(matrix)
