import pandas as pd
import numpy as np

#  print('%s' % )===================================================================================

import csv
from random import *
from math import *
import requests as rq
from pandas.core.series import Series
print('%s님 %s 시작을 %s' % ('김수한', '파이선', '환영합니다.'))
# 변수를 사용한 출력.=================================
interest_stocks = ["Naver", "Samsung", "SK Hynix"]
for company in interest_stocks:
    print("%s: Buy 10" % company)

# Naver: Buy 10
# Samsung: Buy 10
# SK Hynix: Buy 10


### 문자형 ###

a = '나는 소년입니다.'
print(a)
b = '파이썬학습 중입니다.'
print(b)
c = """
나는 소년이고,
파이썬학습 중입니다.
"""
print(c)
print(a, b)

greet = 'hello everyone'
type(greet)
# 길이 츨정
len(greet)  # 공란도 문자숫자로 인식

greet = ''
type(greet)
len(greet)  # 빈문자열도 가능

greet = 'hello'
greet[0]
greet[1:4]
greet[-1]  # 뒤에서 두번째

# ===================================================================================

### 숫자형 ###
a = 1  # int (정수)
b = 3.2  # float (실수)
result = a + b
print(a)

a = [0, 1, 2, 3, 4, 5]
a = list(range(0, 6, 1))
a = list(range(6))

print(a)
b = range(4)
print(b)

# ===================================================================================

### list ###

a = ['김수한', '김봉희', '김한희']
type(a)
a[0]
a[0:1]  # 마지막꺼 빼고 나온다
a[0:3]

'hello' [0:3]

a = [0, 1, 2, 3, 4, 5]
a['']
a[1:5]

# 하나의 값 추가할 때
# append는 x 그 자체를 원소로 넣고 extend는 가장 바깥쪽 iterable을 넣습니다

a.append(4)  # a 뒤에 ()안의 값을 모양 그대로 추가 appendix
print(a)

a.extend([4])  # extend는 ()안에 type이 정해 져야 한다
a.extend(4)   # TypeError: 'int' object is not iterable
a.extend('4')
print(a)

x = ['tic', 'tac']
x.append('pic')   # ['tic', 'tac', 'pic']
x.extend('pic')   # ['tic', 'tac', 'p', 'i', 'c']
print(x)


# 두개 이상의 값 추가할 때

x = [1, 2, 3]
x.append([4, 5])  # [1, 2, 3, [4, 5] ]

x = [1, 2, 3]
x.extend([4, 5])  # [1, 2, 3, 4, 5]

# ===================================================================================

### 문자열 포맷 ###

name = 'kim'
age = '50'
place_of_birth = '서울'
residence = '호주'

print('안녕하세요, 저의 이름은 ' + name + '입니다. 올해 나이는 ' + age + '살 입니다')
print('저는 ' + place_of_birth + '에서 태어났고, 현재 ' + residence + '에서 살고 있습니다.')

print('안녕하세요, 저의 이름은 {} 입니다. 올해 나이는 {}살 입니다' .format(name, age))
print('저는 {}에서 태어났고, 현재 {}에서 살고 있습니다.'.format(place_of_birth, residence))

# .format(name, age) 앞에 {}들을 채울 때 사용되는 변수들을 가져오게 하는 것.

'안녕하세요. {}님, 저는 {}입니다.'.format('a', 'b')
'안녕하세요. {}님, 저는 {}입니다.'.format('a', 'b', 'c')  # format() 에 변수가 더 많은경우는 상관없음.
# IndexError: Replacement index 1 out of range
'안녕하세요. {}님, 저는 {}입니다.'.format('a')

### 변수 생성 ###
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3
print("우리집" + animal + "의 이름은" + name + "예요")
hobby = "공놀이"
print(name, "는", age, "살이에요",)  # ,의 경우, 띄어쓰기 자동 한칸씩 적용 "
print(name+"는 어른일까요?", "->",   str(is_adult) + "입니다",)

# ===================================================================================

# .decode('utf-8') : decode는, byte로 된 내용에만 사용해야 한다.


