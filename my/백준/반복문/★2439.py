# "{0:<10}".format("?") 총 10글자 이지만 ?를 왼쪽으로 보내겠다 나머진 공백
# "{0:>10}".format("?") 총 10글자 이지만 ?를 오른쪽으로 보내겠다 나머진 공백
# "{0:^10}".format("?") 총 10글자 이지만 ?를 가운데로 보내겠다 나머진 공백
# "{0:=<10}".format("?") 총 10글자 이지만 ?를 왼쪽으로 보내겠다 나머진 =으로 채움

T = int(input())

for x in range(1, T + 1):
    star = "{0:>T}".format("*" * x)
    print(star)


# T = int(input())

# for x in range(1, T+1):
#     star = "{0:>5}". format("*"*x)
#     print(star)