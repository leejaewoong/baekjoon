# 문제 링크: https://www.acmicpc.net/problem/1914

def moveHanoi(num, start, end):
        if num > 1:
            moveHanoi(num-1, start, 6-start-end) 
        print(start, end)  
        if num > 1: 
            moveHanoi(num-1, 6-start-end, end)  

num = int(input()) 
print(2**num - 1)  
moveHanoi(num, 1, 3)  

    


    