resp = rq.get('http://www.naver.com/')
resp.decode('utf-8')  # error 발생
resp.content.decode('utf-8')  # resp.content :url site의 정보가 byte 정보로 저장
resp.content  # byte 정보는 한글등이 보여지지 않음.

s = b'test string'  # dyte형 data 생성
type(s)


# ===================================================================================

# Dictionary 생성 ### dictionary name = {'key name' : value}

g1 = {'a': 'one'}
g1
g2 = {'b': 'two',
      'c': 'three'}
g2
g2['d'] = 'four'
g2

g3 = {'a': [1, 2, 3, 4, 5]}
g3

g2.keys()
g2.values()
print('key : %s, value : %s' % ('a', g2.get('c')))
for key, value in g2.items():
    print('key : %s, value : %s' % (key, value))
g2.update({'b': 'TWO'})
g2.update({'추가키': '추가값'})
g2['b'] = 'two2'

g4 = {'01234': {'b': 'two', 'c': 'three'}}
print(g4['01234']['b'])
print(g4.get('01234').get('b'))
print(g4.keys())
print(g4['01234'].keys())

for i in g2.keys():
    print(i)

for i in g2.values():
    print(i)

for i in g2.keys:
    print(i)

for i, j in zip(g2.keys(), g2.values()):  # items()로 대체 가능.
    print(i, j)

for i, j in g2.items():
    print(i, j)

##### dataFrame df의 컬럼 column을 사용하여 dict 만들기 #######

my_stock = 'my_stock'
dir = 'C:/Users/histi/py37_32/autostock/'
df_all = pd.read_excel(
    f'{dir}files/{my_stock}.xls', sheet_name=None, dtype={'종목코드': str})
df_all.keys()
concatted_df = pd.concat(df_all)
concatted_df.columns
df = concatted_df.drop(
    ['Unnamed: 0', '매입단가', '매입수량', '메모'], axis=1).dropna(how='all', axis=0)
df = df.drop_duplicates(subset=['종목코드'], keep='first')
df = df.dropna(how='all', axis=1).reset_index()
stock_code = df['종목코드'].values
stock_n = df['종목명'].values
stock_name = []
for i in stock_n:
    stock_name.append({'종목명': i})
portfolio_stock_dict = dict(zip(stock_code, stock_name))


################################################################################
a_dict = {'023943': {'종목명': '삼광글라스', '등락율(%)': 0.0,
                     '고가대비(%)': -0.97, '보유수량': 0, '현재가': 41050,
                     '(최우선)매도호가': 41050}}

a_dict.update({'000080': {'종목명': '하이트진로', '등락율(%)': 3.1,
                          '고가대비(%)': -1.63, '보유수량': 0, '현재가': 21000,
                          '(최우선)매도호가': 21000}})

a_dict.keys()
a_dict.values()
# 1
for value in a_dict.keys():
    print(value)
    if a_dict[value]['등락율(%)'] > 3.0 and a_dict[value]['현재가'] > 10000:
        print('%s -- 매수완료 \n\t 상세데어터 : %s' %
              (a_dict[value]['종목명'], a_dict[value]))
    else:
        print('매수되지 않았습니다.')

a_dict = {'키움증권': 5000, '카카오': 3000, '네이버': 2000, '애플': 100000}
my_account = 1000000

for value in a_dict.keys():
    if value == '키움증권':
        my_account -= a_dict[value] * 5

    elif value == '카카오':
        my_account -= a_dict[value] * 2

print('남은 금액 = %s' % my_account)


a_dict = {'키움증권': 5000, '카카오': 3000, '네이버': 2000, '애플': 100000}
ee_bool = True
while ee_bool:
    a_dict['키움증권'] = a_dict['키움증권'] + 1000

    if a_dict['키움증권'] == 10000:
        a_dict.update({'키움증권': 0})
        break
print(a_dict)


# ===================================================================================

### 연산 ###

