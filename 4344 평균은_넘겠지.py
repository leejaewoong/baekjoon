# 문제 링크: https://www.acmicpc.net/problem/4344

def feelAvg():
    caseNumber = int(input())
    for i in range(caseNumber):
        report = list(map(int, input().split()))
        students = report[0]        
        results = []        
        for i in range(1, students+1):
            result = report[i]
            results.append(result)
        average = sum(results)/students        
        modelStudents = 0
        for i in range(1, students+1):                        
            score = report[i]
            if score > average:
                modelStudents += 1
        ratemodelStudent = round(modelStudents/students*100, 3)
        print(f"{ratemodelStudent:.3f}%")      

feelAvg()
            
        
        
