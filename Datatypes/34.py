def mergeDict(d1,d2):
    try:
        if isinstance(d1,dict) and isinstance(d2,dict):
            d1.update(d2)
        else:
            raise ValueError("provide dictionaries to merge")
    except ValueError as error:
        return error
    return d1

try:
    n= int(input("Enter length of dictionaries"))
except ValueError:
    print("Enter integer")
d1={}
d2={}
print("Enter for dict1")
for i in range(n):
    a=input("Enter key")
    b=input("Enter value")
    d1[a]=b
print("1Enter for dict2")

for i in range(n):
    a=input("Enter key")
    b=input("Enter value")
    d2[a]=b
print(d1,d2)
print("Merging")

print(mergeDict(d1,d2))