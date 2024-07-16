# while 조건문:
#     수행할_문장1
#     수행할_문장2
#     수행할_문장3
#     ...

treeHit = 0
while treeHit < 10:
     treeHit = treeHit +1  # treehit +=1 로 줄일 수 있음
     print("나무를 %d번 찍었습니다." % treeHit)
     if treeHit == 10:
         print("나무 넘어갑니다.")


# while문 만들기
prompt = """
 1. Add
 2. Del
 3. List
 4. Quit

 Enter number: """

number = 0
while number != 4:
     print(prompt)
     number = int(input())


# while 문 중지 (검사할때)
coffee = 10
money = 300
while money:
     print("돈을 받았으니 커피를 줍니다.")
     coffee = coffee -1
     print("남은 커피의 양은 %d개입니다." % coffee)
     if coffee == 0:
         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
         break


# coffee.py
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

# while 문 맨 처음으로 돌아가기
a = 0
while a < 10:
     a = a + 1
     if a % 2 == 0:  # %는 나머지 (2로나눈 나머지가 0이니?)
         continue  # 다시 돌아가라 만약 pass를 사용하면 지나간다 또한 가장 가까운 while문 으로 돌아감
     print(a)

# 무한 루프 정지법
# while True: 
#     수행할_문장1 
#     수행할_문장2

while True:
     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

# 무한 루프 메모리 누수는 챗gpt사용