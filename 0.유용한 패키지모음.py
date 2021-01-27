
from io import BytesIO as bt
from re import A
from typing import ValuesView
from zipfile import ZIP_FILECOUNT_LIMIT
from numpy.core.fromnumeric import shape, std, var
from numpy.lib.function_base import median, quantile
from pandas._libs.missing import NA
from pandas.core.frame import DataFrame
import requests as rq
import pandas as pd
import numpy as np  # 연산기능
import re  # 정규식 사용 라이브러리
import os  # 화일 복사 탐색 불러오기 등의 operation library
import xml.etree.ElementTree as ET  # xml을 불러오는 라이브러리
import FinanceDataReader as fdr  # 주식 정보를 불러오는 라이브러리
from tqdm import tqdm  # for X in tqdm(X) 기존의 in 구문 시작할때 넣으면 progress bar가 나옴.
import time  # roof 돌때 time.sleep(4) 4초 sleeping 가능
from requests.api import head
import matplotlib.pyplot as plt  # statistical data visualization 시각화
import seaborn as sns  # statistical data visualization 시각화
import itertools as import  # 반복값 처리하는 패키지
# %matplotlib inline : 쥬피터노트북에서 자동으로 그래프를 보여줌.

# 1st update to Remote
