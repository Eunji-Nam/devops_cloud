def gugudan(number):
    # number = 2
    print(f"--- {number}단 ---")
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")


gugudan(2)
gugudan(3)
gugudan(4)
gugudan(5)
gugudan(6)
gugudan(7)
gugudan(8)
gugudan(9)

# 코드의 함수 호출부를 for 반복문으로 변경하기.
for number in range(2, 10):
    gugudan(number)
