def trim(name):
    if len(name)<2:
        return ''
    else:
        return name[0:2]+name[-2:len(name)]


name= input("Enter string\n")
print(trim(name))
