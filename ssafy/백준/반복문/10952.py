while True: # _ 는 T만큼 반복한다는 뜻
    A, B = map(int, input().split())  # A와 B를 입력
    if A == 0 and B == 0: # A와 B의 합을 출력
         break 
    else:
         print(A+B)