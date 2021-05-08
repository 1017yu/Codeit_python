import random  # random 모듈 불러오기
import datetime  # date 모듈 불러오기

print(random.random())  # 0과 1 사이 무작위 숫자 출력

print(random.randint(1, 20))  # radient 함수 사용으로 1 이상 20 이하의 무작위 integer 출력
print(random.randint(1, 20))


print(random.uniform(0, 2))  # uniform 함수 사용으로 0 이상 2 이하의 무작위 소수 출력
print(random.uniform(0, 2))


pi_day = datetime.datetime(2021, 3, 14, 3, 14, 15)  # pi_day에 datetime.datetime 함수 저장
print(pi_day)
print(type(pi_day))

today = datetime.datetime.now()
print(today)
print(type(today))

# timedelta 활용하기
print(today - pi_day)  # 오늘 날짜와 pi_day간의 날짜 차이
print(type(today - pi_day))


my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)   # 5일 3시간 10분 50초의 timedelta 생성
print(today)
print(today + my_timedelta)  # 오늘로부터 timedelta만큼 이후의 시각 출력

# datetime 포맷팅
print(today)
print(today.strftime("%A, %B %dth %Y"))
