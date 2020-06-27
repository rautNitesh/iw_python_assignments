def tuple_sort(items):
    items=sorted(items,key= lambda tup: tup[1])
    return items


sample_list=[(1,2),(7,3),(2,6),(5,9),(20,1),(1,7)]
print(tuple_sort(sample_list))
