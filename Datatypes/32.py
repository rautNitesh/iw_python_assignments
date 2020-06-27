def fillDict(n):
    d={}
    for i in range(1,n+1):
        d[i]=i**2
    return d

try:    
    n=int(input("Enter num"))
    print(fillDict(n))
except ValueError:
    print("Enter integer")