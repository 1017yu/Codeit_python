import random  # 랜덤 모듈

ANSWER = random.randint(1, 20)  # 1 이상 20 이하의 무작위 정수를 ANSWER 상수에 저장
NUM_TRIES = 4  # 4번의 기회를 NUM_TRIES 상수에 저장
guess = -1  # input 문자열값을 guess라는 변수에 정수로 저장하기 위해 guess 변수 생성
tries = 0  # 정답시도 횟수를 tries 변수에 저장

while guess != ANSWER and tries < 4:  # input값과 ANSWER 정답이 같지않고, 기회가 남아있을 동안 while문 반복
    guess = int(input(f"기회가 {NUM_TRIES - tries}번 남았습니다. 1~20 사이의 숫자를 맞혀보세요: "))  # input 함수의 리턴값을 정수형으로 형 변환
    tries += 1  # 정답 시도 횟수 + 1

    if guess == ANSWER:  # input 값과 ANSWER 값이 같을 경우, 메시지 출력
        print(f"축하합니다! {tries}번 만에 맞혔습니다!")

    if tries == 4:  # 정답을 맞히지 못하고, 정답 시도 횟수가 4일 때, 메시지 출력
        print(f"아쉽습니다. 정답은 {ANSWER}였습니다.")
        break

    elif guess > ANSWER:
        print("DOWN")

    elif guess < ANSWER:
        print("UP")













