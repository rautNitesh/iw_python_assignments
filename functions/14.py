# def doSort(l):
#     l.sort(key=lambda x: list(x.values()))
#     return l

# l=[{1:8,3:1},{5:6},{7:9},{6:1},{4:3}]
# print(doSort(l))
def doSort(l):
    l.sort(key=lambda x: x['name'])
    return l

l=[{"name":"Nitesh","age":23,"address":"Chitwan"},
{"name":"Ramesh","age":43,"address":"Ganganagar"},
{"name":"Brijesh","age":27,"address":"Bharatpur"},]
print(doSort(l))