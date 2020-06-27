def duplicate(items):
    items=dict.fromkeys(items)
    return list(items)


items=[1,1,2,3,4,5,5,6,7,8,1,9,8,7,5,3,4,54]
print(duplicate(items))