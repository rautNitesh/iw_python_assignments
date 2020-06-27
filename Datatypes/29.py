def concateDict(dict1,*args):
    for d in args:
        try:
            if isinstance(d,dict) and isinstance(dict1,dict):
                dict1.update(d)
            else:
                raise ValueError("All values should be dictionary") 
        except ValueError as error:
            return error
    return dict1

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3=7

print(concateDict(dic1,dic2,dic3))