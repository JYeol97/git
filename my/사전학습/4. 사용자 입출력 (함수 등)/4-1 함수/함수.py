def add(a, b):       # a, b는 매개변수
    return a + b  # 여기까진 함수를 정의한 것 add는 아무거나 상관 ㄴ 

add(4, 5)
print(add(4,5))        # 3, 4 는 인수

def say():
    return 'Hi'
a = say()
print(a)

def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b)) # 만약 return a + b가 있다면 리턴이 가능
a = add(1,2)
print(a)

def say():
    print('Hi')

a = say()
print(a)


def sub(a,b):
    return a - b
result = sub(b=3, a=7)
print(result)


def add_many(*args):
    result = 0
    for i in args:
        result = result + i      # *args에 입력받은 모든 값을 더한다 * 표시가 가장 중요
    return result
add_many(1,2,3,4,5)
print(add_many(1,2,3,4,5))


def add_mul(choice, *args):
    if choice == 'add':         # 매개변수 choice에 'add'를 입력받았을 때
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':          # 매개변수 choice에 'mul'을 입력받았을 때
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4)
print(result)


def print_kwargs(**kwargs):            # 키워드를 뽑아낸다 키워드 아규먼트 **는 딕셔너리 형태로 뽑아냄
    print(kwargs)
print_kwargs(a=1,b=2)                     



def add_and_mul(a,b):
    return a+b, a*b
   #return a+b 는 안됨
   #return a*b 는 안됨
print(add_and_mul(3,4))               # 튜플로 나옴



def say_nick(nick):
    if nick == "바보":
        return            # 함수를 빠져나감
    print("나의 별명은 %s 입니다." % nick)

say_nick("나")
say_nick("바보")           # 바보는 출력이 안됨 닉이 바보이기 때문에 return을 만나서 함수가 종료됨



def say_myself(name, old, man=True):          # 만약 man=True와 old의 위치를 바꾼다면 매개변수의 순서가 달라지기 때문에 오류가 나옴 그러나 아래에서 old= 처럼 해논다면 오류없음 (지정된건 맨뒤로)
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("임재열", 28, True)           # True는 생략가능 왜냐 함수를 정의할 때 기본값이 True이기 때문에



a = 1       # 전역 변수 (전체를 담당)
def vartest(a):
    a = a+1          # 여기서 정의한 a는 지역변수 (함수 안에서만, 함수가 끝난다면 사라짐)

vartest(a)
print(a)        # 따라서 a를 출력하면 1이 나오는 것



# def vartest(a):         # a라는 전역변수가 없기 때문에 함수가 사라지면서 a라는 값이 정의되지 않게됨
#     a = a + 1

# vertest(3)
# print(a)



a = 1
def vartest(a):
    a = a + 1
    return a      # return사용하면 전역변수를 변경가능

a = vartest(a)
print(a)



a = 1
def vartest():
    global a             # global이란 전역변수의 예약으로 쓰인다. 전역변수를 가져온다라는 뜻 
    a = a+1              # 여기서 a가 전역변수를 가져와서 활용을 했기 때문에 a가 바뀌었다 (전역변수와 지역변수가 바뀜)

vartest()
print(a)



b = [1, 2, 3]
def vartest2(b):
    b = b.append(4)
vartest2(b)
print(b)            # 여기는 vartest2(b) 이거 자체가 리스트 자체를 넘긴것이기 때문에 지역변수 전역변수가 의미없어짐



a = [1,2,3,4]

result = a.pop()     # result = a.append()는 result값이 없음 왜냐 a 자체에 추가하는 행위이기 때문에. a.pop()은 a에서 하나를 빼서 result에 넣기 때문에 값이 있음

print(result)
print(a)



def add(a,b):
    return a + b

add = lambda a, b: a+b     # 위와 같지만 멋있게 쓸 수 있음 lambda는 그런 용도
result = add(3,4)
print(result)

a = [lambda a, b : a+b, lambda a, b : a*b]
print(a[0](3,4))          # 얘도 위와 같음



