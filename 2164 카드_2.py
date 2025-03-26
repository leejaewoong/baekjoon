# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque
import sys

input = sys.stdin.readline

def getLast():
    N = int(input())
    deck = deque(i+1 for i in range(N))       

    while len(deck) > 1:
        deck.popleft()        
        deck.append(deck.popleft())               

    print(deck[-1])

getLast()



    
