def isInRange(n,a,b):
    for i in range(a,b):
        if i ==n:
            return True
    return False
try:
    a=int(input("Enter the lower bound"))
    b=int(input("Enter the upper bound"))
    n=int(input("Enter the number"))
    print(isInRange(n,a,b))
except ValueError:
    print("Enter number in all fields")