# Pandas 기초

import datetime
from io import BytesIO as bt
from re import A
from typing import ValuesView
from zipfile import ZIP_FILECOUNT_LIMIT
from numpy.core.fromnumeric import shape, std, var
from numpy.lib.function_base import median, quantile
from pandas._libs.missing import NA
from pandas.core.frame import DataFrame
from pandas.core.tools.datetimes import to_datetime
import requests as rq
import pandas as pd
import numpy as np
import re  # 정규식 사용 라이브러리
import os  # 화일 복사 탐색 불러오기 등의 operation library
import xml.etree.ElementTree as ET  # xml을 불러오는 라이브러리
import FinanceDataReader as fdr  # 주식 정보를 불러오는 라이브러리
import time  # roof 돌때 time.sleep(4) 4초 sleeping
import matplotlib.pyplot as plt  # statistical data visualization 시각화
import seaborn as sns  # statistical data visualization 시각화
# %matplotlib inline

# 한글 폰트 깨짐 방지

Han_font = 'Malgun Gothic'

plt.rc('font', family=Han_font)  # 한글폰트 해결.
plt.rc('axes', unicode_minus=False)  # 축에 - 값 적용
# plt.style.use('ggplot')  # 원하는 표의 style을 지정.

# ()가 붙고 안붙는 경우의 차이점.
# attribute : .sharp, .index, .column, .value 등
# function : .describe(), .head().... ()안에 option을 쓸 수 있다.

# 1_1. data set Creation (객체 생성)

# 1_1_1. Series creation (Series는 list 형식, 컬럼라인 하나)
# index - value

s = pd.Series(['1', '2', '3'])
s  # dtype: object
s1 = pd.Series([1, 2, 3])
s1  # dtype: int64
s2 = pd.Series(['1', '2', '3'], index=['A', 'B', 'C'])  # index 지정
s2
s3 = pd.Series(['1', '2', '3'], index=['A', 'B', 'C'],
               name='출석부')  # index 지정, Series name지정
s3

dic1 = {'name': 'A', 'age': 40, 'gender': 'mail',
        'job': 'analist'}  # dictionaly 사용 { : }
dic1
s4 = pd.Series(dic1)
s4

s1.sum()
s1.mean()

# 1_1_2. Dataframe creation (data table형식)
# index - column명 - value

# list 형식으로 생성시 가로로 data가 들어간다.
df = pd.DataFrame([
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]],
    index=[1, 2, 3]
)
df

# dictionary 형식으로 생성시 column명을 포함해서 세로로 data가 들어간다.
df = pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
    index=[1, 2, 3]
)
df

# list 형식으로 입력후, index. column명을 정의.
df = pd.DataFrame(
    [[4, 7, 10],
     [5, 8, 11],
     [6, 9, 12]],
    index=[1, 2, 3],
    columns=['a', 'b', 'c']
)
df

# Multiple index (2개 이상의 index를 사용)
df = pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
    index=pd.MultiIndex.from_tuples(
        [('d', 1), ('d', 2), ('e', 2)],
        names=['n', 'v'])
)
df


### Data의 모양확인 ###

df.shape
df.info

# ============================================================================================

# 2_1_1. 컬럼(Series)추출 -  column 명이 없음.

# 하나의 컬럼에 해당하는 data를 추출할 때 사용

df = pd.DataFrame(
    [[4, 7, 10],
     [5, 8, 11],
     [6, 9, 12]],
    index=[1, 2, 3],
    columns=['a', 'b', 'c']
)
df

s = df['a']  # Series 형식으로 추출
s

s[1]  # s에 있는 index 1의 value출력
s[2]  # s에 있는 index 2의 value출력
s[0:]  # : 사용시 original index 0 부터 계산 됨 주의 필요
s[1:2]  # : 사용시 original index 0 부터 계산 됨 주의 필요 index 1부터 2앞. 즉 index 1 값 출력
s[1:3]  # : 사용시 original index 0 부터 계산 됨 주의 필요 index 1부터 3앞. 즉 index 1~2 값 출력
s[:2]  # : 사용시 original index 0 부터 계산 됨 주의 필요 index 2의 앞까지. 즉 index 0~1 값 출력

s = df['a']
s == 5  # 특정 value 가 있는 행을 True 나머지는 False로 추출
s[s == 5]  # 특정 value 가 있는 행만 index 포함 추출

