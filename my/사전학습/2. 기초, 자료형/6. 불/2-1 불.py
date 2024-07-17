# 참과 거짓을 판단
a = 3 == 3
if a == 3: print(a)
print(type(a))
print(a)

# 자료형의 참과 거짓
# "python" 참, "" 거짓
# [1, 2, 3] 참, [] 거짓
# (1,2 , 3) 참, () 거짓
# {'a': 1} 참, {} 거짓
# 1 참, 0 거짓
# None 거짓

# while은 반복문
a = [1, 2, 3, 4]
while a:
    print(a)
    a.pop()

# 리스트에 들어있으면 참 없으면 거짓 을 표함
if []:
    print("참")
else:
     print("거짓")

a = bool([1,2,3]) # bool을 붙여도 됨 안에 든게 없으면 false
print(a)