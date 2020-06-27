def findIndex(l,i):
    print(l.index(i))


l=(1,2,3,5,6)
try:
    i=int(input(f"Enter element to find index{l}"))
except ValueError:
    print("Enter the element from the tuple")
findIndex(l,i)