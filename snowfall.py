import simple_draw as sd

coord_list = []
length_list = []
factor_list = []
outside_list = []
out_of_screen = False
N=0


def snowfall(N,color):
    global out_of_screen,outside_list
    sd.clear_screen()
    for i in range(N):
        x, y = coord_list[i]
        if x < 0 or y <= 0:


        point = sd.get_point(x, y)
        a, b, c = factor_list[i]
        sd.snowflake(center=point, length=length_list[i], factor_a=a, factor_b=b, factor_c=c, color=color)
        x += sd.random_number(-10, 10)
        y -= sd.random_number(0, 50)
        coord_list[i] = x, y


def create_snowflake(N):
    global coord_list, length_list, factor_list
    for i in range(N):
        fill = [sd.random_number(0, 1200), sd.random_number(600, 900)]
        coord_list.append(fill)
        fill = sd.random_number(10, 50)
        length_list.append(fill)
        fill = [sd.random_number(40, 70) / 100, sd.random_number(30, 50) / 100, sd.random_number(30, 90)]
        factor_list.append(fill)

def delete_snowflake():
