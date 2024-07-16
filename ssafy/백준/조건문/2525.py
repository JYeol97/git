# from datetime import datetime, timedelta

# A, B, C = map(int, input().split())

# current_time = datetime(2024, 7, 14, A, B) 

# adjust_time = current_time - timedelta(minutes=C)

# print(adjust_time)

# datetime 객체는 문자열로 출력 불가

from datetime import datetime, timedelta  # 클래스 사용

A, B, C = map(int, input().split())

current_time = datetime(2024, 7, 14, A, B) 

adjust_time = current_time - timedelta(minutes=C)

adjust_hour = adjust_time.hour     # .hour 을 붙여서 시간만 가져오겠다
adjust_minute = adjust_time.minute        # .minute 을 붙여서 분만 가져오겠다

print(adjust_hour, adjust_minute)

###########################################################
from datetime import datetime, timedelta

A, B = map(int, input().split())
C =int(input())

current_time = datetime(2024, 7, 14, A, B) 

adjust_time = current_time + timedelta(minutes=C)

adjust_hour = adjust_time.hour
adjust_minute = adjust_time.minute 

print(adjust_hour, adjust_minute)