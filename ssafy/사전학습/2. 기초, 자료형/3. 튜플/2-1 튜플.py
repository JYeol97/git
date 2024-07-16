# 튜플은 변경이 안되는 리스트라고 생각하면 편함
# immutable (정수, 실수, 문자열, 튜플)
# 소괄호

t1 = ()
t2 = (1, ) # 뒤의 값이 비어도 무조건 , 해야함
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(type(t1))
print(t2[0])
print(type(t4))

# del t1[0] X 변경 불가능

print(t2[0])

t1 = (1, 2, 'a', 'b')
print(t1[1:]) # 슬라이싱은 된다 (선택해서 가져온다는 개념)
print(t1)

t1 = (1, 2, 3)
t2 = ('a', 'b', ('ab', 'cd'))
t3 = t1 + t2
t4 = t1 + t2 + t3
print(t4)

t5 = t3 * 3
print(t5)

print(len(t5))