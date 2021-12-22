import random

_number = []
_user_number = []
fool_flag = False
bulls, cows = 0, 0


def generate_number():
    global _number
    _number = [random.randint(1, 9)]
    for i in range(3):
        # _number[i]=int(input())
        new_number = random.randint(0, 9)
        while new_number in _number:
            new_number = random.randint(0, 9)
        _number.append(new_number)
    print(_number)


def input_user_number(guess_number):
    global fool_flag
    global _user_number
    _user_number = []
    # guess_number = str(guess_number)
    for i in range(4):
        new_user_number = int(guess_number[i])
        if (new_user_number in _user_number) or (int(guess_number[0]) == 0):
            print('Дурак')
            fool_flag = True
            break
        else:
            _user_number.append(int(guess_number[i]))

    print(_user_number)


def fool_check():
    global fool_flag
    if fool_flag:
        global _user_number
        _user_number = [random.randint(1, 9)]
        for i in range(3):
            # _number[i]=int(input())
            new_number = random.randint(0, 9)
            while new_number in _user_number:
                new_number = random.randint(0, 9)
            _user_number.append(new_number)
        fool_flag = False
        print(_user_number)


def comparison():
    hidden_number = _number
    attemption = _user_number
    global bulls, cows
    bulls = 0
    cows = 0
    for i in range(len(hidden_number)):
        if attemption[i] == hidden_number[i]:
            bulls += 1
        if (attemption[i] in hidden_number) and (attemption[i] != hidden_number[i]):
            cows += 1
    print(bulls, cows)


def game_in_progress():
    if bulls == 4:
        return False

# generate_number()
# x = input()
# input_user_number(x)
# # comparison()
# print(fool_flag)
