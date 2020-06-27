def isPrime(n):
    c=0
    for i in range(2,n//2+1):
        if n%i==0:
            c+=1
    if c>=1:
        print("Composite")
    else:
        print("Prime")

try:
    n=int(input("Enter a number"))
    isPrime(n)
except ValueError:
    print("Enter a number")