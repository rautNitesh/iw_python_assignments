def oddIndex(name):
    name=list(name)
    for item in range(len(name)-1):
        if item%2 !=0:
            name.remove(name[item])
    name="".join(name)
    return name

name="nitesh"

print(oddIndex(name))