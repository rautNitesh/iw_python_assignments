def separateEven(l):
    for i in l:
        if i%2 !=0:
            l.remove(i)
    return l

l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(separateEven(l))