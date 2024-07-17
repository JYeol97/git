# time.time() : 현재 시간을 초 단위로 변환
# datetime.time(hour, minute, second) : 지정된 시간을 나타내는 time 객체 생성
# datetime.strftime(format): datetime 객체를 문자열로 변환합니다.
# datetime.strptime(date_string, format): 문자열을 datetime 객체로 변환합니다.
# from ?? import : datetime 클래스 얻기 위해 from 사용, timedelta 는 두 날짜 또는 시간 사이의 차이
# (특정 날짜에서 일정 기간을 더하거나 뺄 때)
# current_time : datettime 코드로 생성된 datetime 객체를 가리킴
# adjusted_time : 새로운 변수
# from datetime import datetime, timedelta : timedelta는 시간 더하기 빼기
# datetime : 날짜와 시간을 조작하고 표현하기 위한 클래스
# import datetime
# H = int(input())
# M = int(input())

# time_obj = datetime.time(H,M)

# print(time_obj)

# import datetime
# H = int(input())
# M = int(input())
# datetime.strftime(format, H,M)

from datetime import datetime, timedelta

H, M = map(int, input().split())

current_time = datetime(2024, 7, 14, H, M)

adjusted_time = current_time - timedelta(minutes=45)

print(adjusted_time.hour, adjusted_time.minute)

