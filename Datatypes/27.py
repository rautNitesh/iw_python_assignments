def replaceLast(l1,l2):
    try:
        if isinstance(l2,list) and isinstance(l1,list):
            l1[len(l1)-1]=l2
        else:
            raise AttributeError("list is required")
        return l1    
    except AttributeError as error:
        return error


l1=[1,5,6]
l2=[5]
print(replaceLast(l1,l2))