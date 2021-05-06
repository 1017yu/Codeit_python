# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# while 반복문을 이용하여 리스트의 값을 변경
a = 0
while a < 6:
    temperature_list[a] = round(fahrenheit_to_celsius(temperature_list[a]), 1)
    a += 1

print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력
