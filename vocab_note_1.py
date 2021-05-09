with open('vocabulary.txt', 'r', encoding="utf-8") as f:  # f라는 변수에 vocabulary.txt 를 read 버전으로 오픈

    for line in f:  # for 반복문으로 f 함수의 line 을 반복 호출
        i = (line.strip().split(": "))  # 각 line 의 영어 단어와 한국어 뜻을 분리해서 변수 i 에 저장

        eng_word, kor_word = i[0], i[1]  # i 리스트이 0번 데이터를 eng_word, 1번 데이터를 kor_word에 저장

        guess = input(f"{kor_word}: ")  # input 으로 받은 영어 단어를 guess 변수에 저장
        while True:  # while 반복문 (무한 loop 에 빠지지 않게 break 걸어줘야함)
            if guess == eng_word:  # guess 변수값이 eng_word 정답과 같다면,
                print("맞았습니다!")  # 메시지를 출력하고 break
                break

            else:  # guess 변수값이 eng_word 정답과 다르다면,
                print(f"아쉽습니다. 정답은 {eng_word}입니다.")  # 메시지를 출력하고 break
                break









# 고양이: cat
# 사과: apple
# 교회: church
# 절: temple
# 지갑: wallet
# 책가방: backpack
# 비누: soap
# 자전거: bicycle

