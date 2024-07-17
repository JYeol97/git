# # 코드 수정됨
# print('안녕하세요')

# a=3

# b=5

# a=print(b)
# b=print(a)

# 사과는 영어로 apple
# 바나나는 영어로 banana
# 키위는 영어로 kiwi

# A = "사과는 영어로 apple"
# B = "바나나는 영어로 banana"
# K = "키워는 영어로 kiwi"
# print(A)
# print(B)
# print(K)
# python ex_1_2.py

# korean = "한글"
# english = "english"
# number = 3

# print(f'{korean}과 {english}')
# print(korean*number)


# score_jy = int(input())

# if score_jy > 90:
#     print('A')
# elif score_jy > 80:
#     print('B')
# elif score_jy > 70:
#     print('C')
# else:
#     print('F')



# password 문장에서 
password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# first_char 는 28번째 35번째
# second_char 는 113번째부터 총 5글자
# third_word 는 66~68 뒤집어서
# fourth_word 322 부터 4글자 뒤집어서
# fifth_wrod 365 'python' 이다.

# life is short you need "python".


# first_char = password[27:35]
# second_char = password[113:118]
# third_word = password[68:65:-1]
# fourth_word = password[325:321:-1]
# fifth_word = password[365:372]
# print(f'{first_char} {second_char} {third_word} {fourth_word} {fifth_word}')

# 중괄호를 사용 key : value 를 :를 사용하여 구분함
# dic = {'name' : 'pey', 'phone' : '010-9220-1761', 'birth' : 1110}
# print(dic)
# print(type(dic))

# dic = {'name' : 'pey', 'age' : '20',}
string = '문자열'
integer = 10
floating_point = 3.14
a_list = [1, 2, 3, 4, 5]
dictionary = {'name': '홍길동', 'age': 20}
a_set = {1, 2, 3, 4, 5}
a_range = range(11)
a_tuple = (1, 2, 3)
boolean = True

print(type(string))
print(type(integer))
print(type(floating_point))
print(type(a_list))
print(type(dictionary))
print(type(a_set))
print(type(a_range))
print(type(a_tuple))
print(type(boolean))

