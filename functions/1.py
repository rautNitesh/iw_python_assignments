def findMax(a,b,c):
    return max(a,b,c)
try:
    a=int(input("Enter number"))
    b=int(input("Enter number"))
    c=int(input("Enter number"))
except ValueError:
    print("Input should be number")

print(f"the max num is{findMax(a,b,c)}")