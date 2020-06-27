def ing(name):
    if len(name)>=3:
        n=name[-3:len(name)]
        if n == 'ing':
            n=name+"ly"
        else:
            n=name+"ing"
        return n
    return name


name=input("Enter string\n")

print(ing(name))
        