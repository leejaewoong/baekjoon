# 문제 링크: https://www.acmicpc.net/problem/2577

import math
from collections import Counter

def getNumberCount():    
    numbers = []
    for i in range(3):
        number = int(input())
        numbers.append(number)
    cal = str(math.prod(numbers))    
    countPerNumber = Counter(cal)
    for i in range(10):
        ind = str(i)
        count = countPerNumber.get(ind, 0)
        print(count)

getNumberCount()



