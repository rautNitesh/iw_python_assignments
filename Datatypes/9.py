def exchange(name):
    name=list(name)
    name[0],name[len(name)-1]=name[len(name)-1],name[0]
    name="".join(name)
    return name


name=input("Enter string")

print(exchange(name))