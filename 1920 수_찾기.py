# 문제 링크: https://www.acmicpc.net/problem/1920

import sys

input = sys.stdin.readline

N = int(input())
array1 = sorted(map(int, input().split()))

M = int(input())
array2 = list(map(int, input().split()))

def binary(target, value):
    for V in value:
        start, end = 0, len(target) - 1
        found = False
        while start <= end:
            mid = (start + end) // 2
            if target[mid] == V:
                found = True
                break
            elif target[mid] < V:
                start = mid + 1
            else:
                end = mid - 1
        if found:
            print(1)
        else:
            print(0)

binary(array1, array2)
