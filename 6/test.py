# 1번 문제

for i in range(1,51):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

# 2번 문제

import random

num = list(range(1,31))

while(1):
    pick = random.sample(num,1)
    num.remove(pick[0])

    if pick[0] % 3 == 0:
        continue
    else:
        print(pick[0])
        if 20 < pick[0]:
            print(num)
            break