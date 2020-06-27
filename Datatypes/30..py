def keyExistsAlready(d,key):
    try:
        if isinstance(d,dict):
            dkeys=d.keys()
            if key in dkeys:
                return "Exists"
        else:
            raise ValueError("Provide dictionary as first parameter")
    except ValueError as error:
        return error
    return "Doesnot exist"


d={1:1,2:3,3:6}
# d=87
k=2
print(keyExistsAlready(d,k))