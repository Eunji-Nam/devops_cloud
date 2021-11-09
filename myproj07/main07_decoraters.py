
def base(base_number):
    def fn(x, y):
        return x + y + base_number
    return fn


base_10 = base(10)
base_20 = base(20)

print(base_10(1, 2))
print(base_20(1, 2))

# name = "Tom"
# def mysum(x, y): return x + y

# other_name = name
# other_fn = mysum

# def fn(x):
#     y = "hello"
#     return y

# fn(name)
