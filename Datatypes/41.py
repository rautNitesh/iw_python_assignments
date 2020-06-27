from functools import reduce
def toString(t):
    s= ""
    convert= lambda x,y : x+y
    s+=reduce(convert,t)
    print(s)
    print(type(s))


toString(('p','y','t','h','o','n'))