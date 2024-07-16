# 집합(set)은 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형.

s1 = set([1, 2, 3])
print(s1)

s1 = {1, 2, 3}
print(s1)

s1 = set("hello") # 집합의 특성으로 순서가 딱히 없음 또한 중복된것도 하나로 취급 (집합의 특징)
print(s1)

s1 = set([1, 2, 3])
l1 = list(s1)
print(l1[0])
l1 = tuple(s1)
print(l1[0])

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1&s2) # 교집합 <&말고 intersection라는 함수로 사용가능>

print(s1-s2) # 차집합 <-말고 diffrence라는 함수로 사용가능>

print(s1|s2) # 합집합 shift + 백슬래쉬 <|말고 union라는 함수로 사용가능>

s1 = set([1, 2, 3])
s1.add(4) # 집합에 원소 추가
print(s1)

s1 = set([1, 2, 3])
s1.update([3, 4, 5, 6]) # 집합에 여러 원소 추가
print(s1)

s1 = set([1, 2, 3])
s1.remove(2) # 원소 제거라고 생각
print(s1)

# 응용
l1 = [1,2,2,3,3,3,3,4]
s1 = set(l1)
print(s1)

s1 = list(set(l1))
print(s1)