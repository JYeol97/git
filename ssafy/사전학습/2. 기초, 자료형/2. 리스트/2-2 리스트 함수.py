# 리스트 추가
a = [1, 2, 3, 4 ,5]
a.append(6)
a.append(['quit', 5])
print(a)

# 리스트 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a','w','c']
a.sort()
print(a)

a= ['a','c','b']
a.sort() # 오름차순
a.reverse() # 내림차순
print(a)

a = [1, 2, 3]
print(a.index(3)) # 찾기

a = ['a','c','b']
print(a.index('a'))

a = [1, 2, 3]
a.insert(0,4) # 0번째 index에 4를 추가(삽입)한다
print(a)

a = [1, 2, 3, 4, 5]
a.remove(3) # 가장 처음에 있는 3을 제거한다
print(a)

a = [1, 2, 3]
a.pop() # ?번째를 날려버린다 (제거한다)
print(a)

print(a.pop()) # 날려버린걸 찾을 수 있음

a = [1 ,2 ,3, 1]
print(a.count(1)) # 1이 몇개인지

a = [1, 2, 3]
a = a+[4] # a+= [4] 와 같은 의미
print(a)

a = [1, 2, 3]
a.extend([4,5]) # 확장 append는 [] 자체로 추가 extend는 숫자만 추가
print(a)