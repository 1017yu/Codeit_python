import random  # 랜덤 모듈


#  무작위 번호 추출 함수
def generate_numbers(n):
    numbers = []  # number 리스트 생성

    while len(numbers) < n:  # n개의 무작위 숫자 생성
        number = random.randint(1, 45)
        if number not in numbers:  # 숫자 중복 방지
            numbers.append(number)

    return numbers  # while 반복문이 끝나면 ex_number 리스트를 리턴


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)  # 7개의 무작위 숫자 생성

    return sorted(winning_numbers[:6]) + winning_numbers[6:]  # 앞 6개의 숫자 정렬


def count_matching_numbers(list_1, list_2):  # 두 개의 리스트를 비교해서 중복되는 개수를 카운팅하는 함수 정의
    # 리스트 연산보다 숫자 연산이 더 빠르다.
    duplicated_numbers = 0

    for i in list_1:  # i가 list_1의 원소를 호출
        if i in list_2:  # i가 list_2의 원소와 겹친다면
            duplicated_numbers += 1  # 중복되는 요소의 갯수 저장

    return duplicated_numbers  # 중복되는 갯수 리턴


def check(numbers, winning_numbers):
    general_numbers = winning_numbers[:6]
    check_numbers = count_matching_numbers(numbers, general_numbers)
    bonus_number = winning_numbers[6]

    if check_numbers == 6:
        return 1000000000

    elif check_numbers == 5:
        if bonus_number in numbers:
            return 50000000
        else:
            return 1000000

    elif check_numbers == 4:
        return 50000

    elif check_numbers == 3:
        return 5000

    else:
        return 0