# (주의) Multiple index에서는 index 행은 0부터 인식하게 된다.
df = pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
    index=pd.MultiIndex.from_tuples(
        [('d', 1), ('d', 2), ('e', 2)],
        names=['n', 'v'])
)
df

s = df['a']  # Series 형식으로 추출 - multi index가 적용
s

s[1]  # s에 있는 index 1의 value출력
s[2]  # s에 있는 index 2의 value출력
s[0:]  # index 0 부터 계산 됨 주의 필요
s[1:2]  # index 1부터 2앞. 즉 index 1 값 출력
s[1:3]  # index 1부터 3앞. 즉 index 1~2 값 출력
s[:2]  # index 2의 앞까지. 즉 index 0~1 값 출력

s = df['a']
s == 5  # 특정 value 가 있는 행을 True로 추출
s[s == 5]  # 특정 value 가 있는 index 포함 추출

# 2_1_2. 컬럼을 data frame 형식으로 추출 -  column 명이 존재
# 2개 이상의 Column data는 [[]]를 사용하여 data frame으로만 추출 가능

df = df[['a']]  # [] 컬럼 하나의 경우는 series로 추출 차이는 컬럼명이 있고 없고의 차이.
df

df = df[["a", "b"]]  # [] 컬럼이 둘이상 경우는 data frame으로 추출
df

df == 5
df[df == 5]

# ==================================================================================

# 2_2. 행 / 열 출력

# ==================================================================================
# single index에서 작동 - multiple에서 작동하지 않음.

df.loc[1]
df.loc[1:2]
# 컬럼(Series) and 행 지정 추출
df = df.loc[1, "a"]
df

# ==================================================================================
# 2_4. 특정 value 컬럼(Series) and 행 지정 추출

# .loc [행, 열]
dt = df.loc[1, "a"]
df.loc[[0, 1], "a"]
df.loc[[1, 2], ["a", "b"]]

# Bool 에서는
# and => &
# or => |

# df = fdr.StockListing('KRX')  # 코스피, 코스닥, 코넥스 전체

# (df['Region'] == '서울특별시') & (df['Market'] == 'KOSPI')
# df[(df['Region'] == '서울특별시') & (df['Market'] == 'KOSPI')]

# df.loc[((df['Region'] == '서울특별시') & (df['Market'] == 'KOSPI')), ['Symbol', 'Name']]
# df.loc[(df['Region'] == '서울특별시') & ((df['Market'] == 'KOSPI')
#                                     | (df['Market'] == 'KOSDAQ')), ['Symbol', 'Name']]
# df.loc[((df['Region'] == '서울특별시') & (df['Market'] == 'KOSPI')
#         | (df['Market'] == 'KOSDAQ')), ['Symbol', 'Name']]

# Pandas 연산자 - single/multiple index에서 같이 작동

df = pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
    index=pd.MultiIndex.from_tuples(
        [('d', 1), ('d', 2), ('e', 2)],
        names=['n', 'v'])
)
df

df[df.a < 6]
df[df['a'] < 6]
df["b"] != 7
df[df["b"] != 7]

df.a.isin([5])  # df.column명.isin(values)  # 특정 column에 특정value가 들어 있는 값 가져오기
# df['column명'].isin(values)  # 한글/숫자등 특정 column에 특정value가 들어 있는 값 가져오기
df['a'].isin([5])

# NaN null 처리 =============================================================
# df['컬럼명'].isnull() / notnull() / ~ df['컬럼명'].notnull() 특정 컬럼에 na가 있는지를 bool 값으로 반환
# df['컬럼명'].isna()의 경우, 특정 컬럼에 na가 있는지를 bool 값으로 반환
# df['컬럼명'].dropna()의 경우, 특정 컬럼에서 na를 제외한 값을 컬럼의 list형태로 반환

df_krx = fdr.StockListing('KRX')

krx_list = df_krx[['Market', 'Sector', 'Symbol', 'Name']]
ex_list = krx_list[(krx_list['Name'].str.contains('콜' or '풋'))]  # 콜, 풋 제외

ex_list[~ex_list['Sector'].notnull()]  # 콜, 풋 종목은 Sector가 NaN임
ex_list[ex_list['Sector'].isna()]  # 콜, 풋 종목은 Sector가 NaN임
ex_list['Sector'].dropna()  # Sector가 NaN인 값을 제외한 Sector list

