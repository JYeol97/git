a = [1, 2, 3]
b = a
print(id(a)) # 주소값(id)이 같은지 비교하는것 
print(id(b))

a = [1, 2, 3]
b = a
a[1] = 4
print(a)
print(b)

a = [1, 2, 3]
b = a[:] # 슬라이싱(:)을 하면 아래 바꾸기 전 본래의 모습을 가지고 있기에 값이 다름
a[1] = 4
print(a)
print(b)

from copy import copy # 복사하는 기능을 가진 모듈 복사 후엔 독립적으로 바뀜
a = [1, 2, 3]
b = copy(a) # b=a.copy() 함수표현
print(a)
print(b)

a, b = ('python', 'life') # 한번에 쓰는것도 가능
print(a)
print(b)
(a, b) = ('python', 'life') # 튜플과도 같다
print(a)
print(b)
a, b = 'python', 'life'
print(a)
print(b)
[a, b] = ['python', 'life']
print(a)
print(b)

# a,b위치를 바꾸는 방법
a = 3
b = 5
a, b = b, a
print(a)
print(b)