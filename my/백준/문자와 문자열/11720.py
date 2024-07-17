# # 문제
# # N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# # 입력
# # 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# # 출력
# # 입력으로 주어진 숫자 N개의 합을 출력한다.
# N = int(input())
# numbers = map(int, input().split())
# a = [numbers[::1]]
# print(sum(a))

# N = int(input())
# numbers = list(map(int, input().split()))
# a = [numbers[::1]]
# b = sum(a)
# print(a)

# N = int(input())
# numbers = list(map(int, input().split()))
# a = numbers 
# print(sum(a))  

N = int(input())  
numbers = input().strip()  # 공백 없는 숫자 문자열 만듬
total = sum(map(int, numbers))  # numvers의 각 문자를 정수로 변환하여 합산
print(total)  
