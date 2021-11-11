"""
Quiz: 지정 조건의 인자만 처리하기
filter_fn을 True로 판정된 인자는 alter_value 값으로 대체해봅시다. 
"""

# 1


def myfilter(filter_fn, alter_value):
    def wrap(fn):
        def inner(*args):
            # TODO : new_args를 적절히 구성해주세요
            # new_args는 리스트 및 튜플 자료구조가 가능합니다
            new_args = []
            for i in args:
                if filter_fn(i):
                    new_args.append(alter_value)
                else:
                    new_args.append(i)
            return fn(*new_args)
        return inner
    return wrap


# 2
def myfilter(filter_fn, alter_value):
    def wrap(fn):
        def inner(*args):
            # TODO : new_args를 적절히 구성해주세요
            # new_args는 리스트 및 튜플 자료구조가 가능합니다
            new_args = []
            for i in args:
                new_args.append(
                    alter_value if filter_fn(i) else i
                )
            return fn(*new_args)
        return inner
    return wrap


@myfilter(lambda i: i % 2 == 0, 0)   # 0이 alter_value
def mysum(a, b, c, d, e):
    return a + b + c + d + e


@myfilter(lambda i: i % 2 == 0, 1)
def mymultiply(a, b, c, d, e):
    return a * b * c * d * e


print(mysum(1, 2, 3, 4, 5))  # 9
print(mymultiply(1, 2, 3, 4, 5))  # 15
