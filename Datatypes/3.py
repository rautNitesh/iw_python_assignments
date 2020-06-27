def change(name):
    n= name[0]
    name_list=list(name)
    for i in range(1,len(name_list)-1):
        if name_list[i]==n:
            name_list[i]='$'
    name="".join(name_list)
    return name


name= input('Enter string\n')
print(change(name))