print(2**3)  # 제곱근 2^3 = 8
print(pow(2, 3))  # 2^3 = 8
print(5 % 3)  # 나머지 구하기 2
print(5//3)  # 1
print(10//3)  # 3
print(10 > 3)  # True
print(4 >= 7)  # False
number = 2+3*4
print(number)

# ===================================================================================

### 논리 ###

True + True  # True = 1
True + False  # False = 1
False + False

print(3+4 == 7)  # (같다 ==) True
print(1 != 3)  # (같지 않다 !=) True
print(not(1 != 3))  # (않다 not) False

print(not(1 != 3))  # False
print((3 > 0) & (3 > 5))  # False
print((3 > 0) or (3 > 5))  # True


### math 함수 = 연산 관련 ###

print(abs(-5))  # 절대값
print(max(5, 12))
print(min(5, 12))
print(round(3.14))  # 반올림
round(3.14, ndigits=1)

print(floor(4.99))  # 내림
print(ceil(3.14))  # 올림
print(sqrt(16))  # 제곱근

# ===================================================================================

### random 함수 - 숫자를 임의로 생성 ###

print(random())
print(int(random() * 10))
print(int(random() * 10)+1)  # 1~10까지 숫자만 출력
print(int(random() * 45)+1)  # 1~45까지 숫자만 출력
print(randrange(1, 46))  # 1~45까지 숫자만 출력
print(randint(1, 45))  # 1~45이하의 숫자만 출력
print(5 > 10)
print(not True)
print(not(5 > 10))

# ===================================================================================

### 슬라이싱 - data의 필요한 부분만 잘라서 사용###

jumin = "990120-1234567"
print("성별 : ", jumin[7])
print("연 : ", jumin[0:2])  # 0부터 2 직전까지
print("월 : ", jumin[2:4])
print("일 : ", jumin[4:6])
print("생년월일 : ", jumin[0:6])
print("생년월일 : ", jumin[:6])  # 처음부터 6 직전까지
print("뒤 7자리 :", jumin[7:14])
print("뒤 7자리 :", jumin[7:])  # 7번째부터 마지막까지
print("뒤 7자리 :", jumin[-7:])  # 뒤에서 -7번까지

# ===================================================================================

### 문자열 처리 함수 ###

a = "Python is Amazing."
print(a.lower())  # 모두 소문자로 전환
print(a.upper())  # 모두 대문자로 전환
print(a.count("n"))  # 문자n의 갯수
print(a[0].isupper())  # 첫번째나오는 것이 대문자면 True
print(len(a))  # 변수의 길이
print(a.replace("Amazing", "Easy"))  # 변수안의 글자 변환
b = a.index("n")  # 변수안에 첫번째 n이 몇번째에 존재하는가?
print(b)

### 주의 Find와 Index 비교 ###
# find에서는 있으면 0, 없으면 -1을 출력. 프로그램 진행
# index에서는 없으면 error발생 프로그램 종료

a = "Python is Amazing."
print(a.find("Python"))  # 변수안에 Python이 있는가? --> 0
print(a.find("Java"))  # 변수안에 Java가 있는가? -->  -1
print(a.index("thon"))  # 변수안에 첫번째 thon이 어디에 존재하는가? 2
print(a.index("Java"))  # 변수안에 첫번째 Java가 어디에 존재하는가? 없으면 error 프로그램 종료

# ===================================================================================

### 문자열 List 전환 - split ###
a = '나는 소년입니다. 파이썬학습 중입니다.'

b = ''' Hello world~
나는 소년이고,
파이썬학습 중입니다.
'''
a.split()
a.split(maxsplit=2)
a.split('.')
b.split()
b.split('\n')  # 행바꿈 '\n'


# Python 리스트 list 화일로 저장 csv로 저장하기
# 파이썬 모듈인 csv 모듈을 import하고 데이터는 날짜 데이터, 정수 데이터, 부동소수점 자료형 데이터가 있다고 가정했다. 엑셀로 그린다면 열 방향으로 그릴 것 같지만, 파이썬 리스트로 표현하여 행 방향으로 나열되었다.


# list 만들기
date = ['200801', '200802', '200803', '200804', '200805']
val1 = [50, 100, 300, 150, 200]
val2 = [2000.0, 2200.5, 2320.3, 2250.0, 2200.0]

# csv파일로 적기
# newline 설정을 안하면 한줄마다 공백있는 줄이 생긴다.
with open('listfile.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(date)
    writer.writerow(val1)
    writer.writerow(val2)


### 서식 formating ###############
d = '1000'
ds = format(int(d), ',')
