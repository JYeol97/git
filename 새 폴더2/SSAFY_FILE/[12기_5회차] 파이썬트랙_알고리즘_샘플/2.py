import sys
sys.stdin = open("algo2_sample_in.txt")
def tree(root):
    if int(parent[root]) == N:
        return


    tree(left[root])
    lst.append(left[root])
    tree(right[root])
    lst.append(right[root])




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input()))
    # print(ord(arr[0]))
    stack = []
    lst = []
    for i in range(N):
        a = ord(arr[i])
        while True:
            stack.append(a % 2)
            a //= 2
            if a == 1:
                stack.append(a)
                break

    # print(stack)  # [1, 0, 0, 0, 0, 0, 1]
    M = len(stack)

    parent = [0]*(M+1)
    left = [0]*(M+1)
    right = [0]*(M+1)

    for j in range(M-1,-1,-1):
        if j % 2 == 0:
            right[j+1] = str(stack[j])
            parent[j+1] = str(stack[j-M])

        else:
            left[j+1] = str(stack[j])
            parent[j+1] = str(stack[j - M])

    print(parent)
    tree(M)
    print(lst)