# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def binarySearch(l,first,last,n):
    if last >= first:
        index= (first+last)//2
        if l[index] == n:
            return index
        elif l[index] > n:
            return binarySearch(l,first,index-1,n)
        else:
            return binarySearch(l,index+1,last,n)
    
    return -1


l=[1,2,3,4,5,6,7,8,9]
n=7
first=0
last=len(l)-1
print(binarySearch(l,first,last,n))