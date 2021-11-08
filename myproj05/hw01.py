from random import randint

number = randint(1, 100)

for retry in range(1, 11):
    line = input(f"[{retry}] Try guess number : ")
    answer = int(line.strip() or 0)  # strip => 앞뒤 빈 공간 제거
# Minimum Valuable Product(MVP) 최대한 간단하게 구성

    try:
        # answer = int(line.strip() or 0)
        answer = int(line.strip())
    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
        continue

    if answer == number:
        print(f"{retry}회 시도에 성공!")
        break
    elif answer < number:
        print("더 큰 수를 입력해주세요.")
    else:
        print("더 작은 수를 입력해주세요.")
else:
    print("다음 기회에...")
