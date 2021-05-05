# 상수  (constant): 대문자로 작성
PI = 3.14  # 원주율 '파이'


# 반지름을 받아서 원의 넓이 계산
def calculate_area(r):
    return PI * r * r


radius = 4  # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print(f"반지름이 {radius}면, 넓이는 {calculate_area(radius)}")

radius = 7
print(f"반지름이 {radius}면, 넓이는 {calculate_area(radius)}")
