T = int(input())  # T의 개수를 입력

for _ in range(T):    # _ 는 T만큼 반복한다는 뜻
    A, B = map(int, input().split())  # A와 B를 입력
    print(A + B)  # A와 B의 합을 출력
