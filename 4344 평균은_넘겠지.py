# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

def feelAvg():
    caseNumber = int(input())
    for i in range(caseNumber):
        report = list(map(int, input().split()))
        students = report[0]        
        results = []        
        for i in range(1, students+1):
            result = report[i]
            results.append(result)
        totalResults = sum(results)
        average = totalResults/students
        modelStudents = 0
        for i in range(1, students+1):                        
            score = report[i]
            if score > average:
                modelStudents += 1
        ratemodelStudent = round(modelStudents/students*100, 3)
        print(f"{ratemodelStudent:.3f}%")      

feelAvg()
            
        
        
