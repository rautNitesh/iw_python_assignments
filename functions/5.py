def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

try:
    n=int(input("Enter number to find factorial"))
    print(fact(n))

except ValueError:
    print("The input should be a number")