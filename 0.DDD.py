# ================================= DDD DATA EXCEL Raw PROCESSING =============================

# 0. Import Data and configure parameters ----------------------------------------------
from io import BytesIO as bt
import requests as rq
import pandas as pd 
import datetime
import os

#DDD folder 지정

DDD_dir = 'F:/AMD_HDD용/Sanofi/Market data/DDD/'

# options(scipen = 999999, digits = 22) 

# Parameter setup 

t_data = ['IMS', 'DDD', 'UBIST','CAM']

st_date = datetime.date(2018, 10, 1)
en_date = datetime.date(2020, 9, 1)
date = pd.date_range(st_date, en_date, freq='M')

dir = (DDD_dir + format(en_date, '%Y') + '/'+ format(en_date, '%Y%m')+ '/IAM Raw/') # excel raw data directory
et_dir = (DDD_dir + format(en_date, '%Y') + '/' + format(en_date, '%Y%m')+ '/P_Raw/') # 추출 directory
# Exf <- paste0(format(en_date, '%Y'), '/', format(en_date, '%Y%m'),  '/Final file/') #xls 출력 사용시 
Pmd = 'F:/AMD_HDD용/Sanofi/Market data/Master-IMS,DDD,UBIST/Final secondary master/' # product master directory
Bmd = 'F:/AMD_HDD용/Sanofi/Market data/DDD/DDD MASTER/Brick master/' # Brick master directory

# 1. Brick Master update -------------------------------------------------------

B_master = pd.read_excel(Bmd+'BRICK MASTER FILE('+format(en_date,'%Y%m')+').xlsx'
                 #, sheet_name = "연결 재무상태표"
                 #, header = 5
                 #, skiprows = 5 # header 대신 사용
                 #, names = ['1st column 명' ,'2nd column 명']
                 #, dtype = {'1st column 명' : str, '2nd column 명' : np, int64, '3rd column 명' : float }
                 # 문자열(string), 정수형(integer), 부동소수형(float)
                 #, index_col = 'id'                 
                 #, na_values= 'NaN'
                 #, thousands=','
                 #, nrows = 10) #10번째행까지만 잘라서 출력
                       , sheet_name = 1
#                       , index_col = 'Brick Code(IAM)'
                       , na_values= 'NaN' 
                       , thousands=','       
                       , nrows = 10
                       )

s=B_master['Brick Code(IAM)']
s

setDT(B_master)
str(B_master)
names(B_master)

B_master[, c('Brick Code(IAM)', 'Brick_Name_E', 'HIRA 지역코드명칭') := NULL] 
setnames(B_master, 'Brick_Code (숫자변환용)', 'Brick_Code')
names(B_master)


# 2. Aprovel ---------------------------------------------------------------------------

p <- 'APROVEL'

# 2_1. Product Master update -------------------------------------------------------

Pm <- read_excel(path=paste0(Pmd, 'Master for ', p, '.xlsx')
                 , sheet = 3
                 , skip = 1  # Minimum number of rows to skip before reading anything
                 , col_names = TRUE)

setDT(Pm)
names(Pm)

Pm1 <- Pm[, !(1:7)]
names(Pm1)
Pm2 <- Pm1[, 1:9]
Pm3 <- Pm2[!is.na(Products), ]
names(Pm3) <- c("ATC", "Product", "Molecule", "Product_G", "Molecule_S", "ORIGINAL_GX", "MOLETYPE", "FAMILY",
  "APROVEL_COREMOL")

Mm <- read_excel(path=paste0(dir, 'Aprovel Raw data 1(C09C-Value)', '.xlsx') #당월 product 전체list
                 , sheet = 4
                 #, range = "B3:E8", # cell range to read from
                 , skip = 4 # Minimum number of rows to skip before reading anything
                 , col_names = TRUE # TRUE to use the first row as column names
                )
setDT(Mm)
names(Mm)

Mm1 <-Mm[, 1:2]
Pm4 <- Pm3[Mm1, on =. (Product)]
names (Pm4)

# Product master update 용 data extraction ==================================================

Pmu <-Pm4[is.na(ATC), ]
Pmu <- unique(Pmu [, 1:3])
Pmu1 <- Mm[Pmu, on =. (Product)]
Pmu2 <- Pmu1[, 1:3]
Pmu2 <- unique(Pmu2 [, 1:3])
setcolorder(Pmu2, c('ATC4',	'Product',	'Manufacturer'))
print(Pmu2)

write.table(Pmu2
            , paste0(Rf, p, '_master_NA_',  format(en_date, '%Y%m'), '.csv')
            , sep=','
            , col.names = T
            , row.names = F)

# Product master update 파일 저장 후 재 실행========================================================

