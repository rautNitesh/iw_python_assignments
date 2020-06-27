# def isEmpty(items):
#     if len(items)==0:
#         return True
#     return False

# items=[{},{},{}]
# results=[]
# for i in range(len(items)):
#     results.append(isEmpty(items[i]))

# results=list(dict.fromkeys(results))
# if results[0] and len(results)==1:
#     print("True")
# else:
#     print("False")
def isEmpty(items):
    return all(not d for d in items)

items=[{},{},{1}]
print(isEmpty(items))