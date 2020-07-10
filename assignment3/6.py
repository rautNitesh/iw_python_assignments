#BinarySearch

def binarySearch(l,start,end,value):
    if start <= end:
        m= (start+end)//2
        if l[m] == value:
            return f"Found at {m}"
        elif l[m] < value:
            return binarySearch(l, m+1, end , value)
        elif l[m] > value:
            return binarySearch(l,start , m-1 ,value)
    
    return "Not found"

l=[1,2,3,4,5,6,7]
print(binarySearch(l,0,len(l)-1,5))
print(binarySearch(l,0,len(l)-1,57))