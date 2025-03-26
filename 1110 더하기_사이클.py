# 문제 링크: https://www.acmicpc.net/problem/1110

def getCycle(NN):    
    
    global count   

    add = str(int(NN[0]) + int(NN[1])) 
    newName = NN[-1] + add[-1] 
    count += 1 

    if N == newName:
        print(count)
        return     

    getCycle(newName)

N = input().zfill(2)
count = 0

getCycle(N)



    