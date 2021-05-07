# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전

    # dict의 key와 value를 뒤집어서 new_dict에 저장
    for key, value in vocab.items():
        new_dict[value] = key  # != new_dict[key] = value

    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print(f"영-한 단어장\n{vocab}\n")

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print(f"한-영 단어장\n{reversed_vocab}")