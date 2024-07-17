# # 조건부 표현식
# score = 80
# if score >= 60:
#     message = "success"
# else:
#     message = "failure"
# print(message)

score = map(int, input().split())

if score >= 90:
    message = "A"
elif score >= 80:
    message = "B"
elif score >= 70:
    message = "C"
elif score >=60:
    message = "D"
else:
    message = "F"

print(message)