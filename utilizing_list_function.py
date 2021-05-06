# 1. 빈 리스트 만들기
numbers = []
print(numbers)


# 2. numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)

print(numbers)


# 3. numbers에서 홀수 제거
a = 0

while a < len(numbers):
    if numbers[a] % 2 != 0:
        del numbers[a]
    else:
        a += 1
print(numbers)


# 4. numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)


# 5. numbers를 정렬해서 출력
numbers.sort()
print(numbers)

# new_numbers = sorted(numbers)
# print(new_numbers)

# 6. numbers를 역으로 정렬해서 출력
numbers.reverse()
print(numbers)

# 7. numbers에 6이 있는지 찾기.
print(6 in numbers)

# 8. numbers에 6이 없는지 찾기.
print(6 not in numbers)

# 9. numbers 원소의 인덱스를 리턴.
print(numbers.index(14))
