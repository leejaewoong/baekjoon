# 문제 링크: https://www.acmicpc.net/problem/1065

def getOne():
    num = int(input())
    if num < 100:
        print(num)
    else:
        count = 99
        for num in range(100, num+1):
            string = str(num)
            num_list = [int(i) for i in string]
            if num_list[1] - num_list[0] == num_list[2] - num_list[1]:                
                count +=1
        print(count)

getOne()


    