ex_list = ex_list[~ex_list['Sector'].notnull()]
krx_ex_list = df_krx[~df_krx.Symbol.isin(ex_list.Symbol)]  # 콜, 풋 제외

df.isnull().sum()   # df에 컬럼별로 null 값의 갯수
pd.isnull(df).sum()  # 상동
df.a.isnull().sum()  # df의 컬럼a에 null 값의 갯수
df['a'].isnull().sum()  # 상동

df.notnull().sum()   # df에 컬럼별로 null 아닌 값의 갯수
pd.notnull(df).sum()  # 상동
df.a.notnull().sum()   # df의 컬럼a에 null이 아닌 값의 갯수
df['a'].notnull().sum()  # 상동

~ df.notnull()

pd.isna(df).sum()  # df에 컬럼별로 na 값의 갯수
df['a'].isna().sum()  # df의 컬럼a에 na 값의 갯수

# 특정 column 컬럼의 값 조건으로 추출
df_krx = fdr.StockListing('KRX')  # 코스피, 코스닥, 코넥스 전체
df_krx = df_krx[(df_krx['Region'] == '서울특별시') & (df['Market'] == 'KOSPI')]
df_krx_v1 = df[(df_krx['Sector'] == '보험업') | (df['Symbol'] == '294870')]

# 특정 column 컬럼에 특정문자를 포함한 값 찾기
df[df['Name'].str.contains('디피')]
df[df['Name'] == '빅히트']  # 문자를 정확히 알때.

### 특정 column에 특정값 특정문자가 있는 행의 다른 column 컬럼값 반환###
df[df['Name'] == '빅히트']['Symbol'].values  # 자세한 정보
df[df['Name'] == '빅히트']['Symbol'].tolist()  # list 형식으로
df.loc[df['Name'] == '빅히트']['Symbol'].tolist()[0]  # 값으로
df.loc[df['Name'] == '빅히트', 'Symbol'].tolist()[0]  # 값으로

# index 변경
df.set_index('Symbol', inplace=True)

# index reset
df.reset_index()

# 정렬
df.sort_values(by=['core_code', 'Period'])

# 논리 연산자 사용 ===============================================================

# Pandas 연산자 &,  |,  ~,  ^, df.any(), df.all()

df[(df == 5) | (df == 7)]
df[df[(df.a == 5) & (df.b == 7)]]

# Python 연산자 and, or, not, xor, any, all
1 and 2

True and True
True and False
False and True
False and False

[df.a == 5] and [df.b == 7]
df[(df.a == 5) and (df.b == 7)]  # Value값을 and 하므로 error
[df.a == 5] & [df.b == 7]  # 논리값들을 & 하므로 error

# ================================================================================

# unique 만 남김 -> Duplicates 중복제거
# subset을 통해 unique해당 항목을 선택, keep을 통해 first만 살릴지, last만 살릴지 결정.
df = pd.DataFrame(
    {"a": [4, 5, 6, 6],
     "b": [7, 8, 9, 9],
     "c": [10, 11, 12, 13]},
    index=pd.MultiIndex.from_tuples(
        [('d', 1), ('d', 2), ('e', 2), ('e', 3)],
        names=['n', 'v'])
)
df

df1 = df.drop_duplicates(subset=['a', 'b'], keep='last')
df1
df2 = df.drop_duplicates(subset=['a', 'b'], keep='first')
df2

# Summarize Data ================================================================

df = sns.load_dataset('iris')

df.shape  # df의 모양 (행, 열)
df.shape[0]  # df의 행의 갯수
len(df)  # df의 행의 갯수

df.shape[0]
df.shape[1]  # df의 열의 갯수
df.head()  # 컬럼 및 전체 모양

# df['w'].value_counts() --> column안에 unique한 값들의 갯수,
df['species'].value_counts()
df['species'].value_counts(normalize=True) * 100  # 100분율로 계산


# df['w'].nunique() --> # of distinct values in a column. 열에 있는 고유값의 갯수.
df['species'].nunique()

# 특정 column 컬럼의 uniq한 object를 추출. dataframe으로 저장
uq_sp = pd.DataFrame(df['species'].value_counts())
uq_sp

# column 컬럼 순서 변경==========================================================
df.columns
cols = ['corp_code', 'corp_name', '날짜', '종가', '전일비', '시가', '고가', '저가', '거래량']
df = df[cols].copy()

# 기초 통계 값 확인.==============================================================================

