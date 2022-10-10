def add_digits(num:int):
    return (num % 10) + int(num / 10)


def get_partial_sum(number:str)->int:
    double_digit = True
    partial_sum:int = 0
    for index in range(len(number)-1,-1,-1):
        c = number[index]
        if double_digit:
            partial_sum += add_digits(int(c)*2)
        else:
            partial_sum += int(c)
        double_digit = not double_digit
    return partial_sum


def get_last_digit(number):
    a = get_partial_sum(number)
    remainder = a % 10
    if remainder == 0:
        return 0
    else:
        return 10 - remainder


def do_test_case():
    numbers = input().split(' ')
    for num in numbers:
        digit = get_last_digit(num)
        print(digit, end='')
    print()


for i in range(5):
    do_test_case()
