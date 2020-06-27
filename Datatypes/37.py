from functools import reduce
def mulAll(d):
    s=0
    mul= lambda x,y:x*y
    s= reduce(mul,d.values())
    return s

d={1:2,2:3,4:6,7:1}
print(mulAll(d))