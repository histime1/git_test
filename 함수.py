# Function ======================================================================

# def 함수 정의 1. return값이 있는 함수/없는 함수 ====================================

def add(a, b):  # add는 2개의 변수로 되어져 있다.
    return a + b  # add 함수 결과는 a + b로 되어져 나온다.


add(1, 2)

# Warnning ## 보여주는 결과는 같으나 return값이 없는 경우, 변수값으로 사용 불가.

# ex) print 값의 경우 변수로 사용불가.

c1 = add(1, 2)  # c1에 return값이 적용되어져 있다.
c2 = print(add(1, 2))  # c2에 return값이 적용되어져 있지 않고, 단순히 결과만 print되고 종료된다.
c1  # 결과값 3
c2  # 결과값 없음.즉 c2에 return값이 없다.

# def 함수 정의 2_1 - 함수 안에 정의된 변수는 return값을 가지지 않는다.


def add_multiply(a, b):  # a, b 변수가 정의되어져 있지 않다
    c = (a + b) * 2     # c 변수가 정의되어져 있지 않다
    return c


add_multiply(4, 8)

# def 함수 정의 2_2 - 함수 밖의 변수는 함수 안에 정의된 변수로 변하지 않는다.
# def 안에 정의된 변수는 def를 실행하는 범위에서만 활용된다.
a = 10
b = 20
c = 30


def add_multiply(a, b):
    c = (a + b) * 2
    return c


add_multiply(4, 8)
a
b
c

# def 함수 정의 2_3 - 함수 안에 변수 정의값이 부족할 경우, 함수 밖에서 변수값을 찾게 된다.


def add_multiply(a, b):
    c = (a + b) * x
    return c


x = 5
add_multiply(4, 8)  # a=4, b=8,  변수 x 가 없음, def 밖의 x=5를 가져옴.

# 구구단 정의 활용.


def gugudan_print(x):
    print(x,  'X 1 =', x * 1)
    print(x,  'X 2 =', x * 2)
    print(x,  'X 3 =', x * 3)
    print(x,  'X 4 =', x * 4)
    print(x,  'X 6 =', x * 5)
    print(x,  'X 5 =', x * 6)
    print(x,  'X 7 =', x * 7)
    print(x,  'X 8 =', x * 8)
    print(x,  'X 9 =', x * 9)
    print()


gugudan_print(5)

for i in range(1, 10):
    for j in range(1, 10):
        print(i, "X", j, '=', i*j)
        if(j == 9):  # X9하고 나서 한칸씩 띄도록 조건 지정
            print()

for i in range(1, 10):
    gugudan_print(i)


def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment
    return upper_price


cal_upper(100)


def cal_upper_lower(price):
    offset = price * 0.3
    upper = price + offset
    lower = price - offset
    return (upper, lower)


cal_upper_lower(10000)
