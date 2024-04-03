import random

min = int(input('請決定隨機數字範圍最小值: '))
max = int(input('請決定隨機數字範圍最大值: '))
r = random.randint(min, max)
count = 0
while True:
    num = int(input("請輸入一個數字 :"))
    count += 1
    if num == r:
        print('答對了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('再小一點!')
    else:
        print('再大一點!')
    print('這是你猜的第', count, '次')
