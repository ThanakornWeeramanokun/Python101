name = 'Boss'
print(name)
# Boss
name.lower()
# 'boss'
name.upper()
# 'BOSS'
#เรียกว่าการใช้ string method

friend = 'สมชาย'
money = '10'

print(friend + 'ยืมเงิน ' + str(money) + ' บาท')
#สมชายยืมเงิน 10 บาท
print('{}ยืมเงิน {} บาท'.format(friend,money))
#สมชายยืมเงิน 10 บาท
print(f'{friend}ยืมเงิน {money} บาท')
#สมชายยืมเงิน 10 บาท

money = 145454111534
print(f'{money:,}')
# 145,454,111,534

print(f'{money:,.2f}')
# 145,454,111,534.00
print('{:,.2f}'.format(money))
# 145,454,111,534.00

import math
math.pi
# 3.141592653589793
math.pi * (5 ** 2)
# 78.53981633974483

from datetime import datetime
datetime.now()
# datetime.datetime(2023, 2, 24, 0, 13, 28, 136099)
datetime.now().strftime('%Y%m%d %H:%M:%S')
# '20230224 00:14:19'

import random
random.randint(1,7)
# 7

store = ['ป้าส้ม','ป้าเล็ก','ลุงดำ']
random.choice(store)
# 'ป้าเล็ก'