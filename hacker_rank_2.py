def az(fst,ogn):
    az = 'abcdefghijklmnopqrstuvwxyz'
    
    fnt = 0
    bk = 0
    for i in range(len(az)):
        if az[i] == ogn == fst :
            bk = fnt = i
        elif az[i] == fst : 
            fnt = i
        elif az[i] == ogn :
            bk = i
        else:
            pass
        
    return False if bk < fnt else True
    
    
    
def main(sentence):
    
    lst=sentence.split()
    fnrst=""
    for i in range(len(lst)):
        
        stng = str(lst[i]) 
        ln = len(stng)
        lst1=[]
        lst1.append(stng[0])
        for j in range(1,ln):
            #print(stng[j])
            x = stng[j].lower()
            y = stng[j-1].lower()
            result = az(y,x)
            if result == False:
                if stng[j].isupper():
                    lst1.append(stng[j].lower())
                else:
                    lst1.append(stng[j].upper())
            else:    
                lst1.append(stng[j])
        jnst = "".join(lst1)
        fnrst +=   jnst + " "
    return fnrst

if __name__ == '__main__':
    result = main(input("Please enter your string: "))
    print(result)


""" We should use sys.stdin.readline() instead of input() because
    input() will raise an EOF error when there is no input or typo input 
    but sys.stdin.readline() will be closed when there is no input """