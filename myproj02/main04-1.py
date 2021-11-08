import random
import time

animal_names = ["cat", "dog", "fox", "monkey",
                "mouse", "panda", "frog", "snake", "wolf"]

input("준비되셨으면, 엔터키를 입력해주세요.")

random.shuffle(animal_names)

begin_time = time.time()

count = 0
text = 0

for random_name in animal_names[0:5]:
    print(random_name)
    line = input(">>> ")
    text += len(line)
    if random_name == line:
        count += 1
        print("정확합니다!")
    else:
        print("오타가 있군요.")

end_time = time.time()
t = end_time-begin_time
speed = int(text / t * 60)

print(f"{count}번 성공하셨습니다.")
print(f"총 {t}초가 걸리셨어요.")
print(f"타이핑 속도는 {speed}입니다.")
