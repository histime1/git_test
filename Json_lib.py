import pandas as pd
import requests as rq

dir = 'H:/Python/workplace/3.주식관련/ETF종목분석/'
url = 'https://finance.naver.com/api/sise/etfItemList.nhn?etfType=0&targetColumn=market_sum&sortOrder=desc'

r = rq.get(url)
etf_json = r.json()
etf_json
etf_item_list = etf_json['result']['etfItemList']
df = pd.DataFrame(etf_item_list)
df.shape
