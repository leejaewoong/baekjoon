# %%
# try / else / finally
num = 7

def test(text:str):         
    try:
        if not isinstance(text, str):
            raise TypeError ("str만 지원합니다.")
    
        else:
            for letter in range(len(text)):
                print('letter')   

    finally:
        print('함수를 마칩니다.')

test(num)   