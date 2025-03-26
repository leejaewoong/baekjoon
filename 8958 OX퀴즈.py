# 문제 링크: https://www.acmicpc.net/problem/8958

def ox():
    caseNumber = int(input())
    for i in range(caseNumber):
        results = input()
        scores = []
        score = 0                
        count = 0
        for index, result in enumerate(results):            
            if result == 'O':           
                count += 1                
                if index + 1 == len(results):
                    score = count*(count + 1)//2
                    scores.append(score)   
                else:
                    continue
            else:
                score = count*(count + 1)//2
                scores.append(score)
                count = 0                
        answer = sum(scores)
        print(answer)
ox()