names(Pm4)
P_master <- unique(Pm4 [, .(ATC, Product, Manufacturer, Molecule, Product_G, Molecule_S, ORIGINAL_GX, MOLETYPE, FAMILY, APROVEL_COREMOL)])

TEST <- P_master[, .N, keyby = .(Product)]
print(TEST[N>1,])
print(P_master[, sum(is.na(Product))])
colSums(is.na(P_master)) #MNF NA 이번달에 제품 매출이 0인 경우.

# 2_2. Counting unit Volume update ===============================================================

CV <-Mm[, !5]
CV <- P_master[CV, on =. (Product, Manufacturer)]
CV[, ATC4 := NULL][, Molecule := NULL]
names(CV)

names(CV) <- c("ATC", "Product", "Manufacturer" , "PRODUCT_G", "MOLECULE_S", "ORIGINAL_GX", "MOLETYPE", "FAMILY", "APROVEL_COREMOL", "MOLECULE", as.character(date))

setcolorder(CV, c("Product", "Manufacturer",as.character(date),"ATC", "MOLECULE","MOLECULE_S", "PRODUCT_G", "ORIGINAL_GX", "MOLETYPE", "FAMILY", "APROVEL_COREMOL"))

CV[FAMILY == '0', FAMILY := '']
CV[is.na(FAMILY), FAMILY := '']

write.table(CV
            , paste0(Rf, t_data[2], ' ', p, '_CU_Volume_Raw_Final',  format(en_date, '%Y%m'), '.csv')
            , sep=','
            , col.names = T
            , row.names = F)

# 2_3. Aprovel value update =============================================================================

Ap <- read_excel(path=paste0(dir, 'Aprovel Raw data 1(C09C-Value)', '.xlsx')
                , sheet = 1
                , skip = 5 # Minimum number of rows to skip before reading anything
                , col_names = TRUE # TRUE to use the first row as column names
                )

Ap1 <- read_excel(path=paste0(dir, 'Aprovel Raw data 2(C09D-Value)', '.xlsx')
                 , sheet = 1
                 , skip = 5 # Minimum number of rows to skip before reading anything
                 , col_names = TRUE # TRUE to use the first row as column names
                )

Ap2 <- read_excel(path=paste0(dir, 'Aprovel Raw data 2(C09D-Value)', '.xlsx')
                  , sheet = 2
                  , skip = 5 # Minimum number of rows to skip before reading anything
                  , col_names = TRUE # TRUE to use the first row as column names
                )

setDT(Ap)
setDT(Ap1)
setDT(Ap2)

dt <- rbindlist(list(Ap, Ap1, Ap2), use.names = T)

str(dt)
names(dt)

names(dt) <- c('code', 'Product', as.character(date)) 
names(dt)
dt$code <- as.numeric(as.character(dt$code)) #column의 character 바꾸기
str(dt)

dt1 <- P_master[dt, on =. (Product)] #서로 다른 컬럼 Join하는 것.
dt2 <- B_master[dt1, on =.  ( Brick_Code = code )]

dt2[FAMILY == '0', FAMILY := ''][is.na(FAMILY), FAMILY := '']

names(dt2)

print(dt2[, sum(is.na(Product_G))])
colSums(is.na(dt2))

#names(dt2)[1] <- 'code2' #첫 컬럼만 이름 바꿀때, 

names(dt2) <- c('code', 'Brick_Name_K', 'Region', 'HVB_GB', 'REGION(시단위)', 'REGION(구단위)', 'Brick_address', 'HIRA_code'
                , 'CV HP Team', 'CV MR', 'DMCKD HP Team', 'DMCKD MR', 'DES', 'DES Specialsit', 'Clinic Team', 'Clinic MR', 'Digital', 'SCS'
                ,'ATC', 'Product', 'Manufacture', 'MOLECULE', 'PRODUCT_G',  'MOLECULE(S)','ORIGINAL/GX',  'MOLETYPE', 'Family', 'APROVEL/COREMOL', as.character(date))

setcolorder(dt2, c('code',	'Brick_Name_K',	'Product', 'Manufacture',	as.character(date),	'ATC',	'MOLECULE',	'MOLECULE(S)',	'PRODUCT_G',	'ORIGINAL/GX',	'MOLETYPE',	'Family',	'APROVEL/COREMOL',	'Region',	'HVB_GB',	'REGION(시단위)',	'REGION(구단위)',	'Brick_address',	'HIRA_code',	'CV HP Team',	'CV MR',	'DMCKD HP Team',	'DMCKD MR',	'DES',	'DES Specialsit',	'Clinic Team',	'Clinic MR',	'Digital', 'SCS'))

names(dt2)

write.table(dt2
            , paste0(Rf, t_data[2], ' ', p, '_Raw_Final',  format(en_date, '%Y%m'), '.csv')
            , sep=','
            , col.names = T
            , row.names = F)