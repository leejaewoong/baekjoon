# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

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



