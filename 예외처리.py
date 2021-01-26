import pandas as pd

try:
    def ten_div(x):
        return 10/x

    ten_div(2)

except:
    pass


# Pass 처리

def calc(values):
    sum = None

    try:
        sum = values[0] + values[1] + values[2]
    except (IndexError, ValueError):
        # pass
        print('오류발생')
    print(sum)


values = ['s']
calc(values)

# error 발생 회피 , for문 등에서 error 발생후에도 계속 돌도록 만듬
#############################################################
df = pd.read_csv(f'{dir}krx_corp_list.csv', encoding='euc-kr')
#############################################################


def corp_code_by_corp_name(corp_name):
    corp_code_list = df.loc[df['Name'] == corp_name, 'Symbol'].tolist()
    if len(corp_code_list) > 0:
        corp_code = corp_code_list[0]
        return corp_code
    else:
        return False


corp_code_by_corp_name('빅 히트')


def farmer_johns():

    r = int(input('Enter the radius of the circle in feet:'))
    # check for valid input
    try:
        while input >= 0:
            # area of brown
            # area of square - area of circle
            import math

            pi = math.pi
            area_square = (r+r)**2
            area_circle = pi * r**2

            area_brown = area_square - area_circle
            print(
                'The area of the brown shaded region is {:.2f} feet^2.'.format(area_brown))

            # turtle graphics set up
            import turtle
            wn = turtle.Screen()
            a = turtle.Turtle()
            a.pensize(5)

            # draw circles
            a.pencolor('green')

            a.penup()
            a.goto(r, r)
            a.pendown()
            a.circle(r)

            a.penup()
            a.goto(r, -r)
            a.pendown()
            a.circle(r)

            a.penup()
            a.goto(-r, -r)
            a.pendown()
            a.circle(r)

            a.penup()
            a.goto(-r, r)
            a.pendown()
            a.circle(r)

            # square
            a.pencolor('blue')

            a.penup()
            a.goto(r, r+r)
            a.pendown()
            a.goto(-r, r+r)
            a.goto(-r, -r+r)
            a.goto(r, -r+r)
            a.goto(r, r+r)

            # middle region
            a.pencolor('#654321')
            a.fillcolor('#b5651d')
            a.begin_fill()

            a.penup()
            a.goto(r, r)
            a.pendown()
            a.circle(r, -90)

            a.penup()
            a.goto(0, r+r)
            a.right(180)
            a.pendown()
            a.circle(r, -90)

            a.penup()
            a.goto(-r, r)
            a.left(-180)
            a.pendown()
            a.circle(r, -90)

            a.penup()
            a.goto(0, 0)
            a.left(180)
            a.pendown()
            a.circle(r, -90)

            a.end_fill()

            # writing

            # a.write('The area of the brown shaded region is {:.2f} feet^2.'.format(area_brown))

    except ValueError:
        print('invaild input')
    except TypeError:
        print('invaild input')
