# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자',
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기',
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:  # votes에 있는 이름을 순서대로 name이라는 변수에 지정.
    if name not in vote_counter:
        vote_counter[name] = 1  # 빈 vote_counter에 key와 values를 추가
    else:
        vote_counter[name] += 1  # vote_counter에 key와 value가 이미 있다면 value + 1

# 후보별 득표수 출력
print(vote_counter)