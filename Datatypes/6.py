def poor(name):
    n=name.find('not')
    n2=name.find('poor')
   
    if n<n2:
        name1=name[0:n]
        name2=name[n2+4:len(name)]
        name=name1+"good"+name2

    return name


name=input("Enter the string\n")
print(poor(name))