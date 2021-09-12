import random

START = 1
END   = 50
LIMIT = 11


def get_lottery_number():
    number = [random.randint(START, END) for _ in range(1, LIMIT)]
    number.sort()
    return number


if __name__ == '__main__':
    print(get_lottery_number())