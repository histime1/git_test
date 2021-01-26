from io import BytesIO as bt
import re  # 정규식 사용 라이브러리
import requests as rq
import pandas as pd
import numpy as np  # 연산기능
import math  # 연산 올림 사용

# 정규식 (Reqular Expression) import re
# 파이썬으로 문자열 처리를 할때, 특정한 패턴을 가진 문자열을 찾거나 치환해야하는 경우가 있다.

# A~~~~~~~~~~~~~~B 에서 (~~~~~~~~~~~~)를 추출하는 방법
"A(.*?)B"

# ===================================================================================

# 라이브러리의 세부적인 내용은 위의 링크를 통해서 찾아보면 된다.
# 다양한 메타 문자가 있지만 자주 사용하는 메타 문자를 정리해보면,
# . : (dot) \n을 제외한 모든 문자 한 개와 매치
# * : 앞의 패턴이 0번 이상 반복됨을 의미
# +: 앞의 패턴이 1번 이상 반복됨을 의미
# ? : 앞의 패턴이 0번 혹은 1번 등장함을 의미 (={0,1})
# {m,n}: 앞의 패턴이 m번 이상 n번 이하 반복되는 걸 의미
# []: []안의 문자들 중 한 글자와 매칭됨, -를 통해서 범위를 나타낼 수 있음(ex> [a-zA-Z]: 모든 알파벳, [0–9]: 숫자)
# | : or 조건을 의미
# ^: 문자열의 시작을 의미
# $ : 문자열의 끝을 의미
# \d= any number (a digit)
# \D= anything but a number (a non-digit)
# \s = space (tab,space,newline etc.)
# \S= anything but a space
# \w = letters ( Match alphanumeric character, including "_")
# \W =anything but letters ( Matches a non-alphanumeric character excluding "_")
# . = anything but letters (periods)
# \b = any character except for new line
# \.  #{x} = this amount of preceding code

# re.sub('찾을문자', '바꿀문자', 대상) 문자 바꿈
# re.match()
# re.search()  #Finding Pattern in Text
# re.findall(r'찾을문자열 앞 정규문자(.*?)찾을문자열 뒤 정규문자')

s = 'python python python'
s1 = re.sub('python', 'P', s)
s1

t = '<rcp_no>AAAAAAAA</rcp_no>BBBBBBBBB</company>CCCCCCC<rcp_no>ABBBBBB</rcp_no>BCCCCCC</company>DDDDDDD'
r1 = re.findall(r'<rcp_no>(.*?)</rcp_no>', t)

num_string = "<p class='corona19_no'>7625</p>"
num_string = num_string.replace("corona19", "")
num = re.sub("[^0-9]", "", num_string)  # 0-9까지 숫자가 아니라면, 공란
num = int(num)

#####################################################################
# Data 데이타 전처리 ================================
#####################################################################
dir = 'H:/Python/workplace/100.ETC/Seoul_COVID19/'
df = pd.read_csv(f'{dir}Final_list.csv', encoding='euc-kr')
df.shape
df.info()
df.iloc[:10]
# ==============================================================
df['연번'].value_counts(10)


def extract_number(연번):
    if type(연번) == str:
        연번 = 연번.replace("corona19", "")
        num = re.sub("[^0-9]", "", 연번)  # 0-9까지 숫자가 아니라면, 공란
        num = int(num)
        return num
    else:
        return 연번


연번 = "<p class='corona19_no'>7625</p>"
extract_number(연번)

df['연번'] = df['연번'].map(extract_number)

# ==============================================================
df['퇴원현황'].value_counts()


def extract_hangeul(퇴원현황):
    subtract_text = re.sub("[^가-힣]", "", 퇴원현황)  # 가-힣까지 문자가 아니라면, 공란
    return subtract_text


퇴원현황 = "<b class=''></b>"
extract_hangeul(퇴원현황)
퇴원현황 = "<b class='status1'>퇴원</b>"
extract_hangeul(퇴원현황)
퇴원현황 = "<b class='status1'></b>"
extract_hangeul(퇴원현황)
퇴원현황 = "<b class='status2'>사망</b>"
extract_hangeul(퇴원현황)
퇴원현황 = "<b class='status2'></b>"
extract_hangeul(퇴원현황)

df['퇴원현황'] = df['퇴원현황'].map(extract_hangeul)
df['퇴원현황'].value_counts()

# str.contains 활용 ==============================================================
df.loc[df['퇴원현황'].str.contains('퇴원'), '퇴원현황'] = '퇴원'
df.loc[df['퇴원현황'].str.contains('사망'), '퇴원현황'] = '사망'
df.loc[~df['퇴원현황'].str.contains('퇴원|사망'), '퇴원현황'] = np.nan
df['퇴원현황'].value_counts()
# ==============================================================
