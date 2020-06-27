def filterIntegers(l):
    func=lambda x: x%2==0
    l=filter(func,l)
    print(list(l))


l=[1,2,3,4,5,6,7,8,9]
filterIntegers(l)