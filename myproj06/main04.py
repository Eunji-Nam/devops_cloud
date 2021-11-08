s = "안녕하세요"

idx = 0

for idx, ch in enumerate(s, 1):
    # 인덱스 1부터 시작. 생략시 처음부터 시작
    print(idx, ch)


numbers = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
]

for idx, (x, y) in enumerate(numbers):
    print(x, y)

"""
enumerate 공식문서 : 
https://docs.python.org/ko/3/library/functions.html#enumerate
"""
