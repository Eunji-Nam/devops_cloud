# 오늘의 과제 01  # 숫자 퀴즈
import random

print("1~100 사이의 숫자를 입력해주세요.")
number = random.randint(1, 100)

count = 1

for count in range(10):
    answer = int(input(""))
    if answer < number:
        print("더 큰 수를 입력해주세요")
        count += 1
    elif answer > number:
        print("더 작은 수를 입력해주세요")
        count += 1
    if answer == number:
        print(f"{count+1}번만에 성공하셨습니다.")
        break

if count == 11:
    print("다음기회에...")