# df.describe() --> Basic descriptive statistics for each column (or GroupBy)

df.describe()   # 수치형 value data에 대한 통계값을 보여줌
df.describe(include='all')  # 모든 dataframe을 보여줌 Na 나옴.
df.describe(include=[np.number])  # 숫자형 dataframe만 출력
df.describe(include=[np.object])  # Object형 dataframe만 출력
df.describe(include=[np.category])  # category만 출력. Na 있는 경우, error.
df.describe(exclude=[np.number])  # 숫자형을 제외한 dataframe만 출력

# df.summarize 함수() =====================================

df.sum()
df.count()
df.min()
df.max()
df.median()
df.var()
df.std()
df.quantile([0.25, 0.75])

# df.summarize 함수 argument  =====================================

df.sum()  # 기본은 sum over the row axis (세로)
df.sum(axis=0, skipna=True)  # axis = 0 sum over the row axis (세로)
df.sum(axis=1, skipna=True)  # axis = 1 sum over the column axis (가로)

# df.['컬럼명'].summarize 함수() ========================

df['petal_width'].sum()
df['petal_width'].count()
df['petal_width'].min()
df['petal_width'].max()
df['petal_width'].median()
df['petal_width'].var()
df['petal_width'].std()
df['petal_width'].quantile([0.25, 0.75])

# (lambda 인자들 : 표현식)(인자 값들) 으로 구성
# 함수 안에 사용해서 손쉽게 계산식을 적용할 수 있도로 하는 역할
(lambda x, y: x * y)(1, 5)
(lambda x: x * 5)(3)

# apply (function 생성)  데이터 전처리시 많이 사용==================================
# index 값에 해당행 전체의 column과 value를 가져옴.
# 새로운 column 컬럼을 생성/만들고 기존 column 컬럼의 data 값을 가져와서 사용.
# argument로 , axis=1 # 각 row별 ,axis=0 # 각column별로 작동
df = sns.load_dataset('iris')

df.apply(lambda x: x[1])  # 1번째
df.loc[1]
df.apply(lambda x: x[2])  # 2번째
df.loc[2]
df['species'].apply(lambda x: x[0:])  # column 컬럼의 0번째 값만
df['species'].apply(lambda x: x[:3])  # column 컬럼의 뒤에서3번째 값만
# df에 새로운 column 컬럼을 만들어서 apply를 통해 수정한 data 값을 추가한다.
df['species_New'] = df['species'].apply(lambda x: x[:3])
df

# df에 새로운 column 컬럼을 만들어 주는 함수를 만들어서 apply에 포함하여추가

# apply 사용==================================


def smp(x):
    x = x[:3]  # 뒤에서 3번째까지 문자를 가져오는 함수
    return x


df['species_New_with def smp'] = df['species'].apply(smp)
df
# map 사용==================================
# 반드시 Series 형식에서 사용
# index의 값에 해당하는 value 값을 호출.

df['species_New_with def smp'] = df['species'].map(smp)
df

# apply 사용==================================
# df1의 2개 column을 기준으로 data 추출할 때.
df['C'] = df.apply(lambda x: df1(x['A'], x['B'])[3], axis=1)

# 새로운 column 컬럼 생성 ==================================
# df.assign(new column명 = column 정의 or 함수, 수식) :
# df명['new column명'] =

df = pd.DataFrame({'A': range(1, 11), 'B': np.random.randn(10)})
df

df2 = df.assign(C=' ')
df2
df3 = df2.assign(D=lambda df: df2.A * df2.B)
df3
df3['E'] = df3.A * df3.B
df3
df3['F'] = ''
df3
df3['F'] = df3.A ** df3.B
df3
df3.F = df2.A  # 생성된 컬럼 data 변경.
df3

# list 내부 값 추가
# ex_list.append['추가값']
# list 내부 값 삭제
# del ex_list[-1]

# dic 내부 값 추가
# dic_name['key값'] = value값
# dic_name.update({'key값':'value값'})
# dic_name.update({'newkey값':'value값'})
# dic 내부 값 삭제
# del dic_name['key값']

# 변수를 사용한 출력.=================================
interest_stocks = ["Naver", "Samsung", "SK Hynix"]
for company in interest_stocks:
    print("%s: Buy 10" % company)
# Naver: Buy 10
# Samsung: Buy 10
# SK Hynix: Buy 10

