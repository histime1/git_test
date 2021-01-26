### XML 파일에서 불러오기 ================================================================
import pandas as pd 
import xml.etree.ElementTree as ET

### content list 형식으로 ================================================================

xml_data = "H:/Python/workplace/공시기업 corpCode/corpCode.xml"
with open(xml_data, 'rb') as fp:
        content = fp.read().decode('UTF-8')
print(content)

### XML 객체로 Parse -> dataFrame으로 전환 ============================================

import xml.etree.ElementTree as ET

xml_data = "H:/Python/workplace/공시기업 corpCode/corpCode.xml"
with open(xml_data, 'rb') as fp:
        content = fp.read().decode('UTF-8')

parser = ET.XMLParser(encoding="utf-8") 
tree = ET.fromstring(content, parser=parser) 

rows = []
for node in tree :
    corp_codes = node.find('corp_code').text
    corp_names = node.find('corp_name').text
    stock_codes = node.find('stock_code').text
    modify_dates = node.find('modify_date').text
    rows.append({'corp_code' : corp_codes ,
                 'corp_name' : corp_names ,
                 'stock_code' : stock_codes ,
                 'modify_date' : modify_dates})

corpcode_df = pd.DataFrame(rows, columns= ['corp_code', 'corp_name', 'stock_code', 'modify_date'])
print(corpcode_df)

corp_code = corpcode_df['corp_code'].values 
corp_name = corpcode_df['corp_name'].values

dict(zip(corp_code, corp_name))



### for 문으로 전환하려 하였으나 실패 -.-;; ======================================================================

xml_data = "H:/Python/workplace/공시기업 corpCode/corpCode.xml"
with open(xml_data, 'rb') as fp:
        content = fp.read().decode('UTF-8')

parser = ET.XMLParser(encoding='utf-8')    # element tree
tree = ET.fromstring(content, parser=parser)

def xml2df(tree) :
    root = ET.XML(tree)
    all_records = []
    for i, child in root:
        record = {}
        for subchild in child :
            record [subchild.taq] = subchild.text
            all_records.append(record)
        return pd.DataFrame(all_records)
    
df = xml2df(tree)

### ======================================================================



