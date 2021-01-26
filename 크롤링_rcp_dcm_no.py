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
# import xml.etree.ElementTree as ET  # xml을 불러오는 라이브러리
import FinanceDataReader as fdr  # 주식 정보를 불러오는 라이브러리
from tqdm import tqdm  # for X in tqdm(X) 기존의 in 구문 시작할때 넣으면 progress bar가 나옴.
import time  # roof 돌때 time.sleep(4) 4초 sleeping 가능
from requests.api import head

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

# From FinanceDateReader package =============================================
# 코스피, 코스닥, 코넥스 전체 - KRX stock symbol list (종목 list)

df_krx = fdr.StockListing('KRX')
df_krx.shape
no_of_rows = len(df_krx.index)
df_krx.loc[0]

# unique한 Market 명과 갯수
# df_krx.drop_duplicates(subset='Market', keep='first')
# df_krx['Market'].value_counts()

# ======================================================================
# Error filtering (1)
# Sector중 error 발생되는 영역 제외 : 자료 미지원, PDF only etc
# ex_Sector_list = ['금융 지원 서비스업', '기타 금융업', '보험 및 연금관련 서비스업', '보험업', '재 보험업']
# df_krx_v1 = df_krx[~df_krx.Sector.isin(ex_Sector_list)]

# corp_list 중 error 발생되는 회사들 제외 : 자료 미지원, PDF only etc
# ex_Symbol = ['011150', '069730', '114090', '030200']

# df_krx_v2 = df_krx_v1[~df_krx_v1.Symbol.isin(ex_Symbol)]
# df_corp = df_krx_v2[['Market', 'Symbol', 'Name']]

#df_corp_kp = df_corp[df_corp.Market.isin(['KOSPI'])]
#df_corp_kd = df_corp[df_corp.Market.isin(['KOSDAQ'])]
#df_corp_kn = df_corp[df_corp.Market.isin(['KONEX'])]
# corp_list = df_corp_kd[['Symbol', 'Name']].values #[1036:no_of_rows]
# =========================================================================
###
# corp_list = df_krx.loc[(((df_krx['Sector'] != '금융 지원 서비스업')
#                          & (df_krx['Sector'] != '기타 금융업')
#                          & (df_krx['Sector'] != '보험 및 연금관련 서비스업')
#                          & (df_krx['Sector'] != '보험업')
#                          & (df_krx['Sector'] != '재 보험업'))
#                         & ((df_krx['Symbol'] != '011150')
#                            & (df_krx['Name'] != '069730')
#                            & (df_krx['Name'] != '114090')
#                            & (df_krx['Name'] != '030200')
#                            & (df_krx['Name'] != '306620'))
#                         & (df_krx['Market'] == 'KOSDAQ')), ['Symbol', 'Name']].values #[:no_of_rows]

market = ['KOSPI', 'KOSDAQ']
corp_list = df_krx.loc[(df_krx['Market'] == 'KOSPI'), (['Symbol', 'Name'])]
no_of_rows = len(corp_list)
print(no_of_rows)

# API를 통한 rcp_no 추출 with Dart_OpenAPI====================================================

crtfc_key = 'ca1a25e36025c3af6d593a5a484a19a7f503e62d'
bgn_de = '20200101'
# 고정 : 수정보고서 있으면 적용 -> Y
last_reprt_at = 'Y'
pblntf_detail_ty = 'A001&pblntf_detail_ty=A002&pblntf_detail_ty=A003'  # 고정 : 분기, 반기, 사업보고서
# 최대 출력 Page수 1~100까지
page_count = '100'
# corp_code = '306620'  # '005930'
# corp_name = '네온테크' # '삼성전자'
sleepingtime = 2
Error_corp = []

KOSPI = ([0, 50], [51, 880], [881, no_of_rows])
#KOSDAQ = ([0, 680], [681, 785], [786, 904], [905, 1214] [1215, no_of_rows])

