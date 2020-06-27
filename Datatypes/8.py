def nth(name,n):
    if name is not None and n<len(name):
        name=list(name)
        name.remove(name[n])
        name="".join(name)
        return name
    else:
        print("Error check your string or index")


name=input("Enter string\n")
n=int(input("Enter index"))

print(nth(name,n) or "")