# 컬럼명 column명만 삭제 = 특정열만 추출 =================
df = df.drop(['삭제할 컬럼명1', '삭제할 컬럼명2'], axis=1)
df = df.drop(['삭제할 컬럼명1', '삭제할 컬럼명2'], axis='columns')
df = df.data.loc[:, ['남길 컬럼명1', '남길 컬럼명2']]

# NA값을 가진 행/열 삭제 =================
df = df.dropna(how='all', axis=0)  # how = 'any' 하나라도 있으면 제거
df = df.drop(['시장구분', '업종'], axis=1).dropna(how='all', axis=0)
# axis = 0 row 행기준 =================
# axis = 1 column 열기준 =================


# 컬럼명 column명 변경 ==================================
# 컬럼 column 1:1 매칭하여 변경
df = df.rename({'one': 'New_one', 'two': 'New_two'}, axis='columns')

# 컬럼 column 덮어쓰기
df.columns = ['New_one', 'New_two']

# 컬럼 column 기존 문자 대체
df.columns = df.columns.str.replace('_', '+')

# 컬럼 column 특수 문자 추가하기
df.add_preffix('@_')
df.add_suffix('_%')

# 숫자형 data를 구분하여 category 화 시키는 함수 ==================================
pd.qcut(range(5), 5)
pd.qcut(range(5), 3, labels=['good', 'medium', 'bad'])
pd.qcut(df3.A, 3, labels=['good', 'medium', 'bad'])

df3.max(axis=0)  # 행을 기준으로 최대값
df3.max(axis=1)  # 컬럼을 기준으로 최대값
df3.min(axis=0)  # 행을 기준으로 최대값
df3.min(axis=1)  # 컬럼을 기준으로 최대값

df3['A'].clip(lower=-1, upper=5)  # A컬럼의 low와 up 값을 제한하여 변형.
df3['B']
df3['B'].abs()  # B컬럼의 - 값을 절대값으로 변경.


# 특정 column 컬럼의 특정값이 들어간 row를 제거, 삭제하기 ==============
ex_corp = [3, 4, 5]
df4 = df3[~df3['F'].isin(ex_corp)]

s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

np.random.seed(0)
dates = pd.date_range('2000-01-01', '2009-12-31', freq='D')
# dates = pd.date_range('2000-01-01', '2009-12-31', freq='3D') 3일간격
data = np.random.rand(len(dates))
series = pd.Series(data, dates)

# value 조건 value in series > 0.8
series = series[series > 0.8]

# row 조건 start at 2001-01-01, 3 month 간격
date_rng = pd.date_range('2001-01-01', periods=50, freq='3MS')

# row 조건 몇행~몇행까지
labels = date_rng[0:]
# use pd.cut to cut ts index into chunks
grouped = series.groupby(
    pd.cut(series.index, bins=date_rng, labels=labels, right=False))

start_date = grouped.head(1).index

dates = pd.date_range('20180101', periods=6, freq='3MS')
dates


df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df

# Change column Type

# ================================================================================

# to_numeric() is a Series or a single column of a DataFrame.

s = pd.Series(['8', 6, '7.5', 3, '0.9', ''])  # mixed string and numeric values
s
pd.to_numeric(s)

# Rather than fail, we might want 'pandas' to be considered a missing/bad numeric value.
# We can coerce invalid values to NaN as follows using the errors keyword argument:
pd.to_numeric(s, errors='coerce')

# to ignore the operation if an invalid value is encountered:
pd.to_numeric(s, errors='ignore')

df["a"] = pd.to_numeric(df["a"], errors='coerce')

# convert type all columns of DataFrame.
df = df.apply(pd.to_numeric)
df = df.apply(pd.to_datetime)

# object 타입을 datetime타입으로 바꾼다
df['a'] = pd.to_datetime(df['a'], format='%Y-%m-%d %H:%M:%S', errors='raise')

# convert just columns "a" and "b"
df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric, errors='coerce')
df[["a", "b"]] = df[["a", "b"]].apply(pd.to_datetime, errors='coerce')
df["c"] = pd.to_numeric(df["c"])

# data type 변경 ===============================
# data의 min/max 등 표현가능한 범위 확인후 변경 ===================
for dtype in ['int8', 'int16', 'int32', 'int64']:
    print(np.iinfo(dtype))

for dtype in ['uint8', 'uint16', 'uint32', 'uint64']:
    print(np.iinfo(dtype))

