def doSort(l):
    l.sort(key=lambda x: x[1])
    return l

l=[(1,2),(5,6),(7,9),(6,12),(4,3)]
print(doSort(l))