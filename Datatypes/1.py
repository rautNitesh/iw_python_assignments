def count(name):
    d={}
    c=0
    for i in name:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    sorted_dict=sorted(d.items(),reverse=True)
    return dict(sorted_dict)


name= input("Enter string")
print(count(name))
