def mergeSort(l):
    if len(l)> 1 :
        m= len(l)//2

        left= l[:m]
        right=l[m:]
        
        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k]= left[i]
                i+=1
            else:
                l[k]= right[j]
                j+=1
            
            k+=1

        
        while i<len(left):
            l[k]= left[i]
            i+=1
            k+=1


        while j<len(right):
            l[k]= right[j]
            j+=1
            k+=1

    return l


print(mergeSort([9,8,7,6,4,5,2,3,1]))

       

