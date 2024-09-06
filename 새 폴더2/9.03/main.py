def subset(arr, N, i):
    # 기저조건(종료) : 모든 요소의 포함 유무를 결정
    # => i 가 N이 되었을 때
    if i == N:
        # 값의 포함유무에 따라서 출력...!
        for k in range(0, N):
            if bits[k] == 1:  # 포함이 된 요소라면
                print(arr[k], end=', ')
        print()
        return

    # 유도조건
    for j in range(0, 2):  # j: 0 or 1
        bits[i] = j  # 결정
        subset(arr, N, i + 1)


arr = [1, 2, 3, 4]
N = len(arr)

# 해당 인덱스의 요소를 포함할지 유무(1, 0)
bits = [0] * N
subset(arr, N, 0)
print(bits)
