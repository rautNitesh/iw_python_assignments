#Insertion Sort
def insertSort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and key < l[j]:
            l[j+1]=l[j]
            j-=1
            l[j+1]=key
        

    return l

l=[20,12,10,15,2]
print(insertSort(l))
