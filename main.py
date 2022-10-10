def add_digits(num:int):
    return (num % 10) + int(num / 10)


def get_partial_sum(number:str):
    doubleDigit = True
    sum = 0
    for index in range(len(number)-1,-1,-1):
        c = number[index]
        if doubleDigit:
            sum += add_digits(int(c)*2)
        else:
            sum += int(c)
        doubleDigit = not doubleDigit
    return sum


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
