# 문제 링크: https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

def bin_search(array, num): 
    
    left = 0
    right = len(array) -1    

    while left < right:
        mid = (left + right)//2
        if num > array[mid]:
           left = mid + 1
        elif num < array[mid]:
            right = mid -1 
        else:
            return 1        
    
    if num == array[left]:
        return 1
    else:
        return 0
    
def isHave(own, comparison): 

    own = sorted(own)    
    ans = []

    for num in comparison:
        result = bin_search(own, num)        
        ans.append(result)

    print(*ans)

ownN = int(input())
own = list(map(int, input().split()))
comparisonN = int(input())
comparison = list(map(int, input().split()))

isHave(own, comparison)
        
