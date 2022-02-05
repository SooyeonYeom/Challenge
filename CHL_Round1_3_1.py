# Challenge1 / 난이도3 / 1번 문제

# 문제 1) 사용자로부터 숫자를 입력받고, 해당 숫자의 구구단을 출력하는 함수를 만드세요. (O)

# Quiz1 인풋값을 받아 해당 인풋값의 구구단(1~9까지 연산)을 출력하기

## <논리 상상> ##

# 1) 크게 보면, 일단 num = int(inpu("")으로 인풋값을 받아야하고
# 2) num 값을 list에 있는 1~9까지의 수와 곱해야 한다.
# 3) 여기서 중요한건 list에서 추출해오는 수들이 "순서"대로 오면서, 동시에 "중복"되어선 안된다는 것.
# 4) 그리고 이 과정이 반복돼야 한다는 것.


## <논리 스케치> ##

# num = int(input("어떤 숫자의 구구단이 궁금한가요?") <인풋값 받기>
# table = [1, 2, 3, 4, 5, 6, 7, 8, 9]        <1~9가 포함된 리스트 만들기>
# result = num * table[x]                    <인풋값*리스트 중 x위치의 값..?>
# for i in range(len(a)):                    <리스트 안 수만큼 반복해야되니까 for문..>
#     print(f"{num} X {table[X]} = {result}")<일단 프린트....???>
#
#!문제발견!    table[x]로 리스트안의 숫자를 "계속 순서대로+중복되지 않게 다르게" 추출하기 어렵다
# ?필요한것?    즉, table[x] 리스트 안의 숫자를 "하나씩, 다르게, 순서대로, 중복이 안되게" 추출해야된다.

# list 함수 중에 써먹을게 있지 않을까? >> 찾아보니 pop() 이라는 재밌는 함수 발견!
# pop()은 리스트 중 하나를 지우는 함수인데, 여기서 del와 다른 점은 "지운 인덱스 값을 반환한다는것!"
# 리스트 중 하나를 지우고, 지운 값을 가져와 쓸 수 있으며, 이를 for문으로 반복한다
#  = "하나씩, 다르게, 중복안되게, 다르게" 가 모두 충족된다!  그래서 생각대로 해봤다 :-)


## <풀이 성공> ##

num = int(input("어떤 숫자의 구구단이 궁금한가요?"))  # <인풋값 받기>

print(f"{num}의 구구단은 아래와 같습니다.")  # <안내문>

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]  # <역순으로 진행되는 pop()함수라 역순으로 리스트 만들기>

for i in range(len(a)):  # <리스트 안 수 만큼 반복하는 for문>
    removed = a.pop()  # <(지운 인덱스값) 설정>
    result = num * (removed)  # < 결과=인풋값*(지운 인덱스값)>
    print(f"{num} X {removed} = {result}")  # <안내 : "인풋값" X "지운 인덱스 값" = "결과">


print()
print()
print()


###후기 : 근데 pop() 이럴때 쓰는 거 맞긴 함? 몰랑 ~ ^^


# <출제자의 의도>

# num=5

# for i in range(1, 10):
#     print(f"{i}*{num}={i*num}")
