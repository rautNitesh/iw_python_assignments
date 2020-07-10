#Bubble Sort in pythonic way.

def sortBubble(l):
    for i in range(len(l)):
        for j in range(i):
            if l[i] < l[j]:
                print(f"{l}\n")
                l[i],l[j]=l[j],l[i]
    return l


l=[9,8,7,6,5,4,3,2,1]
print(sortBubble(l))

        