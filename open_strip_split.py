with open('data/chicken.txt', 'r') as f:  # data 폴더의 chicken.txt를 f라는 이름으로 읽어들임
    for line in f:  # for 반복문 통하여 f를 출력하기
        print(line)  # f의 첫 줄을 변수 line에 저장, 반복
        print(line.strip())  # line문의 공백을 .strip()로 제거


full_name = "Kim, Yuna"
name_data = full.name.split(", ")  # ,\n 을 기준으로 split

last_name = name_data[0]  # name_data의 'Kim'을 last_name에 저장
first_name = name_data[1]  # name_data의 'Yuna'를 first_name에 저장

print(first_name, last_name)  # Yuna Kim
