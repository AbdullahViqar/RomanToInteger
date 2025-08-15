x = input("Enter roman number")
def roman(n):
    num=0
    
    #we must handle cases such as IV and CM which translate to 4 and 900 respectively

    if 'IV' in n:
        num+=4
        n = n.replace("IV","")
    elif 'IX' in n:
        num+=9
        n = n.replace("IX","")
    elif 'XL' in n:
        num+=40
        n = n.replace("XL","")
    elif 'XC' in n:
        num+=90
        n = n.replace("XC","")
    elif 'CD' in n:
        num+=400
        n = n.replace("CD","")
    elif 'CM' in n:
        num+=900
        n = n.replace("CM","")

    #standard conversion
    for i in n:
        if i == 'I':
            num+=1
        elif i == 'V':
            num+=5
        elif i == 'X':
            num+=10
        elif i == 'L':
            num+=50
        elif i == 'C':
            num+=100
        elif i == 'D':
            num+=500
        elif i == 'M':
            num+=1000
        
        print("The number is", num)

roman(x)
