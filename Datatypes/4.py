def swap(name):
    name1=list(name[0])
    name2=list(name[1])
    name1[0],name2[0]=name2[0],name1[0]
    name1[1],name2[1]=name2[1],name1[1]
    name1="".join(name1)
    name2="".join(name2)
    name= [name1,name2]
    name=" ".join(name)
    return name

   
name=[]
n= input("Enter a string\n")
name.append(n)
n= input("Enter a string\n")
name.append(n)
print(swap(name))