for start, end in KOSPI:  # KOSDAQ
    corp_list = corp_list.values[881: no_of_rows]  # [start : end]
    corp_list.shape
    N = 881  # start
    print(start, end)

    for corp_code, corp_name in tqdm(corp_list):
        print(corp_code, corp_name)

        try:
            url1 = 'https://opendart.fss.or.kr/api/list.xml?crtfc_key={}&bgn_de={}&last_reprt_at=Y&pblntf_detail_ty=A001&pblntf_detail_ty=A002&pblntf_detail_ty=A003&page_count={}&corp_code={}'.format(
                crtfc_key, bgn_de, page_count, corp_code)
            # r = rq.get (url1, verify=False) # verify 오류 허용
            r = rq.get(url1, headers={"user-agent": user_agent})
            wp = r.content.decode('UTF-8')
            rcp_no_list = re.findall(r'<rcept_no>(.*?)</rcept_no>', wp)
            rpt_no_list = re.findall(r'<report_nm>(.*?)</report_nm>', wp)
            period_list = re.findall(r'<rcept_dt>(.*?)</rcept_dt>', wp)
            dict(zip(period_list, rcp_no_list))
            # dcm_no 추출 with Dart_OpenAPI based on rcm_no ==============================================
            dcm_no_list = []
            for rcp_no in rcp_no_list:  # [:10] 갯수제한을 하고자 할때 : 앞에 추가
                url2 = 'http://dart.fss.or.kr/dsaf001/main.do?rcpNo={}'.format(
                    rcp_no)
                #dcm = rq.get(url2, verify=False)
                dcm = rq.get(url2, headers={"user-agent": user_agent})
                wp2 = dcm.content.decode('utf-8')
                # 정규식 사용, [0] - unique하게 처음나오는 하나만 추출
                dcm_no = re.findall(
                    r"'{}', '(.*?)',".format(rcp_no), wp2)[0]
                dcm_no_list.append(dcm_no)
            dcm_no_list
            # Dart_site 통한 추출 with consol data =============================================

            def download_excel(period, rcp_no, dcm_no, corp_code, corp_name):
                url3 = "http://dart.fss.or.kr/pdf/download/excel.do?rcp_no={}&dcm_no={}&lang=ko".format(
                    rcp_no, dcm_no)
                r = rq.get(url3, headers={"user-agent": user_agent})
                dt = bt(r.content)
                i = ["연결 재무상태표", "연결 포괄손익계산서"]
                # i = ["재무상태표", "포괄손익계산서"] # error 처리시 사용
                for sheet in i:
                    df = pd.read_excel(dt, sheet_name=sheet,
                                       header=5, na_values=0, thousands=',')
                    df.to_csv('{}_{}_{}_{}.csv'.format(str(period), str(
                        corp_code), corp_name, sheet), encoding="euc-kr")
                    # df.to_excel(str(period)+corp_name+sheet+".xlsx", encoding="UTF-8")
            for period, rcp_no, dcm_no in zip(period_list, rcp_no_list, dcm_no_list):
                download_excel(period, rcp_no, dcm_no,
                               corp_code, corp_name)
                print('=========================================================')
                time.sleep(sleepingtime)
                print("Let me sleep for {} seconds".format(sleepingtime))
                print('=========================================================')
                print('{}번째_{}_{}_{}_done.'.format(
                    N, str(period), str(corp_code), corp_name))
                print('now let me continue ~~~')

        except TypeError:
            TypeError_corp = []
            TypeError_corp.append(corp_code)
            print('TypeERROR in : {}번째_{}_{}'.format(
                N, corp_code, corp_name))

        except ValueError:
            ValueError_corp = []
            ValueError_corp.append(corp_code)
            print('ValueError in : {}번째_{}_{}'.format(
                N, corp_code, corp_name))

            def download_excel_1(period, rcp_no, dcm_no, corp_code, corp_name):
                url4 = "http://dart.fss.or.kr/pdf/download/excel.do?rcp_no={}&dcm_no={}&lang=ko".format(
                    rcp_no, dcm_no)
                r = rq.get(url4, headers={"user-agent": user_agent})
                dt = bt(r.content)
                i = ["재무상태표", "포괄손익계산서"]
                for sheet in i:
                    df = pd.read_excel(dt, sheet_name=sheet,
                                       header=5, na_values=0, thousands=',')
                    # period int type이므로 str으로 전환
                    df.to_csv('{}_{}_{}_{}.csv'.format(str(period), str(
                        corp_code), corp_name, sheet), encoding="euc-kr")
                    # df.to_excel(str(period)+corp_name+sheet+".xlsx", encoding="UTF-8")
            for period, rcp_no, dcm_no in zip(period_list, rcp_no_list, dcm_no_list):
                download_excel_1(period, rcp_no, dcm_no,
                                 corp_code, corp_name)
                print('=========================================================')
                time.sleep(sleepingtime)
                print("Let me sleep for {} seconds".format(sleepingtime))
                print('=========================================================')
                print('{}번째_{}_{}_{}_done.'.format(
                    N, str(period), str(corp_code), corp_name))
                print('now let me continue ~~~')
        except:
            Error_corp.append(corp_code)
            e = pd.Series(Error_corp)
            e.to_csv('Error_corp_list.csv', encoding='euc-kr')
            print('Error in : {}번째_{}_{}'.format(N, corp_code, corp_name))
            pass

    s = pd.Series([N])
    s.to_csv('Data was done until_{}th company.csv'.format(
        N), encoding='euc-kr')
    N = N + 1
    time.sleep(sleepingtime)
    if N == no_of_rows:
        print("OPERATION IS DONE.......................................")
        print("========================================================")
    else:
        print('waiting for continue ~~~')

