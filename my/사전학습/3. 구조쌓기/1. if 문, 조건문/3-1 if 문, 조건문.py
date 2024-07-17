# if 조건문 : 
#       수행할_문장1
#       수행할_문장2
#          ... 
# else : 
#       수행할_문장A
#       수행할_문장B
#          ...
# 들여쓰기는 탭을 누르면됨or스페이스4번

money = True # false
if money:
     print("택시를 타고 가라")
else:
     print("걸어 가라")

# 비교 연산자
# x<y
# x>y
# x==y 같다
# x!=y x와 y가 같지않다
# x>=y x가 y보다 크거나 같다
# x<=y x가 y보다 작거나 같다


money = 2000
if money >= 3000:
     print("택시를 타고 가라")
else:
     print("걸어가라")

# 3000원 이상 or 카드 있으면 택시
money = 2000
card = True
if money >= 3000 or card:
     print("택시를 타고 가라")
else:
     print("걸어가라")


print(1 in [1, 2, 3]) # in , not in 은 들어있냐고 물어보는것
print(1 not in [1, 2, 3])

#ex
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
     print("택시를 타고 가라")
else:
     print("걸어가라")


pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
     pass                               # pass를 사용하면 아무것도 하지 않음
else:
    print("카드를 꺼내라")


# 아래는 두 개는 줄여쓸 수 있다
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
     print("택시를 타고가라")
else:
     if card:
         print("택시를 타고가라")
     else:
         print("걸어가라")


pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
      print("택시를 타고가라")
elif card: 
      print("택시를 타고가라")
else:
      print("걸어가라")

# if, elif, else는 제한없이 무제한 사용 가능

# 줄여쓰기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 조건부 표현식
score = 80
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)


# 문자열 자료형은 참인 값을 가지므로 나온다 (불자료형 참고)
a = "python"
if a:
     print("참입니다")