for dtype in ['float16', 'float32', 'float64']:
    print(np.finfo(dtype))

# astype() 사용  ===============================
df.dtypes

num = 10000000
df = pd.DataFrame(
    {'C1': pd.Series([1.0]*num, dtype='float'),
     'C2': pd.Series([1]*num, dtype='int'),
     'C3': pd.Series(['AAAAAAAAAA']*num, dtype='object')})

df.info(memory_usage='deep')

# float64 -> float32
df.loc[:, ['C1']] = df.loc[:, ['C1']].astype('float32')
df.loc[:, ['C1']].info(memory_usage='deep')
# int64 -> int16
df.loc[:, ['C2']] = df.loc[:, ['C2']].astype('int16')
df.loc[:, ['C2']].info(memory_usage='deep')
# object -> category
df.loc[:, ['C3']] = df.loc[:, ['C3']].astype('category')
df.loc[:, ['C3']].info(memory_usage='deep')

# convert columns to complex type
df = df.astype({'날짜': 'datetime64[D]', '종가': 'float16', '전일비': 'float16', '시가': 'float16', '고가': 'float16',
                '저가': 'float16', '거래량': 'float32', 'corp_code': 'category', 'corp_name': 'category', })
df.info(memory_usage='deep')

# convert all DataFrame columns to the int64 dtype
df1 = df.astype(int)
df1.dtypes

# convert column "a" to int64 dtype and "b" to complex type
df1 = df.astype({"a": int, "b": complex})
df1.dtypes

# convert Series to float16 type
s = df['a']
s.dtypes
s = s.astype(np.float16)
s.dtypes

# convert Series to Python strings
s = s.astype(str)
s.dtypes

# convert Series to categorical type - see docs for more details
s = s.astype('category')
s.dtypes

# 오늘 현재 날짜 시간을 입력
today = datetime.datetime.today()
today = today.strftime('%Y-%m-%d')


# 년월일을 월일만 추출.
# 슬리이싱 이용한 data 전처리 # datetime 형식을 쪼갤 수 없음.
# datetime을 astype(str)으로 object type으로 전환후 쪼개기
df = pd.DataFrame({'date': ['2021-01-15']})
df['mm-dd'] = df['date'].astype(str).map(lambda x: x[-5:])
df


# =============================================================================

# Directory 확인 및 변경

os.getcwd()
os.listdir()
os.chdir('H:/Python/workplace/공시기업 corpCode/')  # working directory 변경
os.chdir('H:/Python/workplace')

# Directory 생성 mkdir('a') / 변경 rename('a', 'b') / 삭제 rmdir('a')
os.mkdir('Christmas Photos')
os.rename('Christmas Photos', 'TEST')
os.rmdir('TEST')

# 파일 불러오기

todo = open('A.txt', 'w')  # To write
# To read and write in binary mode
todo = open('A.txt', mode='r+b', encoding='utf-8')

with open('A.txt') as A:
    A.read()

# pocket.csv 예제 -> period, rcp_no, dcm_no의 컬럼으로 구성
# 판다스로 불러올 경우, 제일앞에 index 값이 생김.
#    period          rcp_no   dcm_no
# 0   19.09  20191114001273  6958001
# 1   19.06  20190814002218  6846651
# 2   19.03  20190515001605  6738798
# 3   18.12  20190401004781  6616741
# 4   18.09  20181114001530  6382016
# 5   18.06  20180814001113  6282263

df['period']  # index 포함해서 불러옴.
df['period'].values  # 행의 value만 불러올 경우, type이 array로 변경됨

period = df['period'].values
rcp_no = df['rcp_no'].values
dcm_no = df['dcm_no'].values

# Directory 주소 변경 방법
# import os 사용
# os.chdir("F:/AMD_HDD용/1.주식/1.파이썬을 활용한 DART 재무제표 데이터 수집과 분석/")
# df = pd.read_csv('pocket.csv')

# pd.read_csv('pocket.csv')
#                  #, sheet_name = "연결 재무상태표"
#                  #, header = 5
#                  #, skiprows = 5 # header 대신 사용
#                  #, names = ['1st column 명' ,'2nd column 명']
#                  #, dtype = {'1st column 명' : str, '2nd column 명' : np, int64, '3rd column 명' : float }
#                  # 문자열(string), 정수형(integer), 부동소수형(float)
#                  #, index_col = 'id'
#                  #, na_values= 'NaN'
#                  #, thousands=','
#                  #, nrows = 10) #10번째행까지만 잘라서 출력


