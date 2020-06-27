def removeKey(d,k):
    d.pop(k)
    return d

d={1:2,2:3,6:4}
try:
    k= int(input("Enter a key to remove"))
except ValueError:
    print("Enter integer key")

print("Removing...")
print(removeKey(d,k))