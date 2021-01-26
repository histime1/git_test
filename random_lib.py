### random 함수 - 숫자를 임의로 생성 ###

from random import *

print(random())
print(int(random() * 10))
print(int(random() * 10)+1)  # 1~10까지 숫자만 출력
print(int(random() * 45)+1)  # 1~45까지 숫자만 출력
print(randrange(1, 46))  # 1~45까지 숫자만 출력
print(randint(1, 45))  # 1~45이하의 숫자만 출력
print(5 > 10)
print(not True)
print(not(5 > 10))
