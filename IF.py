# 조건문 ======================================================================

stock_name = '키움증권'
sales = 10000
stock_com = ['키움증권', '카카오증권', '다음증권']
if stock_name in stock_com and sales > 10000:
    print('강추')
elif stock_name in stock_com and sales > 5000:
    print('추천')
else:
    print('비추')

# or
# and
# a in [a, b, c, d, e]