### Error Corp에 대해서는 여기서 부터 다시 ###
# ==============================================================
# Error_corp_list_처리
# ================================================================

dir = 'H:/Python/workplace/2.Dart_API/Financial_data/Error_Corp_list/'
all_data = os.listdir(dir)  # dir에 있는 화일 리스트 확인

error_list = pd.Series([])  # , columns=['core_code', 'core_name'])
No = 0

for filename in os.listdir(dir):
    print(filename)
    filename = 'KOSDAQ_Error_corp_list(0~680).csv'
    Sr = pd.read_csv('{}{}'.format(dir, filename), encoding='euc-kr').values
    ### 여기서 부터 다시 ###
    error_list = error_list.append(Sr)
    add = re.findall(r"[[, (.*?),]]", Sr)
    N = N + 1
    print(N)

no_of_error_list = len(error_list)
print(no_of_error_list)
corp_list = error_list

No = 0

for corp_code, corp_name in corp_list:
    print(corp_code, corp_name)

    try:
        url1 = 'https://opendart.fss.or.kr/api/list.xml?crtfc_key={}&bgn_de={}&last_reprt_at=Y&pblntf_detail_ty=A001&pblntf_detail_ty=A002&pblntf_detail_ty=A003&page_count={}&corp_code={}'.format(
            crtfc_key, bgn_de, page_count, corp_code)
        # r = rq.get (url1, verify=False) # verify 오류 허용
        r = rq.get(url1, headers={"user-agent": user_agent})
        wp = r.content.decode('UTF-8')
        rcp_no_list = re.findall(r'<rcept_no>(.*?)</rcept_no>', wp)
        rpt_no_list = re.findall(r'<report_nm>(.*?)</report_nm>', wp)
        period_list = re.findall(r'<rcept_dt>(.*?)</rcept_dt>', wp)
        dict(zip(period_list, rcp_no_list))
        # dcm_no 추출 with Dart_OpenAPI based on rcm_no ==============================================
        dcm_no_list = []
        for rcp_no in rcp_no_list:  # [:10] 갯수제한을 하고자 할때 : 앞에 추가
            url2 = 'http://dart.fss.or.kr/dsaf001/main.do?rcpNo={}'.format(
                rcp_no)
            #dcm = rq.get(url2, verify=False)
            dcm = rq.get(url2, headers={"user-agent": user_agent})
            wp2 = dcm.content.decode('utf-8')
            # 정규식 사용, [0] - unique하게 처음나오는 하나만 추출
            dcm_no = re.findall(
                r"'{}', '(.*?)',".format(rcp_no), wp2)[0]
            dcm_no_list.append(dcm_no)
        dcm_no_list
        # Dart_site 통한 추출 with consol data =============================================

        def download_excel(period, rcp_no, dcm_no, corp_code, corp_name):
            url3 = "http://dart.fss.or.kr/pdf/download/excel.do?rcp_no={}&dcm_no={}&lang=ko".format(
                rcp_no, dcm_no)
            r = rq.get(url3, headers={"user-agent": user_agent})
            dt = bt(r.content)
            #i = ["연결 재무상태표", "연결 포괄손익계산서"]
            i = ["재무상태표", "포괄손익계산서"]  # error 처리시 사용
            for sheet in i:
                df = pd.read_excel(dt, sheet_name=sheet,
                                   header=5, na_values=0, thousands=',')
                df.to_csv('{}_{}_{}_{}.csv'.format(str(period), str(
                    corp_code), corp_name, sheet), encoding="euc-kr")
                # df.to_excel(str(period)+corp_name+sheet+".xlsx", encoding="UTF-8")
        for period, rcp_no, dcm_no in zip(period_list, rcp_no_list, dcm_no_list):
            download_excel(period, rcp_no, dcm_no,
                           corp_code, corp_name)
            print('=========================================================')
            time.sleep(sleepingtime)
            print("Let me sleep for {} seconds".format(sleepingtime))
            print('=========================================================')
            print('{}번째_{}_{}_{}_done.'.format(
                N, str(period), str(corp_code), corp_name))
            print('now let me continue ~~~')
    except TypeError:
        TypeError_corp = []
        TypeError_corp.append(corp_code)
        print('TypeERROR in : {}번째_{}_{}'.format(
            N, corp_code, corp_name))
    except ValueError:
        ValueError_corp = []
        ValueError_corp.append(corp_code)
        print('ValueError in : {}번째_{}_{}'.format(
            N, corp_code, corp_name))

        def download_excel_1(period, rcp_no, dcm_no, corp_code, corp_name):
            url4 = "http://dart.fss.or.kr/pdf/download/excel.do?rcp_no={}&dcm_no={}&lang=ko".format(
                rcp_no, dcm_no)
            r = rq.get(url4, headers={"user-agent": user_agent})
            dt = bt(r.content)
            i = ["재무상태표", "포괄손익계산서"]
            for sheet in i:
                df = pd.read_excel(dt, sheet_name=sheet,
                                   header=5, na_values=0, thousands=',')
                # period int type이므로 str으로 전환
                df.to_csv('{}_{}_{}_{}.csv'.format(str(period), str(
                    corp_code), corp_name, sheet), encoding="euc-kr")
                # df.to_excel(str(period)+corp_name+sheet+".xlsx", encoding="UTF-8")
        for period, rcp_no, dcm_no in zip(period_list, rcp_no_list, dcm_no_list):
            download_excel_1(period, rcp_no, dcm_no,
                             corp_code, corp_name)
            print('=========================================================')
            time.sleep(sleepingtime)
            print("Let me sleep for {} seconds".format(sleepingtime))
            print('=========================================================')
            print('{}번째_{}_{}_{}_done.'.format(
                N, str(period), str(corp_code), corp_name))
            print('now let me continue ~~~')
    except:
        Error_corp.append([corp_code])
        e = pd.Series([Error_corp])
        e.to_csv('Error_corp_list.csv', encoding='euc-kr')
        print('Error in : {}번째_{}_{}'.format(N, corp_code, corp_name))
        pass
s = pd.Series([N])
s.to_csv('Data was done until_{}th company.csv'.format(N), encoding='euc-kr')
N = N + 1
time.sleep(sleepingtime)
if N == no_of_error_list:
    print("OPERATION IS DONE.......................................")
    print("========================================================")
else:
    print('waiting for continue ~~~')
