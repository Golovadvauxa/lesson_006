import simple_draw as sd

coord_list = []
length_list = []
factor_list = []
outside_list = []
out_of_screen = False
N = 0


def snowfall(N, color):
    global out_of_screen, outside_list

    for i in range(N):
        x, y = coord_list[i]
        if x < 0 or y <= 0:
            out_of_screen = True
            outside_list.append(i)

        point = sd.get_point(x, y)
        a, b, c = factor_list[i]
        sd.snowflake(center=point, length=length_list[i], factor_a=a, factor_b=b, factor_c=c, color=color)
        x += sd.random_number(-10, 10)
        y -= sd.random_number(0, 50)
        coord_list[i] = x, y


def create_snowflake(N):
    global coord_list, length_list, factor_list
    for i in range(N):
        fill = [sd.random_number(-100, 1000), sd.random_number(600, 900)]
        coord_list.append(fill)
        fill = sd.random_number(10, 50)
        length_list.append(fill)
        fill = [sd.random_number(40, 70) / 100, sd.random_number(30, 50) / 100, sd.random_number(30, 90)]
        factor_list.append(fill)


def delete_snowflake():
    global coord_list, outside_list, out_of_screen
    for i in outside_list:
        coord_list.remove(coord_list[i])
        fill = [sd.random_number(-100, 1000), sd.random_number(600, 900)]
        coord_list.insert(i + 1, fill)
    outside_list.clear()
    out_of_screen = False


def shift_snowfall(shift):
    global coord_list
    for i in range(len(coord_list)):
        temp0, temp1 = coord_list[i]
        temp0 += shift
        coord_list[i] = [temp0, temp1]


def out_check():
    global out_of_screen
    if out_of_screen:
        return True
