# 문제 링크: https://www.acmicpc.net/problem/2588

def multilines_input():
    lines = []
    while True:        
        try:
            line = input()
            if not line:
                break
        except EOFError:
            break
        lines.append(line)        
    line1 = int(lines[0])
    line2 = int(lines[1])
    hundreds = list(str(line2))[0]
    tens = list(str(line2))[1]
    ones = list(str(line2))[2]
    cal100 = int(int(hundreds)*line1)
    cal10 = int(int(tens)*line1)
    cal1 = int(ones)*line1    
    total = cal100*100 + cal10*10 + cal1
    print(cal1)
    print(cal10)
    print(cal100)
    print(total)

multilines_input()
    


