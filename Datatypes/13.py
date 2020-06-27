def csv(name):
    name=sorted(list(name))
    name=",".join(name)
    return name

name=input("Enter comma separate string\n")
name=name.split(",")

print(csv(name))