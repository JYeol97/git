#문자열을 만드는 방법은 "", '', """, '''으로 가능
# 작은따음표 안에 큰따음표로 감싼다면 문자열 안에 문자열 가능 반대도 가능
# 아니면 \으로 가능
# \n : 줄바꿈 , \t : 문자열 사이 탭 간격 , \\ : \를 그대로 표현 , \' : ' 를 그대로 표현 , \" : "를 그대로 표현

a = "Life is too short, You need Python" #str 은 string(문자열)임
b = "a"
c = "123"
print(type(a))

d = "abc\'defg"
print(type(d))

e = "life is \ngood" # 줄바꿈
print(e)
f = '''Life is   
good''' # 줄바꿈 """도 가능
print(f)
g = 'Life is \tgood' # 스페이스바 4번
print(g) 


# A와 B의 값을 다르게 하는 방법
A = 3
B = 5
print(A,B)

temp = A    # stored A.
A = B    # A <- B
B = temp    #  
print(A,B)


A = 3
B = 5
A, B = B, A
print(A, B)

import keyword
print(keyword.kwlist)