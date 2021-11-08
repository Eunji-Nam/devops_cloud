"""
퀴즈) 코드 와성하기

* 1이상 40이하 범위에서 랜덤수를 획득하고 
* 10 미만이라면 1을 출력하고 
* 10이상 20 미만이라면 10을 출력하고 
* 20 이상 30미만이라면 20을 출력하고 
* 30이상이라면, "너무 큰 수"라고 출력합니다.
* 프로그램 종료 시에 "숫자는 ???입니다."라고 출력
"""

from random import randint

number = randint(1, 40)

if 10 > number:
    print(1)
elif 20 > number:
    print(10)
elif 30 > number:
    print(20)
else:
    print("너무 큰 수")

print(f"숫자는 {number}입니다.")
