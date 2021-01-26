# =======================================================
# table 이 아닌경우 =====================================
# =======================================================
# 로봇 배제 표준 - site내에 robots.txt에 기술되어 있음.
# 저작권 정책 - site내에 설명되어져 있음.
# 무리한 네트워크에 요청하지 않기
#  - DDOS 공격으로 의심받을 수 있음.
#  - time.sleep() 사용

from io import BytesIO as bt
import re  # 정규식 사용 라이브러리
import requests as rq
import pandas as pd
import numpy as np  # 연산기능
import time
from tqdm import tqdm  # for X in tqdm(X) 기존의 in 구문 시작할때 넣으면 progress bar가 나옴.
import math  # 연산 올림 사용

dir = 'H:/Python/workplace/100.ETC/Seoul_COVID19/'

# =======================================================
# Data 수집 =====================================
# =======================================================

# first_table 구조 및 data 확인 ==============================
# first_page dataFrame으로

url_10001_ = 'https://news.seoul.go.kr/api/27/getCorona19Status/get_status_ajax.php?draw=0'
# url = f'{url}&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc'
url_10001_ = f'{url_10001_}&start=0&length=100'
# '&search%5Bvalue%5D=&search%5Bregex%5D=true&_=1611028255246'
url_10001_

r = rq.get(url_10001_)
data_json = r.json()
records_Total = data_json['recordsTotal']
end_page = math.ceil(records_Total / 100)
first_page = pd.DataFrame(data_json['data'])


def get_seoul_covid19_no_10001_(page_no):
    start_no = (page_no - 1) * 100
    url_10001_ = f'https://news.seoul.go.kr/api/27/getCorona19Status/get_status_ajax.php?draw={page_no}'
    url_10001_ = f'{url_10001_}&start={start_no}&length=100'
    r = rq.get(url_10001_)
    data_json = r.json()
    return data_json


get_seoul_covid19_no_10001_(end_page+1)
page_list_10001_ = pd.DataFrame([])
end_page

for page_no in tqdm(range(1, end_page+1)):
    page = get_seoul_covid19_no_10001_(page_no)
    page = pd.DataFrame(page['data'])
    page_list_10001_ = pd.concat([page_list_10001_, page])
    time.sleep(2)
page_list_10001_.to_csv(f'{dir}page_list_10001_.csv', encoding='euc-kr')
page_list_10001_.shape

# secod_table 구조 및 data 확인 ==============================
# first_page dataFrame으로

url_1_10000 = 'https://news.seoul.go.kr/api/27/getCorona19Status/get_status_ajax_pre.php?draw=1'
# &columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc
url_1_10000 = f'{url_1_10000}&start=0&length=100'
# &search%5Bvalue%5D=&search%5Bregex%5D=true&_=1611125332651
url_1_10000

r = rq.get(url_1_10000)
data_json = r.json()
records_Total = data_json['recordsTotal']
end_page = math.ceil(records_Total / 100)
first_page = pd.DataFrame(data_json['data'])


def get_seoul_covid19_no_1_10000(page_no):
    start_no = (page_no-1) * 100
    url_1_10000 = f'https://news.seoul.go.kr/api/27/getCorona19Status/get_status_ajax_pre.php?draw={page_no}'
    url_1_10000 = f'{url_1_10000}&start={start_no}&length=100'
    r = rq.get(url_1_10000)
    data_json = r.json()
    return data_json


get_seoul_covid19_no_1_10000(end_page+1)
page_list_1_10000 = pd.DataFrame([])
end_page

for page_no in tqdm(range(end_page+1)):
    page = get_seoul_covid19_no_1_10000(page_no)
    page = pd.DataFrame(page['data'])
    page_list_1_10000 = pd.concat([page_list_1_10000, page])
    time.sleep(2)
page_list_1_10000.to_csv(f'{dir}page_list_1_10000.csv', encoding='euc-kr')
page_list_1_10000.shape

# DataFrame 결합 ============================
Final_list = pd.concat(
    [page_list_10001_, page_list_1_10000], ignore_index=True)
# column 컬럼명 변경
# Final_list.columns = col_name.columns
Final_list.columns = ['연번', '환자', '확진일', '거주지', '여행력', '접촉력', '퇴원현황']
Final_list.to_csv(f'{dir}Final_list.csv', encoding='euc-kr')

# =======================================================
# Data 데이타 전처리 ================================
# =======================================================
df = pd.read_csv(f'{dir}Final_list.csv', encoding='euc-kr')
df.shape
df.info()
df.iloc[:10]
# ==============================================================
df['연번'].value_counts(10)


def extract_number(연번):
    if type(연번) == str:
        연번 = 연번.replace("corona19", "")
        num = re.sub("[^0-9]", "", 연번)
        # 0-9까지 숫자가 아니라면, 공란
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
    subtract_text = re.sub("[^가-힣]", "", 퇴원현황)
    # 가-힣까지 문자가 아니라면, 공란
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
# df.loc[df['퇴원현황'].str.contains('퇴원'), '퇴원현황'] = '퇴원'
# df.loc[df['퇴원현황'].str.contains('사망'), '퇴원현황'] = '사망'
# df.loc[~df['퇴원현황'].str.contains('퇴원|사망'), '퇴원현황'] = np.nan
# df['퇴원현황'].value_counts()
# ==============================================================
df.loc[0]
update_date = df.loc[0]['확진일'].replace('-', '_')
df.to_csv(f'{dir}seoul_covid19_status_{update_date}.csv', encoding='euc-kr')
