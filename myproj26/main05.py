# list
# 항상 좌항과 우항의 개수가 같아야 함.
name, age, region = ["Tom", 10, "Seoul"]

# name만 저장하고 싶을 때
name, *extra = ["Tom", 10, "Seoul"]
name, *__ = ["Tom", 10, "Seoul"]

# age만 저장하고 싶을 때
__, age, __ = ["Tom", 10, "Seoul"]
