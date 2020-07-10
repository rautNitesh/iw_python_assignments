#InterpolationSearch
import math
def interpolationSearch(a,l,h,value):
    if value >= a[l] and value <= a[h]:
        if l==h:
            if a[l]== value:
                return l
            return "Not Found"
        x= l+ (value-a[l])//(a[h]-a[l])* (h-l)
        if a[x]==value:
            return f"Found at {x}"
        if a[x]>value:
            return interpolationSearch(a,l,x-1,value)
        if a[x]< value:
            return interpolationSearch(a,x+1,h,value)
    return "Not found"



l=[1,2,3,4,5,6,7,8,9]
print(interpolationSearch(l,0,(len(l)-1),5)) 
print(interpolationSearch(l,0,(len(l)-1),55)) 