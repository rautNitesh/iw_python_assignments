def squareCube(l):
    k=[]
    func=lambda x: {x:(x**2,x**3)}
    k+=map(func,l)
    print(list(k))


l=[1,2,3,4,5,6,7,8,9]
squareCube(l)