# df.to_csv("연결재무상태표.csv", encoding="euc-kr")
# df.to_excel("연결재무상태표.xlsx", encoding="UTF-8") #excel 출력시 확장자, xls (97-2003), xlsx 구분


# =============================================================================
# 특정 조건에 대한 좌표 설정 '특정 문자열 찾기'

df_boolean = df == '특정문자열'  # df_boolean -> True False를 구분

# data 최소값, 최대값 위치 확인
num_list = list(np.random.randn(10))
num_list = list(range(10))
# random.shuffle(num_list)
np.argmax(num_list)
np.argmin(num_list)

# data 최소값, 최대값 위치 확인 활용 numpy의 argmax, argmin 활용.

df = pd.DataFrame(
    {'A': range(1, 6), 'B': np.random.randn(5), 'c': ['단가', 2, 3, 4, 5]})
df
df == '단가'  # df == '단가' 인 항목에 대해서만 True로 표시
df_boolean = (df == '단가' or df == '2')  # '단가' 문자가 있는 x열 찾아서 1을 표시

# '단가' 문자가 있는 y열 찾아서 1을 표시하고, 위치를 확인
y = df_boolean.sum(axis=0, skipna=True).values.argmax()
# '단가' 문자가 있는 x열 찾아서 1을 표시하고, 위치를 확인
x = df_boolean.sum(axis=1, skipna=True).values.argmax()
x, y

df.iloc[x+1, y]  # iloc 을 사용하여 x,y 좌표의 값을 찾는다.(if,x행 단가값 아래행이 단가value일 경우)

# pandas 문자열 관련 함수 str =========================================

df = pd.read_csv('H:/Python/workplace/TEMP/법정동Sample.csv', encoding='euc-kr')

# 특정문자 . 공백을 새로운 문자로 대체
df['법정동명'].str.replace(" ", "_").head()

# 대소문자 변경
df2['col1'].str.upper()      # 모두 대문자로 변경
df2['col1'].str.lower()      # 모두 소문자로 변경

# 앞 5자리까지만 추출
df['법정동명'].str[:5].head()

# 마지막 한글자만 추출
df['법정동명'].str[-1].head()

# 공백제거 strip()
test1 = df['법정동명'].str.strip()

# 공백(" ")으로 분리
df['법정동명'].str.split(" ").head()
# 분할된 개별 리스트를 데이터 프레임으로 만드려면, expand=True옵션을 추가한다.
df['법정동명'].str.split(" ", expand=True).head()

# 특정문자로 시작하는 데이터 행만 필터링
df[df['법정동명'].str.startswith("서울")].head()

# 특정문자로 끝나는 데이터 행만 필터링
df[df['법정동명'].str.endswith("동")].head()

# 특정문자가 포함된 데이터 행만 필터링
df[df['법정동명'].str.contains("강서구")].head()

# 찾은 모든 값 반환(정규식)
df['법정동명'].str.findall('\w+동').head()

# 시작글자 인식 .str.startswith()
# 특정 boolean 반환, True, False 반환
df['법정동명'].str.startswith("서울").head()

# 원하는 문자열만 추출
# 그룹 ()을 꼭 지정 패턴을 입력, 맞는 단어가 없을 시 NaN이 출력된다.
# 추출그룹이 많을 땐 자동으로 데이터프레임 처리
df['법정동명'].str.extract('( \w*시 )|( \w*군 )|( \w*구 )')

# appendix 비교
# file을 불러와서 dataFrame 만들어서 결합, 합치는 방법 ================================

dir = 'H:/Python/workplace/3.주식관련/투자자별매매동향/'

df = pd.DataFrame(columns=['외인', '기관', '개인'])

for file in os.listdir(dir):
    print(file)
    df_new = pd.read_csv('{}{}'.format(dir, file), encoding='euc-kr')
    df = pd.concat([df, df_new])


# update date 자동으로 화일명에 추가하는 방법 ============================
df.loc[0]
update_date = df.loc[0]['확진일'].replace('-', '_')
df.to_csv(f'{dir}seoul_covid19_status_{update_date}.csv', encoding='euc-kr')

