# T = int(input())

# C=0

# for x in range(1, T+1):
#     A, B = map(int, input().split())
#     C = A+B
#     print(f'Case #{x}: {A + B} = {C}')


# T = int(input())

# for x in range(1, T+1):
#     A, B = map(int, input().split())
# #     C = A+B
# #     print(f'Case #{x}: {A + B} = {C}')

# T = int(input())
# C=0
# for x in range(1, T+1):
#     A, B = map(int, input().split())
#     C = C+ A+B
#     print(f'Case #{x}: {A} + {B} = {C}')

T = int(input())
for x in range(1, T+1):
    A, B = map(int, input().split())
    result = result+ A+B
    print(f'Case #{x}: {A} + {B} = {result}')