# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# https://www.acmicpc.net/upload/images/f5NhGHVLM4Ix74DtJrwfC97KepPl27s%20(1).png
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

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
    


# %%
