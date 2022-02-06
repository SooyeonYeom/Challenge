# Challenge1 / 난이도5 / 1번 문제

# 문제 1) 1부터 30까지의 정수 중 컴퓨터가 랜덤으로 정한 숫자를 알아맞히는 랜덤 숫자 게임을 만들어보세요.
#  정답이 아닐 시 사용자가 입력한 숫자보다 높은지(UP), 낮은지(DOWN) 알려주는 힌트를 출력해주세요.
#  (사용자가 정답을 맞출 때까지 게임은 계속됩니다.)


# Quiz1

## <논리 상상> ##
# 1) 1부터 30까지 중 랜덤으로 정답 정하기
# 2) 인픗값으로 숫자 맞히기 반복하기
# 3) 정답이 아닐시 해당 인풋값이 정답값보다 높은지 낮은지 알려주는 힌트 함께 출력하기


## <풀이 성공> ##


import random

ANS = random.randint(1, 30)

flag = False

C = f"\n!CORRECT! 정답입니다. 제가 좋아하는 숫자는 {ANS}입나다!"
W = f"\n!WRONG! 틀렸습니다. 제가 좋아하는 숫자는 {ANS}보다 높은 수입니다."
W2 = f"\n!WRONG! 틀렸습니다. 제가 좋아하는 숫자는 {ANS}보다 낮은 수입니다."


while True:
    if flag:
        A = int(input("\n다시 기회를 드릴게요. 1부터 30까지 중, 제가 좋아하는 숫자를 맞춰보세요. : "))

        if A == ANS:
            print(C)
            break

        elif A < ANS:
            print(W)
            continue

        else:
            print(W)
        continue

    else:

        A = int(input("\n1부터 30까지 중, 제가 좋아하는 숫자를 맞춰보세요. : "))

    if A == ANS:
        print(C)
        break

    elif A < ANS:
        print(W)
        flag = True
        continue

    else:
        print(W2)
        flag = True
        continue


print()
print()
print()


# 후기 :  랜덤인트로 정답값 랜덤추출, 맞거나 틀린건(높고 낮은건) if문으로 출력, 반복되는건 while문으로 반복
