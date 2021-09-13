import random

def get_lottery_number():
    number = random.sample(range(1, 50), 10)
    number.sort()
    return number

print(get_lottery_number())