#  아직 수정이 많이 필요한 초안입니다. :(

import random  # 랜덤 모듈


#  무작위 번호 추출 함수
def generate_numbers(n):
    numbers = []  # number 리스트 생성

    i = 0
    while i < n:  # n개의 무작위 숫자 생성
        number = random.randint(1, 45)
        if number not in numbers:  # 숫자 중복 방지
            numbers.append(number)
            i += 1

    return numbers  # while 반복문이 끝나면 ex_number 리스트를 리턴


def draw_winning_numbers():
    numbers = []  # ex_number 리스트 생성
    i = 0
    while i < 6:  # 6개의 무작위 번호 생성
        number = random.randint(1, 45)
        numbers.append(number)
        i += 1
    numbers.sort()  # 첫 6개의 무작위 번호 정렬
    bonus = random.randint(1, 45)  # 무작위 보너스 번호 생성
    numbers.append(bonus)  # 정렬한 6개의 번호에 보너스 번호 추가
    return numbers  # ex_number 를 리턴


def count_matching_numbers(a, b):  # 두 개의 리스트를 비교해서 중복되는 개수를 카운팅하는 함수 정의
    list_1 = a  # 첫 번째 파라미터 정의
    list_2 = b  # 두 번째 파라미터 정의
    list_3 = []  # 가상의 세번째 리스트 생성

    for i in list_1:  # i가 list_1의 원소를 호출
        if i in list_2:  # i가 list_2의 원소와 겹친다면
            list_3.append(i)  # list_3 리스트에 원소를 추가

    return len(list_3)  # list_3의 리스트 안의 원소 개수를 리턴


def check(numbers, winning_numbers):
    a = numbers
    b = winning_numbers
    count = []

    for i in a:
        if i in b:
            count.append(i)

    if len(count) == 6 and int(b[6]) not in count:
        return print("10억 원")

    elif len(count) == 6 and int(b[6]) in count:
        return print("5천만 원")

    elif len(count) == 5 and int(b[6]) not in count:
        return print("100만 원")

    elif len(count) == 4:
        return print("5만 원")

    elif len(count) == 3:
        return print("5천 원")

    elif len(count) <= 2:
        return print("낙첨되셨습니다.")


numbers_test = [1, 3, 14, 28, 40, 0]
winning_numbers_test = [1, 3, 14, 28, 40, 41, 6]

print(check(numbers_test, winning_numbers_test))

