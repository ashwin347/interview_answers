import os
import filecmp
def compare(p,q):
    comp= filecmp.cmp(p,q)
    return comp

def sliceit(p):
    value = p[:-4]
    return value

def find_duplicates():
    x=0
    total=os.listdir()
    lst1=[]
    while x < len(total):
        p=total[x]
        temp=[]
        for q in total:
            if p!=q:
                comp=compare(p,q)
                if comp==True:
                    if len(temp)==0:
                        file=sliceit(p)
                        temp.append(file)
                    file=sliceit(q)
                    temp.append(file)
                total.remove(q)
        lst1.append(temp)
        total.remove(p)
    return lst1

if __name__ == '__main__':
    result = find_duplicates()
    for row in result:
        print(" ".join(str(i) for i in row))
