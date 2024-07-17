# A,B=list(map(int(input().split())))
# result1 = (A[0]*B[0])
# result2 = (A[1]*10*B[0])
# result3 = (A[2]*100*B[0])
# result4 = (A[0]*B[1]*10)
# result5 = (A[1]*10*B[1]*10)
# result6 = (A[2]*100*B[1]*10)
# result7 = (A[0]*B[2]*100)
# result8 = (A[1]*10*B[2]*100)
# result9 = (A[2]*100*B[2]*100)

# print(result1+result2+result3+result4+result5+result6+result7+result8+result9 )

# # A,B=list(map(int(input().split())))
# # result1 = (A[0]*B[0])
# # result2 = (A[1]*10*B[0])
# # result3 = (A[2]*100*B[0])
# # result4 = (A[0]*B[1]*10)
# # result5 = (A[1]*10*B[1]*10)
# # result6 = (A[2]*100*B[1]*10)
# # result7 = (A[0]*B[2]*100)
# # result8 = (A[1]*10*B[2]*100)
# # result9 = (A[2]*100*B[2]*100)

# # c = (result1+result2+result3+result4+result5+result6+result7+result8+result9)
# # print(c)


# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# result1 = A[0] * B[0]
# result2 = A[1] * 10 * B[0]
# result3 = A[2] * 100 * B[0]
# result4 = A[0] * B[1] * 10
# result5 = A[1] * 10 * B[1] * 10
# result6 = A[2] * 100 * B[1] * 10
# result7 = A[0] * B[2] * 100
# result8 = A[1] * 10 * B[2] * 100
# result9 = A[2] * 100 * B[2] * 100
# total_result = (
#     result1 + result2 + result3 +
#     result4 + result5 + result6 +
#     result7 + result8 + result9
# )

# print(total_result)


# A = int(input())  
# B = int(input())  

# result1 = (A % 10) * (B % 10)
# result2 = (A % 100 // 10) * (B % 10) * 10
# result3 = (A // 100) * (B % 10) * 100
# result4 = (A % 10) * (B % 100 // 10) * 10
# result5 = (A % 100 // 10) * (B % 100 // 10) * 100
# result6 = (A // 100) * (B % 100 // 10) * 1000
# result7 = (A % 10) * (B // 100) * 100
# result8 = (A % 100 // 10) * (B // 100) * 1000
# result9 = (A // 100) * (B // 100) * 10000

# total_result = result1 + result2 + result3 + result4 + result5 + result6 + result7 + result8 + result9
# print(total_result)

A = int(input().strip())
B = int(input().strip())

result1 = A * (B % 10) 
result2 = A * (B // 10 % 10)
result3 = A * (B // 100) 
result4 = A * B  

print(result1)
print(result2)
print(result3)
print(result4)