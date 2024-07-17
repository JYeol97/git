# n = 2
# y = range(1,10)
# result = [n*y for n in 2 for y in range(1,10)]
# print(result)

# # result = [x*y for x in range(2,10) for y in range(1,10)]
# # print(result)

# n = int(input())
# while y < 10:
#     result = [n * y for y in range(1,10)]
# print(result)


n = int(input())
y = 1
while y <= 9:
    print("%d * %d = %d" % (n, y, n * y))
    y += 1     # y += 1 은 1씩증가
