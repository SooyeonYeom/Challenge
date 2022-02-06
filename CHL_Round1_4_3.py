# Challenge1 / 난이도4 / 3번 문제

# 문제 3) 주민등록번호를 인자로 입력받으면 생년월일과 성별을 출력하는 함수를 만들고 직접 인자를 넣어 실행해보세요.
# (주민등록번호 입력 시 '-'을 포함합니다.)


# Quiz3

## <논리 상상> ##
# 1)주민등록번호 입력 받아서 문자열 슬라이싱으로 생년월일 출력하기.
# 2)주민등록번호 뒷자리 첫번째 글자 짝수면 여자 홀수면 남자 출력하기


## <풀이 성공> ##


PN = input("\n주민등록번호를 입력해주세요. (xxxxxxxx - yyyyyyy): ")

B = PN[:4]

M = PN[4:6]

D = PN[6:8]

S = int(PN[10:12])


if S % 2 == 0:
    print(f"\n당신은 {B}년 {M}월 {D}일에 태어났고, 여성분이네요. ")
else:
    print(f"\n당신은 {B}년 {M}월 {D}일에 태어났고, 남성분이네요. ")


print()
print()
print()


# 후기 :  '%' = 나눈 후, 나머지 반환 : 배수 구할떄 사용
#        18은 3의 배수가 맞다.   (18%3 == 0) = True
#        홀짝 여부 체크 시 사용 가능 (짝수는 2로 나누면 나머지가 0이니까)
