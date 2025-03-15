# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

def getGrade():
    score = int(input())
    if score > 89:
        print ('A')
    elif score < 90 and score > 79:
        print ('B')
    elif score < 80 and score > 69:
        print ('C')
    elif score < 70 and score > 59:
        print ('D')
    else:
        print ('F')                        

getGrade()

