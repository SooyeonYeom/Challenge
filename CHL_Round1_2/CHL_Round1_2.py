# Challenge 2

# 문제 1) 이름과 비밀번호를 설정하여 사용자가 알맞게 입력했을 시 환영 인사를, 실패 시 실패한 이유를 출력하세요. (O)

# 문제 2) 사용자로부터 생일을 입력받고, 사용자가 태어난 계절을 출력하는 함수를 만드세요. (O)

# 문제 3) 사용자로부터 이름을 입력받고, 성과 이름을 나누어 출력하는 함수를 만드세요. (O)

# 문제 4) 사용자로부터 숫자 2개를 입력받고, 두 숫자 사이에서 랜덤으로 숫자 하나를 출력하는 함수를 만드세요. (O)

# 문제 5) 동물의 이름을 입력하면 해당 동물의 울음소리가 출력되게 만들어보세요. 동물의 종류는 세가지 이상으로 해주세요. (0)


# Quiz1 로그인


while True:
    print("ID를 입력해주세요.")
    ID = input("")
    if ID == "ponyo":
        break

    else:
        print("\n옳지않은 ID입니다. 다시 확인해주세요.")
        continue

while True:
    print("\n비밀번호를 입력해주세요.")
    PW = input("")
    if PW == "iscute":
        break

    else:
        print("\n옳지않은 비밀번호입니다. 다시 확인해주세요.")
        continue


print(f"\n환영합니다, {ID}님! 오랜만이네요..")


# 프로필 시작

while True:

    print(f"\n아직 {ID}님의 프로필이 완성되지 않았습니다. 프로필을 설정하시겠습니까?\n\n1. [예] \n2. [아니오]")
    ch2 = input("")
    if ch2 == "1":
        break
    else:
        print("\n다음에 다시 설정해주세요.")
        continue


# Quiz3 이름 받아서 성/이름 구분하기

while True:
    name = input("\n당신의 이름은 무엇인가요? (성+이름) :")

    family_name = name[:1]
    first_name = name[1:]

    print(f"\n당신의 성은 {family_name}이고, 이름은 {first_name}이군요. 맞나요?\n\n1. [예] \n2. [아니오]")
    ch3 = input("")
    if ch3 == "1":
        break
    else:
        print("\n잘못들었네요. 다시 말씀해주시겠어요?")
        continue


# Quiz2 생일 받아서 계절 맞추기

birth = input(f"\n좋아요, {first_name}님. 당신의 생일은 언제인가요? (yyyy mm dd) :")

year = birth[:4]
month = int(birth[4:7])
day = birth[7:]


if 12 or 1 <= month <= 2:
    print(f"\n당신은 {year}년, {month}월, {day}일, 낭만과 캐롤이 흐르는 추운 겨울날에 태어나셨네요.")
elif 3 <= month <= 5:
    print(f"\n당신은 {year}년, {month}월, {day}일, 꽃들이 기지개 피는 따뜻한 봄날에 태어나셨네요.")
elif 6 <= month <= 8:
    print(f"\n당신은 {year}년, {month}월, {day}일, 시원한 바람과 햇빛이 나리는 여름날에 태어나셨네요.")
else:
    print(f"\n당신은 {year}년, {month}월, {day}일, 청명한 하늘과 단풍이 불거지는 가을날에 태어나셨네요.")


# Quiz4 사용자에게 인풋값 여러개 받아서 랜덤 추출

print(f"\n다음 질문을 드릴게요, {first_name}님.")

import random


num1 = input(f"\n{first_name}님이 가장 좋아하는 요일은 무슨 요일인가요?")
num2 = input(f"\n그렇군요, 그럼 {first_name}님이 가장 지치는 요일은 무슨 요일인가요?")
num3 = input(f"\n마지막으로, 당신이 가장 싫어하는 요일은 무슨 요일인가요?")

nums = [num1, num2, num3]

ran = [random.choice(nums) for i in range(1)]

print(f"\n그렇군요.. 저는 개인적으로.. {ran}을 가장 좋아해요. 이유는 따로 없어요.")


# Quiz5 인풋값 입력시 해당 값의 사운드 재생


##<기본풀이 : if문 활용>

# from playsound import playsound


# print(f"\n{first_name}님은 고양이, 강아지, 새 중에 좋아하는 동물이 있나요..? : ")


# ch1 = input("")
# if ch1 == "고양이":
#     print(f"하하...{first_name}님의 말을 들었는지, 고양이도 인사를 하네요. ")
#     playsound("CHOCO_CHL/Sound1.mp3")
# elif ch1 == "강아지":
#     print(f"하하...{first_name}님의 말을 들었는지, 강아지도 인사를 하네요. ")
#     playsound("CHOCO_CHL/Sound2.mp3")
# else:
#     print(f"하하...{first_name}님의 말을 들었는지, 새도 인사를 하네요. ")
#     playsound("CHOCO_CHL/Sound3.wav")


##<확장풀이 : dictionary 활용>


from playsound import playsound

first_name = "수연"


animal = {
    "강아지": "CHL_Round1_2/Sound2.mp3",
    "고양이": "CHL_Round1_2/Sound1.mp3",
    "참새": "CHL_Round1_2/Sound3.wav",
}


Q = input(f"\n{first_name}님은 고양이, 강아지, 참새 중에 좋아하는 동물이 있나요..? : ")


print(f"\n하하...{first_name}님의 말을 들었는지, 저 친구도 인사를 하네요.")


playsound(animal[f"{Q}"])


print(f"\n이제 헤어질 시간이에요..다음에 또 만나요 {first_name}님.")


print()
print()
print()


###후기 : 난......천재....?
