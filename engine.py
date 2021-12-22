import random

_number = []
_user_number = []
fool_flag = False
bulls, cows = 0, 0


def rules():
    print('Правила:')
    print('Компьютер загадывает четырехзначное число, все цифры которого различны')
    print('(первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.')
    print('Игрок вводит четырехзначное число c неповторяющимися цифрами,')
    print('компьютер сообщают о количестве «быков» и «коров» в названном числе')
    print('«бык» — цифра есть в записи задуманного числа и стоит в той же позиции,')
    print('что и в задуманном числе')
    print('«корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,')
    print('что и в задуманном числе')
    print('Например, если задумано число 3275 и названо число 1234,')
    print('получаем в названном числе одного «быка» и одну «корову».')
    print('Очевидно, что число отгадано в том случае, если имеем 4 «быка».\n\n\n')


def generate_number():
    global _number
    _number = [random.randint(1, 9)]
    for i in range(3):
        # _number[i]=int(input())
        new_number = random.randint(0, 9)
        while new_number in _number:
            new_number = random.randint(0, 9)
        _number.append(new_number)
    print('Число загадано!\nУгадывай')


def input_user_number(guess_number):
    global fool_flag
    global _user_number
    _user_number = []
    # guess_number = str(guess_number)
    for i in range(4):
        new_user_number = int(guess_number[i])
        if (new_user_number in _user_number) or (int(guess_number[0]) == 0):
            print('Дурак!\nЧисло сгенерировано автоматически')
            fool_flag = True
            break
        else:
            _user_number.append(int(guess_number[i]))

    # print(_user_number)


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
        for i in range(len(_user_number)):
            if i < 3:
                print(str(_user_number[i]), end='')
            else:
                print(str(_user_number[i]))


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
    print('Быки - {}'.format(bulls))
    print('Коровы - {}'.format(cows))


def game_over():
    if bulls == 4:
        return True

# generate_number()
# x = input()
# input_user_number(x)
# # comparison()
# print(fool_flag)
