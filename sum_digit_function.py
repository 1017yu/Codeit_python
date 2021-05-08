# 자리수 합 리턴
def sum_digit(num):  # num 이라는 변수를 받아오는 함수 정의
    total = 0  # total 변수 생성
    str_num = str(num)  # 정수형 num을 string으로 변경

    for digit in str_num:  # str_num 속 문자열을 불러와서 반복문 실행
        total += int(digit)  # total이라는 변수에 integer로 바꾼 digit을 저장

    return total  # for문이 끝나면 total 변수를 리턴


digit_total = 0  # 1부터 1000까지 더하기 위해 digit_total 변수 생성
for i in range(1, 1001):  # i가 1부터 1000까지
    digit_total += sum_digit(i)  # digit_total 변수에 자릿수 합을 반복 합

print(digit_total)

# i = 1 이면 for문이 TRUE이므로, digit_total 변수에 sum_digit(1)의 값인 1이 더해짐
# i = 12 이면 for문이 TRUE이므로, digit_total 변수에 sum_digit(12)의 값인 1과 2가 더해짐