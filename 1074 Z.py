# 문제 링크: https://www.acmicpc.net/problem/1074

n, y, x = map(int, input().split())

count = 0

def drawZ(n, x, y, count):
    
    if n == 0:
        print(count)
    
    if n > 0:
        half = 2**(n-1)         

        if x >= half:
            count += 4**(n-1)
            x -= half             

        if  y >= half:
            count += 4**(n-1) * 2            
            y -= half            
        
        drawZ(n-1, x, y, count)          

drawZ(n, x, y, count)


    


