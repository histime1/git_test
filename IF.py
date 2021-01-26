
for i in range(20):
    print(i)

for i in range(0, 20, 4):  # 4로 나누어서 떨어지는 숫자들
    print(i)

for i in range(1, 20, 4):  # 4로 나누어서 1이 남은 숫자들
    print(i)


21 // 4
21 % 4

for i in range(20):
    print(i, i % 4)


# 조건문 ======================================================================

for i in range(20):
    remain = i % 4
    if remain == 3:
        print(i, remain)
    else:
        print('no')
