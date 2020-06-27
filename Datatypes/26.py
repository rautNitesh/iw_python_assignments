def insertString(items,str):
    str+='{0}'
    items2=[]
    items2+=((map(str.format,items)))
    # for i in range(len(items)):
    #     l=items[i]
    #     items[i]="emp"+str(l)
    print(items2)


items=[1,2,3,4,56]
str="emp"
insertString(items,str)
