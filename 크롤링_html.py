# Pandas 기초 cheat sheet 따라하기
# 31강~
# 별도 login 없이 table tag 형식으로 되어 있는 경우 html 문서
from io import BytesIO as bt
import re  # 정규식 사용 라이브러리
import requests as rq
import pandas as pd
import numpy as np  # 연산기능
import time
from tqdm import tqdm  # for X in tqdm(X) 기존의 in 구문 시작할때 넣으면 progress bar가 나옴.
import math  # 연산 올림 사용

dir = 'H:/Python/workplace/100.ETC/Seoul_COVID19/'

url0 = 'https://www.seoul.go.kr/coronaV/coronaStatus.do'

table = pd.read_html(url0)
len(table)
table[0].T  # T = transpose() 가로 세로 전환
table[1]
table[2]
col_name = table[3]
table[4]
table[5]
