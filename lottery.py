import random

def get_lottery_number():
    number = random.sample(range(1, 50), 10)
    number.sort()
    return number


if __name__ == '__main__':
    print(get_lottery_number())