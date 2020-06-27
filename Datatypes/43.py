def removeItem(t,i):    
    # l=list(t)
    # l.remove(i)
    tup=t.index(i)
    return t[0:tup]+t[tup+1:len(t)]


t=(1,2,3,4,5)
try:
    i=int(input(f"Enter one of these items to remove {t}"))
except ValueError:
    print("Enter only the given nums")

print(removeItem(t,i))