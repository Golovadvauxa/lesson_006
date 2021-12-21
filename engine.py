import random

_number = {}


def generate_number():
    global _number
    _number = {}
    for i in range(4):
        if i > 0:
            # _number[i]=int(input())
            _number[i] = random.randint(0, 9)
            for j in _number:
                if i == j:
                    break
                while _number[i] == _number[j]:
                    _number[i] = random.randint(0, 9)

        else:
            _number[i] = random.randint(1, 9)
            # _number[i] = int(input())
    print(_number.values())


def comparison(guess_number):
    _user_number = {}
    for i in range(4):
        _user_number[i] = guess_number

    print(_user_number)


def answer():
    pass


generate_number()
comparison(3234)
