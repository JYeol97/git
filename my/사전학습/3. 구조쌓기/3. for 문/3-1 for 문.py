# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할_문장1
#     수행할_문장2

test_list = ['one', 'two', 'three'] 
for i in test_list: 
     print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
     print(first + last)


# marks1.py 응용
marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)



# marks2.py
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)

# range 함수 긴 숫자를 간편하게
a = range(1, 101)
print(a)


add = 0 
for i in range(1, 11): 
     add = add + i 
print(add)



for i in range(2,10):        # 1번 for문
     for j in range(1, 10):   # 2번 for문
         print(i*j, end=" ")    # end 는 띄어쓰기용
     print('')        # 한줄 띄어준다


# 아래 는 모두 같음 (표현방법만)
a = [1,2,3,4]
result = []
for num in a:
     result.append(num*3)
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)


result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)
