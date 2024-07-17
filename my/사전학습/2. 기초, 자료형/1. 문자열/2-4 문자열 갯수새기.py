a = "hobby"
print(a.find('b')) # 만약 없으면 -1로 출력

print(a.index('b')) # 만약 없으면 오류

# 문자열 삽입
a = ", ".join('abcd')
print(a)

a = ", ".join(['a', 'b', 'c', 'd'])
print(a)

#  소문자 대문자 바꾸기
a = "Hi"
print(a.upper())
print(a.lower())

# 공백지우기
a = " hi "
print(a.lstrip()) # 왼쪽
print(a.rstrip()) # 오른쪽
print(a.strip()) # 양쪽

# 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg")) # Life 를 Your leg로

# 문자열 나누기
a = "Life is too short"
print(a.split()) # 띄워쓰기를 기준으로 나눔
a = "a:b:c:d"
print(a.split(":")) # : 를 기준으로 나눔

# 문자 개수 세기
a = "Life is too short"
print(a.count('o'))

# 문자 위치 알려주기
a = "Life is too short"
print(a.find('e'))