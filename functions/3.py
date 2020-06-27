from functools import reduce
def mulList(l):
    m=[]
    mul= lambda x,y:x*y
    m=reduce(mul,l)
    print(m)


l=[1,2,3,4,5]
mulList(l)