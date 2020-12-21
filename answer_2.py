#!/usr/bin/python


chars = [
    'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 
'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 
'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 
's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z'
]

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def base26toint():
    text = input("Enter The String : ")
    if(len(text) % 2 == 0 and hasNumbers(text) == False):
        leng=len(text) /2
        str1=text[:int(leng)]
        str2=text[int(leng):]
        lst1=[]
        lst2=[]
        for a in str1:
            a=a.lower()
            data=chars.index(a)+1
            lst1.append(str(data))
        for a in str2:
            a=a.lower()
            data=chars.index(a)+1
            lst2.append(str(data))
        num = int(''.join(lst1)) + int(''.join(lst2))
        print( "Text to Base26 is : {}".format(str(num)))
        
def numtotext():
    num = input("Enter the first set numbers : ")
    num2 = input("Enter the second set numbers : ")
    lst1=[]
    lst2=[]
    len1=len(num)
    len2=len(num)
    k=''
    for i in num:
        k = k + str(i)
        if(len(k)==2):
            if(int(k) >26):
                for j in k:
                    lst1.append(chars[int(j)-1])
            else:
                lst1.append(chars[int(k)-1])
            k=''
    k=''
    for i in num2:
        k = k + str(i)
        if(len(k)==2):
            # print(k)
            if(int(k) >26):
                for j in k:
                    lst2.append(chars[int(j)-1])
            else:
                lst2.append(chars[int(k)-1])
            k=''
    out=''.join(lst1) + ''.join(lst2)
    print('Base26 to Text : {}'.format(out.upper()))
        


def main():
    print('Select the Option')
    print('1).Text To base26')
    print('2).Base26 to Text')
    select=input()
    if(int(select) == 1):
        base26toint()
    elif(int(select)==2):
        numtotext()
    else:
        print("Sorry Try again")
        exit



main()
