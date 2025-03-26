# 문제 링크: https://www.acmicpc.net/problem/2739

def multiple():
    number = int(input())
    i = 0
    while True:
        i += 1
        if i < 10:
            cal = number*i
            print(f"{number} * {i} = {cal}")
        else:
            break
multiple()

