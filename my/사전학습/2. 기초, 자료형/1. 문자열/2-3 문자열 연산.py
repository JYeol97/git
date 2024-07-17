# 문자열 더하기 반복
head = "Python"
tail = " is fun!"
print(head + tail) # 문자열 더해서 연결

print(head * 3) # 문자열 3번 반복

# 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기
A = "Life is too short"
print(len(A)) # len(length)문자열 길이 구하기 

# 문자열 인덱싱(가리킨다)과 슬라이싱(잘라낸다)
# 인덱싱
a = "Life is too short, You need Python"
print(a[3]) #a열의 3번째는 
print(a[0])
print(a[12])
print(a[-1])

# 슬라이싱
B = "Life is too short, You need Python"
b = B[0] + B[1] + B[2] + B[3]
print(B)
c = b[0 : 4] # 만약 4자리가 비어있으면 끝까지
d = b[0 : 4 : 1] # [이상 : 미만 : 간격]
print(c)
print(d)

C = "19971110JAEYEOL"
D = C[: 4]
F = C[4 : 6]
G = C[6 : 8]
H = C[8 :]
print(D)
print(F)
print(G)
print(H)
