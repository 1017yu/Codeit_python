from random import randint


def generate_numbers():
    numbers = []  # 리스트 numbers 생성

    while len(numbers) < 3:  # 3개의 요소 생성
        new_number = randint(0, 9)  # 0 이상 9 이하의 숫자를 담는 변수 정의
        if new_number not in numbers:  # 중복 방지
            numbers.append(new_number)  # 리스트 numbers 에 new_number 추가

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []

    while len(new_guess) < 3:
        first_num = int(input(f"{len(new_guess) + 1}번째 숫자를 입력하세요: "))
        if first_num > 9 or first_num < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif first_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(first_num)

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    n = 0

    while n < 3:
        if guess[n] == solution[n]:
            strike_count += 1

        elif guess[n] != solution[n] and guess[n] in solution:
            ball_count += 1

        n += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0

while True:
    my_guess = take_guess()
    S, B = get_score(my_guess, ANSWER)
    print(f"{S}S {B}B")
    tries += 1

    if (S, B) == (3, 0):
        break

print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.")

