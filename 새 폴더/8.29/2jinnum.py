import sys
sys.stdin = open("sample_input (9).txt")
'''
3
4 47FE
5 79E12
8 41DA16CD
'''
dict_oper = {'A': 10 , 'B': 11, 'C': 12, 'D' : 13,'E' : 14 ,'F' : 15}

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(str, input().split()))
    N = int(N)
    a=list(M)
    total = 0
    arr = []
    h = ''
    for i in range(N):
        if a[i].isnumeric():
            b = int(a[i])
            k = N-i-1
            total += int(a[i])*(16**k)

        else:
            k = N - i - 1
            total += dict_oper[a[i]]*(16**k)
    while total != 0:
        # if total == 1:
        #     arr.append(str(total-1))
        arr.append(total % 2)
        total = total // 2
        if total == 0 and N != 1:
            arr.append(total)
            break
    arr.reverse()
    for i in arr:
        h += str(i)
    if len(h) < 4:
        while len(h) != 4:
            h = '0'+h

    print(f'#{tc} {h}')
    # print(f'#{tc}', *twojinsu(total))


