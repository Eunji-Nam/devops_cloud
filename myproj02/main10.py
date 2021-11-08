def get_max_number(number_list):
    number = number_list[0]  # index 참조
    for current_numer in number_list:
        if current_numer > number:
            number = current_numer
    return number


def get_max_index(number_list):
    number = number_list[0]
    index = 0
    max_index = 0
    for current_numer in number_list:
        if current_numer > number:
            number = current_numer
            max_index = index
        index += 1
    return max_index


numbers = [17, 92, 18, 33, 58, 7, 33, 42]

print(get_max_number(numbers))  # 92일 것이라 기대
print(get_max_index(numbers))


def get_max_number(number_list):
    number = number_list[0]
    for current_numer in number_list:
        if current_numer > number:
            number = current_numer
    return number


def get_max_index(number_list):
    number = number_list[0]
    max_index = 0
    for index, current_numer in enumerate(number_list):
        if current_numer > number:
            number = current_numer
            max_index = index
    return max_index


numbers = [17, 92, 18, 33, 58, 7, 33, 42]

print(get_max_number(numbers))
print(get_max_index(numbers))
