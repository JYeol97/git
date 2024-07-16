# Mutable (리스트, 딕셔너리, 집합)
# 리스트는 odd, list 사용, 대괄호
odd = [1, 3, 5, 7, 9]
print(type(odd))
list = [1, 3, 5, 7, 9]
print(type(list))

e = [1, 2, 'Life', 'is']
f = [1, 2, ['Life', 'is']]
print(e[0])
print(f[2])

print(e[1]+f[0])

print(f[2][1])

# 3중 리스트는 연습해보자

#슬라이스
a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[0::2])

a = [1, 2, 3, ['a','b', 'c'], 4, 5]
b = a[:3]
c = a[3]
d = a[4:]
f = a[3][1]
g = a[3][2]
h = a[3][0]
print(b)
print(c)
print(d)
print(f)
print(g)
print(h)

# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
c = 3
print(a+b)
print(a*c)

# 리스트 길이
a = [1, 2, 3]
print(len(a))
print(str(a))

#ex
a = [1, 2, 3]
print(str(2)+"hi")

# 교체
a = [1, 2, 3]
a[2] = 4
print(a)

# 삭제
a = [1, 2, 3]
del a[1]

print(a)

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
del a[2:3]
print(a)