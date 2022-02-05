# Challenge1 / 난이도3 / 3번 문제

# 문제 3) 10초부터 1초 단위로 시간 지연을 주며 0초까지 카운트 다운하게 만들어보세요. (O)

# Quiz3 10부터 0까지 역순으로 세며, 시간 지연 주면서 카운트 다운되게 만들기

## <논리 상상> ##
# 1) 1부터 10까지 카운트하려면 일단 리스트에 1~10 넣어야 할듯
# 2) 시간 지연을 주려면 time 모듈 물러와서 sleep 함수 써야될 듯
# 3) 여기서도 pop()쓰면 간단하게 짤 수 있지 않을까?

## <풀이 성공> ##

import time
from playsound import playsound

print()
print()


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 리스트 만들고

ok = input("2022년 1월 1일의 새해가 밝기 10초 전..! 준비되셨나요? \n\n1. 준비됐습니다! \n2. 준비됐어요!")
if ok == "1":
    print("\n새해 10초 카운트다운 시작합니다!")
else:
    print("\n새해 10초 카운트다운 시작합니다!")

print()

for i in range(10):
    num = list.pop()  # 역순으로 지워가며 뽑기
    print(f"\n{num}..")  # 안내문 출력
    playsound(f"{num}.mp3")  # 사운드 출력
    time.sleep(0.2)  # 시간 지연

print("\n0~!! 2022년 새해가 밝았습니다~!")

playsound("HNY.mp3")


print()
print()
print()


# 후기 : 쏘 이지 ^^ 사운드 활용해봤다 !

# <출제자의 의도>
# for i in range(1, 11):
#     print(11 - i)
