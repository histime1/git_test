import requests

url = 'http://dart.fss.or.kr/pdf/download/excel.do?rcp_no=20200814001766&dcm_no=7446167&lang=ko' # 삼성전자 2020상반기보고서
r = requests.get(url, auth=('user', 'pass'))
r.status_code
r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text
#'{"type":"User"...'
r.json()
#{'private_gists': 419, 'total_private_repos': 77, ...}