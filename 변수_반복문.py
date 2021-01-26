### 조건문과 반복문
### for 문의 경우 들여 쓰기를 통해서 이중 삼중 구조로 구분 할 수도 있고, roof 되는 부분은 항상 한Tap 들여써야한다.
### 들여쓰기 오류 발생(Indentation Error: expected an indented block) 발생 가능.

# 구구단 만들기
 
for i in range (1,10):
    for j in range(1,10):
        print(i, "X", j, "=", i* j ) #,는 자동 띄어쓰기.
        print(str(i)+ "X"+ str(j)+ "=", i* j ) # +는 붙여쓰기
        if(j==9): #X9하고 나서 한칸씩 띄도록 조건 지정
            print()

# 특정단까지만 반복 하게 조건
for i in range (1,10) [:5]:
    for j in range(1,10):
        print(i, "X", j, "=", i* j ) #,는 자동 띄어쓰기.
        print(str(i)+ "X"+ str(j)+ "=", i* j ) # +는 붙여쓰기
        if(j==9): #X9하고 나서 한칸씩 띄도록 조건 지정
            print()


#counta를 1씩 증가해서 출력할 때

i = 0
for job in ["MR", "DSM", "PM"]:
    print(i, job)
    i = i+1 

#두개의 Text는 Zip 활용 예
i = ["0","1","2"]
job = ["MR", "DSM", "PM"]
org = ["Sales", "Sales", "MKT"]

for a, b, c in zip(i,job,org):
    print(a, b, c)
 
### Dictionary 생성과 zip 대체 ### dictionary name = {'key name' : value}

g2 = {'b' : 'two',
      'c' : 'three'}
g2['d'] = 'four'
g2

type(g2)

g2.keys()
g2.values()

for i in g2.keys() :
    print(i) 
for i in g2.values() :
    print(i) 
for i, j in zip(g2.keys(), g2.values()): # items()로 대체 가능.
    print(i, j)
for i, j in g2.items():
    print(i, j)

### ================================================================================
### error 나옴 이유

#d = { 'i' : [0,1,2],
#      'job' : ["MR", "DSM", "PM"],
#      'org' : ["Sales", "Sales", "MKT"]}

#for i, job, org in d.items(): 
#    print(i, job, org)
### ================================================================================
