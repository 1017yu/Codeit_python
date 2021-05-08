#  문자열은 수정이 불가하므로 리스트로 변환하는 작업이 필요하다.
def mask_security_number(security_number):
    num_list = list(security_number)  # security_number를 리스트로 변환

    #  마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

    #  리스트를 문자열로 재변환
    total_str = ""
    for i in range(len(num_list)):
        total_str += num_list[i]

    return total_str  # 문자열로 재변환한 total_str을 리턴


#  사실 간단한 방법은 mask_security_number 함수에 return security_number[:-4] + '****' 로 슬라이싱하면 된다


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))