def checkIfNumber(n):
    func= lambda x: isinstance(n,int) #or isinstance(n,float)
    return func(n)


try:
    n=input("Enter")
    n=int(n)
except ValueError:
    n=n

c=checkIfNumber(n)
if c:
    print("number")
else:
    print("not number")