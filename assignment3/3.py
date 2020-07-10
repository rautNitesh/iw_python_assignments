#Quick Sort in pythonic way

def partition(a,start,end):
    pivot=a[end]
    pindex=start
    for i in range(start , end):
        if a[i]<=pivot:
            a[i],a[pindex]=a[pindex],a[i]
            pindex+=1
    a[pindex],a[end]=a[end],a[pindex]
    return pindex


def quickSort(l,start,end):
    if start >= end:
        return 

    pivot= partition(l,start,end)

    quickSort(l,start,pivot-1)
    quickSort(l,pivot+1,end)


l=[8,2,7,6,4,3,9]
start=0
end= len(l)-1
        
quickSort(l,start,end)
print(l)
    