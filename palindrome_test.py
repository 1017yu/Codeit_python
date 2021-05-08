#  word라는 변수를 받아오는 함수 정의
def is_palindrome(word):
    word_list = list(word)  # word_list 라는 리스트 정의
    reversed_list = word_list[::-1]  # palindrome을 확인하기 위하여 슬라이싱한 reversed_list를 정의

    return word_list == reversed_list  # 두 리스트가 같으면 palindrome이므로 TRUE 아니면 FALSE를 출력


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))