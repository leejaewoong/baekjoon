# 문제 링크: https://www.acmicpc.net/problem/2805

def getHeight(trees, need):
    highest = max(trees)
    a = 0
    b = highest    

    while a <= b:
        mid = (a+b)//2
        rest = sum([i-mid for i in trees if i >= mid])        

        if rest > need:            
            a = mid+1   

        elif rest < need:
            b = mid-1  

        else:
            print(mid)
            return
        
    print(mid)

getHeight(array, num)    




    
        


    