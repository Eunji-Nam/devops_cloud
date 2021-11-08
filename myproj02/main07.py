def 부가세_계산(금액):
    부가세 = 금액 // 11
    return 부가세
# return 하지 않으면 결과값이 나오지 않음 (return none)


부가세 = 부가세_계산(20000)
print(f"부가세 : {부가세}")
