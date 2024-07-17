N = int(input())  
numbers = input().strip()  # 공백 없는 숫자 문자열 만듬
total = sum(map(int, numbers))  # numbers의 각 문자를 정수로 변환하여 합산
print(total)  

word = input().strip()