# Pandas 사용 CSV 파일에서 불러오기  ================================================================
# 00*** 로 되어진 object type을 불러오면 int float로 인식되는 경우, dtype = {'컬럼명' : np.object} 를 넣어준다.
dir = 'H:/Python/workplace/'
filename = 'pocket'
df = pd.read_csv(f'{dir}{filename}.csv', dtype={
                 'corp_code': np.object}, encoding='euc-kr')

df = pd.read_csv(f'{dir}{filename}.csv', converters=dict(
    corp_code=str), encoding='euc-kr')
df = pd.read_csv()


df = pd.read_excel(f'{dir}{filename}.xlsx', dtype={'corp_code': str})

# 숫자형 object type의 경우 csv로 저장시 numeric으로 인식, excel 사용권고
df_krx.to_excel('{}krx.xlsx'.format(dir), encoding='utf-8', index=False)
df = pd.read_excel('{}krx.xlsx'.format(dir), dtype={'Symbol': str})


# Reshaping data ============================================
# pd.melt 가로 -> 세로로 melt ================================
df = pd.DataFrame({"a": [4, 5, 6],
                   "b": [7, 8, 9],
                   "c": [10, 11, 12],
                   "d": ['one', 'two', 'three']},
                  index=[1, 2, 3])

pd.melt(df, id_vars=['a'], value_vars=['b', 'c'])
pd.melt(df, value_vars=['a', 'b', 'c'])
df1 = pd.melt(df, id_vars=['d'], value_vars=['a', 'b', 'c']).rename(
    columns={'variable': 'CATEGORY', 'value': 'COUNT'})

# df.pivot 세로 -> 가로로 pivot ================================
df1.pivot(index='d', columns='CATEGORY', values='COUNT')
df1.pivot(index='d', columns='CATEGORY', values='COUNT').reset_index(
).sort_values(['a', 'b']).rename(columns={'a': 'A', 'b': 'B'})

# pd.concat data (Series / dataFrame) 결합, 합치는 방법 ================================
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
pd.concat([s1, s2])
pd.concat([s1, s2], ignore_index=True)  # 기존 index를 무시하고 새로 설정
pd.concat([s1, s2]).reset_index()  # 새로 index를 추가해 줌.
pd.concat([s1, s2], keys=['s1', 's2'])
pd.concat([s1, s2], keys=['s1', 's2'], names=['Series_name', 'Row_ID'])

df1 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]],
                   columns=['letter', 'number'])
df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
                   columns=['letter', 'number', 'animal'])
pd.concat([df1, df2, df3], ignore_index=True)
pd.concat([df1, df3])
pd.concat([df1, df3], join='inner')
pd.concat([df3, df1], join='inner')

df4 = pd.DataFrame([['cat', 'polly'], ['monkey', 'george']],
                   columns=['animal', 'name'])
pd.concat([df3, df4])
pd.concat([df3, df4], join='inner')

# 중복값 유무 확인
df5 = pd.DataFrame([1], index=['a'])
df6 = pd.DataFrame([2], index=['a'])
pd.concat([df5, df6], verify_integrity=True)
# ValueError: Indexes have overlapping values: Index(['a'], dtype='object') 중복값 확인

# Window function : Expanding and Rolling ==================
# .rolling(window=).sum(), mean()===========================
s = pd.Series(np.random.randn(1000),
              index=pd.date_range('1/1/2015', periods=1000))
s.plot()
plt.show()
s = s.cumsum()  # 누적값, cumulationsum
s.plot(style='k--')
plt.show()
# 이동평균선 - Rolling 전월대비 ======================================
r = s.rolling(window=30)
r.mean()  # window의 기간 만큼 rolling 이동 시켜줌.

s.plot(style='k--')
r.mean().plot(style='k')
plt.show()

df = pd.DataFrame(np.random.randn(1000, 4),
                  index=pd.date_range('1/1/2015', periods=1000),
                  columns=['A', 'B', 'C', 'D'])

# 이동합계선 - Rolling 30일이동 합 ======================================
df = df.cumsum()
df.plot(subplots=True)
df.rolling(window=30).sum().plot(subplots=True)
plt.show()

# .expanding
# 이동합계선 - Rolling 30일이동 합 ======================================
df.rolling(window=len(df), min_periods=1).mean().plot()
df.expanding(min_periods=1).mean().plot()
plt.show()

dfe = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
dfe.plot()
dfe.expanding(2).sum().plot()
dfe.expanding(2).mean().plot()
plt.show()
