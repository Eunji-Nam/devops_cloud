

def mysum3(x, y):
    return x + y + 10


def mysum3(x, y, z):
    return x + y + z + 10

# 가변인자


def mysum(x, y, *args):  # 최소 2개 이상 받고 싶을 때, 인자 x, y 추가
    #args in tuple
    print("args :", args)
    return x + y + sum(args) + 10


print(mysum(1, 2))
print(mysum(1, 2, 3))
