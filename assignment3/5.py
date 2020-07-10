#Linear Search


def linearSearch(l,a):
    if a in l:
        return l.index(a)
    # for i in l:
    #     if a == i
    #         return l.index(a)
    
    
    return "not found"
    
l=[1,2,3,4,5,6,7]
print(linearSearch(l,5))
print(linearSearch(l,57))

