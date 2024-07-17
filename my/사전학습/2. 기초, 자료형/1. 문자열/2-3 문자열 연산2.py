# 문자열 포매팅 
# %d 정수, %s 문자열, %c 문자 1개, %f 부동소수, %o 8진수, %x 16진수, %%Literal % (문자 % 자체)
a = "I eat %d apples." % 4
print(a)

number = 4
b = "I eat %d apples." % number
print(b)

day = "three"
c = "I eat %d apples. so I was sick for %s days." % (number, day)
print(c)

# %s 문자
b = "I eat %s apples." % "five"
print(b)

# 포맷코드와 숫자 함께 사용
# 정렬과 공백 %?s 는 전체 길이가 ?만큼 되도록 문자를 조절(스페이스바)
f = "%10sjane." % 'hi'
print(f)

# 소수점 자리 표시
g = "%.3f" % 3.14152
print(g)

h = "I eat {0} apples" .format(5) # 5말고 "글자"도 가능
print(h)

i = "I eat {0} apples. so I sick for {1} days.". format(5, "three")
print(i)

# 정렬
# "{0:<10}".format("?") 총 10글자 이지만 ?를 왼쪽으로 보내겠다 나머진 공백
# "{0:>10}".format("?") 총 10글자 이지만 ?를 오른쪽으로 보내겠다 나머진 공백
# "{0:^10}".format("?") 총 10글자 이지만 ?를 가운데로 보내겠다 나머진 공백
# "{0:=<10}".format("?") 총 10글자 이지만 ?를 왼쪽으로 보내겠다 나머진 =으로 채움
j = "{0:<10}". format("hi")
print(j)

j = "{0:>10}". format("hi")
print(j)

j = "{0:^10}". format("hi")
print(j)

j = "{0:=<10}". format("hi")
print(j)

# f문자열 포매팅
name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(a)
a = f'나의 이름은 {name}입니다. 나이는 {age + 1}입니다.'
print(a)
a = f'{"hi":<10}'
print(a)



# "%.3f" % 3.14152

c = 3.141592
a = f'{c:0.3f}'
print(a)