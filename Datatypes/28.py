def addKey(d,key,value):
    try:
        if isinstance(d,dict):
            d[key]=value
        else:
            raise AttributeError("First parameter should be dictionary")
    except AttributeError as error:
        return error
    return d

d={'a':1,'b':2,'c':'ram'}
# d=7
key='h'
value=0
print(addKey(d,key,value))