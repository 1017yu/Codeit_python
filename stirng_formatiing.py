# 오늘은 2021년 5월 4일입니다.
year = 2021
month = 5
day = 4

# print("오늘은 " + str(year) + "년 " + str(month) + "월 "+ str(day) + "일입니다.")

print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))  # .format()

date_string = "내일은 {}년 {}월 {}일입니다. 우와 어린이날이다!"  # date_spring 변수 활용
print(date_string.format(year, month, day + 1))

print("저는 {}, {}, {}를 좋아합니다!".format("박지성", "손흥민", "차범근"))

print("저는 {1}, {0}, {2}를 좋아합니다!".format("박지성", "손흥민", "차범근"))  # 순서 바꾸기

num_1 = 1
num_2 = 3

print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))  # floating 소수점 둘째자리까지 출력

print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1 / num_2))  # floating 정수 출력
