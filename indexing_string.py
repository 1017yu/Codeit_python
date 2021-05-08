# 알파벳 리스트의 인덱싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0])  # A
print(alphabets_list[1])  # B
print(alphabets_list[4])  # E
print(alphabets_list[-1])  # J

# 알파벳 문자열의 인덱싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0])  # A
print(alphabets_string[1])  # B
print(alphabets_string[4])  # E
print(alphabets_string[-1])  # J


# 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:  # alphabets_list 에 있는 알파벳을 alphabet 이라는 변수에 지정
    print(alphabet)


# 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:  # alphabets_string 에 있는 알파벳을 alphabet 이라는 변수에 지정
    print(alphabet)


# 알파벳 리스트의 슬라이싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])  # 'A'부터 'E'까지
print(alphabets_list[4:])  # 'E'부터 끝까지
print(alphabets_list[:4])  # 처움부터 'D'까지
print(alphabets_list[4::-2])  # 리스트를 reverse하고, E부터 2칸씩 슬라이싱

# 알파벳 문자열의 슬라이싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])  # A부터 E까지
print(alphabets_string[4:])
print(alphabets_string[:4])


# len 함수의 활용
# 리스트의 길이 재기
print(len(['H', 'E', 'L', 'L', 'O']))

# 문자열의 길이 재기
print(len("Hello, world!"))

# 리스트 데이터 바꾸기
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)  # Mutable

# 문자열 데이터 바꾸기
name = "codeit"
name[0] = "C"
print(name)  # Immutable
